"""Export an mdBook curriculum as IMS Common Cartridge or sync it through Canvas API.

Offline export:
    python canvas_api_full_curriculum_sync.py --export-imscc dist/curriculum.imscc

API sync (requires Canvas credentials in .env):
    python canvas_api_full_curriculum_sync.py
"""
from __future__ import annotations

import argparse
import html
import os
import re
import tempfile
import uuid
import zipfile
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit
import xml.etree.ElementTree as ET

import markdown

SUMMARY_LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
HTML_URL_RE = re.compile(r"(?P<attr>href|src)=(?P<quote>['\"])(?P<url>.*?)(?P=quote)", re.IGNORECASE)
CC_NS = "/xsd/imsccv1p2/imscp_v1p1"
LOM_NS = "http://ltsc.ieee.org/xsd/imsccv1p2/LOM/manifest"
XSI_NS = "http://www.w3.org/2001/XMLSchema-instance"
ET.register_namespace("", CC_NS)
ET.register_namespace("xsi", XSI_NS)
ET.register_namespace("lomimscc", LOM_NS)

MARKDOWN_EXTENSIONS = ["fenced_code", "tables", "nl2br"]


def slugify(value: str) -> str:
    """Return a stable, filesystem-safe ASCII-ish slug."""
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value.strip()).strip("-._")
    return (value or "page")[:80].lower()


def parse_summary(summary_path: Path, source_root: Path) -> list[dict]:
    """Read mdBook SUMMARY.md into ordered module/page records."""
    if not summary_path.is_file():
        raise FileNotFoundError(f"mdBook summary file not found: {summary_path}")

    modules: list[dict] = []
    current = {"title": "General", "items": []}

    for line_number, line in enumerate(summary_path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            if current["items"]:
                modules.append(current)
            title = stripped.lstrip("#").strip()
            current = {"title": title or "Untitled module", "items": []}
            continue

        match = SUMMARY_LINK_RE.search(stripped)
        if not match:
            continue
        title, raw_target = match.groups()
        parsed = urlsplit(raw_target.strip())
        if parsed.scheme or parsed.netloc or not parsed.path:
            continue

        relative_path = Path(unquote(parsed.path))
        source_path = (source_root / relative_path).resolve()
        try:
            source_path.relative_to(source_root.resolve())
        except ValueError as exc:
            raise ValueError(
                f"SUMMARY.md line {line_number} links outside the source directory: {raw_target}"
            ) from exc

        current["items"].append({
            "title": title.strip(),
            "source_path": source_path,
            "source_relative": source_path.relative_to(source_root.resolve()),
            "fragment": parsed.fragment,
            "indent": 1 if len(line) - len(line.lstrip(" ")) > 0 else 0,
        })

    if current["items"]:
        modules.append(current)

    if not modules:
        raise ValueError(f"No local Markdown links were found in {summary_path}")
    return modules


def _safe_asset_path(source_root: Path, source_file: Path, url: str) -> Path | None:
    """Resolve a local href/src target while rejecting traversal outside the book."""
    parsed = urlsplit(html.unescape(url))
    if parsed.scheme or parsed.netloc or not parsed.path:
        return None
    candidate = (source_file.parent / unquote(parsed.path)).resolve()
    try:
        candidate.relative_to(source_root.resolve())
    except ValueError:
        return None
    return candidate


def build_common_cartridge(
    source_root: Path,
    summary_path: Path,
    output_path: Path,
    course_title: str = "mdBook Curriculum",
) -> dict:
    """Build a Common Cartridge 1.2 package containing pages and module structure.

    The package uses standard webcontent resources. It does not create native graded
    Canvas assignments, quizzes, discussions, gradebook settings, or API-side content.
    """
    source_root = source_root.resolve()
    summary_path = summary_path.resolve()
    if not summary_path.is_relative_to(source_root):
        raise ValueError("SUMMARY.md must be inside the source directory")

    modules = parse_summary(summary_path, source_root)
    page_records: list[dict] = []
    source_to_page: dict[Path, str] = {}

    for module_index, module in enumerate(modules, 1):
        for item_index, item in enumerate(module["items"], 1):
            source_file = item["source_path"]
            if source_file.suffix.lower() != ".md":
                raise ValueError(f"SUMMARY.md entry is not a Markdown file: {source_file}")
            if not source_file.is_file():
                raise FileNotFoundError(f"Linked Markdown file does not exist: {source_file}")
            if source_file not in source_to_page:
                page_name = (
                    f"{len(page_records) + 1:04d}_"
                    f"{slugify(source_file.stem)}.html"
                )
                source_to_page[source_file] = f"web_resources/pages/{page_name}"
                page_records.append({
                    "source_file": source_file,
                    "href": source_to_page[source_file],
                    "title": item["title"],
                    "assets": set(),
                })
            item["resource_href"] = source_to_page[source_file]

    page_by_source = {record["source_file"]: record for record in page_records}
    package_files: dict[str, bytes] = {}

    for record in page_records:
        source_file = record["source_file"]
        markdown_text = source_file.read_text(encoding="utf-8")
        body = markdown.markdown(markdown_text, extensions=MARKDOWN_EXTENSIONS)
        current_href = record["href"]

        def rewrite_url(match: re.Match) -> str:
            attr = match.group("attr")
            quote = match.group("quote")
            original_url = match.group("url")
            parsed = urlsplit(html.unescape(original_url))
            if parsed.scheme or parsed.netloc or not parsed.path:
                return match.group(0)

            target = _safe_asset_path(source_root, source_file, original_url)
            if target is None or not target.exists() or not target.is_file():
                return match.group(0)

            if target.suffix.lower() == ".md" and target in source_to_page:
                target_href = source_to_page[target]
                relative = os.path.relpath(
                    target_href, str(PurePosixPath(current_href).parent)
                ).replace(os.sep, "/")
                rewritten = relative
            else:
                asset_relative = target.relative_to(source_root).as_posix()
                asset_href = f"web_resources/assets/{asset_relative}"
                package_files[asset_href] = target.read_bytes()
                record["assets"].add(asset_href)
                rewritten = os.path.relpath(
                    asset_href, str(PurePosixPath(current_href).parent)
                ).replace(os.sep, "/")

            if parsed.fragment:
                rewritten += "#" + parsed.fragment
            if parsed.query:
                rewritten += "?" + parsed.query
            return f"{attr}={quote}{html.escape(rewritten, quote=True)}{quote}"

        body = HTML_URL_RE.sub(rewrite_url, body)
        document = (
            "<!doctype html>\n"
            '<html lang="en">\n<head>\n'
            '<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
            f"<title>{html.escape(record['title'])}</title>\n"
            "</head>\n<body>\n"
            f"{body}\n"
            "</body>\n</html>\n"
        )
        package_files[current_href] = document.encode("utf-8")

    manifest = ET.Element(
        f"{{{CC_NS}}}manifest",
        {
            "identifier": "MANIFEST_" + uuid.uuid4().hex,
            f"{{{XSI_NS}}}schemaLocation": (
                f"{CC_NS} /profile/cc/ccv1p2/ccv1p2_imscp_v1p1_v1p0.xsd "
            f"{LOM_NS} /profile/cc/ccv1p2/LOM/ccv1p2_lommanifest_v1p0.xsd"
            ),
        },
    )
    metadata = ET.SubElement(manifest, f"{{{CC_NS}}}metadata")
    ET.SubElement(metadata, f"{{{CC_NS}}}schema").text = "1EdTech Common Cartridge"
    ET.SubElement(metadata, f"{{{CC_NS}}}schemaversion").text = "1.2.0"
    lom = ET.SubElement(metadata, f"{{{LOM_NS}}}lom")
    general = ET.SubElement(lom, f"{{{LOM_NS}}}general")
    lom_title = ET.SubElement(general, f"{{{LOM_NS}}}title")
    ET.SubElement(lom_title, f"{{{LOM_NS}}}string", {"language": "en-US"}).text = course_title
    lom_description = ET.SubElement(general, f"{{{LOM_NS}}}description")
    ET.SubElement(lom_description, f"{{{LOM_NS}}}string", {"language": "en-US"}).text = (
        "Course pages generated from an mdBook curriculum using Common Cartridge 1.2."
    )

    organizations = ET.SubElement(manifest, f"{{{CC_NS}}}organizations")
    organization = ET.SubElement(
        organizations,
        f"{{{CC_NS}}}organization",
        {"identifier": "ORG1", "structure": "rooted-hierarchy"},
    )
    ET.SubElement(organization, f"{{{CC_NS}}}title").text = course_title
    root_folder = ET.SubElement(
        organization, f"{{{CC_NS}}}item", {"identifier": "ROOT_FOLDER"}
    )

    resources = ET.SubElement(manifest, f"{{{CC_NS}}}resources")
    resource_counter = 0
    item_counter = 0

    for module_index, module in enumerate(modules, 1):
        module_node = ET.SubElement(
            root_folder, f"{{{CC_NS}}}item", {"identifier": f"MODULE_{module_index:04d}"}
        )
        ET.SubElement(module_node, f"{{{CC_NS}}}title").text = module["title"]
        for item in module["items"]:
            resource_counter += 1
            item_counter += 1
            resource_id = f"RESOURCE_{resource_counter:05d}"
            cartridge_item = ET.SubElement(
                module_node,
                f"{{{CC_NS}}}item",
                {"identifier": f"ITEM_{item_counter:05d}", "identifierref": resource_id},
            )
            ET.SubElement(cartridge_item, f"{{{CC_NS}}}title").text = item["title"]
            resource = ET.SubElement(
                resources,
                f"{{{CC_NS}}}resource",
                {"identifier": resource_id, "type": "webcontent", "href": item["resource_href"]},
            )
            ET.SubElement(resource, f"{{{CC_NS}}}file", {"href": item["resource_href"]})
            record = page_by_source[item["source_path"]]
            for asset_href in sorted(record["assets"]):
                ET.SubElement(resource, f"{{{CC_NS}}}file", {"href": asset_href})

    manifest_bytes = ET.tostring(manifest, encoding="utf-8", xml_declaration=True)
    ET.fromstring(manifest_bytes)  # Fail before writing if XML is not well-formed.

    output_path = output_path.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        prefix=output_path.name + ".", suffix=".tmp", dir=output_path.parent, delete=False
    ) as temp_file:
        temporary_path = Path(temp_file.name)
    try:
        with zipfile.ZipFile(temporary_path, "w", compression=zipfile.ZIP_DEFLATED) as archive:
            archive.writestr("imsmanifest.xml", manifest_bytes)
            for archive_name, payload in sorted(package_files.items()):
                archive.writestr(archive_name, payload)
        with zipfile.ZipFile(temporary_path, "r") as archive:
            bad_member = archive.testzip()
            if bad_member:
                raise zipfile.BadZipFile(f"Corrupt package member: {bad_member}")
            names = set(archive.namelist())
            if "imsmanifest.xml" not in names:
                raise zipfile.BadZipFile("Package is missing imsmanifest.xml")
            parsed_manifest = ET.fromstring(archive.read("imsmanifest.xml"))
            for href in parsed_manifest.findall(f".//{{{CC_NS}}}resource/{{{CC_NS}}}file"):
                if href.attrib["href"] not in names:
                    raise zipfile.BadZipFile(f"Manifest references missing file: {href.attrib['href']}")
        temporary_path.replace(output_path)
    except Exception:
        temporary_path.unlink(missing_ok=True)
        raise

    return {
        "output": output_path,
        "modules": len(modules),
        "pages": len(page_records),
        "files": len(package_files) + 1,
        "bytes": output_path.stat().st_size,
    }


def sync_to_canvas(source_root: Path, summary_path: Path) -> None:
    """Create Canvas Modules, Pages, and upload Assignments through the Canvas API."""
    try:
        from dotenv import load_dotenv
        from canvasapi import Canvas
    except ImportError as exc:
        raise RuntimeError(
            "API sync requires canvasapi and python-dotenv. Install them with "
            "'python -m pip install canvasapi python-dotenv'."
        ) from exc

    load_dotenv(source_root / ".env")
    api_url = os.getenv("CANVAS_API_URL")
    api_key = os.getenv("CANVAS_API_KEY")
    course_id_raw = os.getenv("CANVAS_COURSE_ID")
    try:
        points_per_assignment = int(os.getenv("POINTS_PER_ASSIGNMENT", "10"))
        course_id = int(course_id_raw or "")
    except ValueError as exc:
        raise ValueError("CANVAS_COURSE_ID and POINTS_PER_ASSIGNMENT must be integers") from exc
    if not api_url or not api_key or not course_id_raw:
        raise ValueError("Set CANVAS_API_URL, CANVAS_API_KEY, and CANVAS_COURSE_ID in .env")

    modules = parse_summary(summary_path, source_root)
    canvas = Canvas(api_url, api_key)
    course = canvas.get_course(course_id)
    print(f"Connected to Canvas course: {course.name}")

    for module_data in modules:
        canvas_module = course.create_module({"name": module_data["title"]})
        for item in module_data["items"]:
            source_file = item["source_path"]
            markdown_text = source_file.read_text(encoding="utf-8")
            html_body = markdown.markdown(markdown_text, extensions=MARKDOWN_EXTENSIONS)
            page = course.create_page({
                "title": item["title"], "body": html_body, "published": True
            })
            canvas_module.create_module_item({
                "type": "Page", "title": item["title"],
                "page_url": page.url, "indent": item["indent"],
            })
            is_lesson = any(
                word in str(item["source_relative"]).lower()
                for word in ("unit", "lesson", "bash", "powershell")
            )
            if is_lesson:
                assignment_title = f"Assignment: {item['title']}"
                assignment = course.create_assignment({
                    "name": assignment_title,
                    "description": (
                        "<p>Upload completed files, scripts, or workspace deliverables "
                        f"for <strong>{html.escape(item['title'])}</strong>.</p>"
                    ),
                    "points_possible": points_per_assignment,
                    "submission_types": ["online_upload"],
                    "allowed_extensions": [
                        "zip", "tar", "py", "c", "cpp", "rs", "js", "go",
                        "java", "cs", "txt", "pdf",
                    ],
                    "published": True,
                })
                canvas_module.create_module_item({
                    "type": "Assignment", "content_id": assignment.id,
                    "title": assignment_title, "indent": item["indent"],
                })
    print("Canvas API curriculum sync completed.")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Export mdBook content as IMS Common Cartridge or sync to Canvas via API."
    )
    parser.add_argument(
        "--source-dir", type=Path, default=Path("."),
        help="mdBook source directory (default: current directory)",
    )
    parser.add_argument(
        "--summary", type=Path, default=Path("SUMMARY.md"),
        help="mdBook summary file relative to --source-dir (default: SUMMARY.md)",
    )
    parser.add_argument(
        "--export-imscc", type=Path, metavar="OUTPUT.imscc",
        help="create an offline Common Cartridge package; no Canvas API token is needed",
    )
    parser.add_argument(
        "--title", default="VI Focused Coding Curricula",
        help="course title stored in the Common Cartridge manifest",
    )
    args = parser.parse_args()

    source_root = args.source_dir.resolve()
    summary_path = args.summary if args.summary.is_absolute() else source_root / args.summary
    if args.export_imscc:
        output = args.export_imscc
        if not output.is_absolute():
            output = source_root / output
        result = build_common_cartridge(source_root, summary_path, output, args.title)
        print(
            f"Created {result['output']} ({result['bytes']:,} bytes): "
            f"{result['modules']} modules, {result['pages']} pages, "
            f"{result['files']} package files."
        )
        print("This is an IMS Common Cartridge 1.2 web-content package, not a live Canvas API sync.")
        return 0

    sync_to_canvas(source_root, summary_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
