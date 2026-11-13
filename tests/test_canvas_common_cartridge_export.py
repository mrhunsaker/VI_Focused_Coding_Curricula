import tempfile
import unittest
import zipfile
from pathlib import Path
import xml.etree.ElementTree as ET

from canvas_api_full_curriculum_sync import CC_NS, build_common_cartridge


class CommonCartridgeExportTests(unittest.TestCase):
    def test_exports_module_pages_and_local_assets(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "images").mkdir()
            (root / "images" / "diagram.svg").write_text(
                '<svg xmlns="http://www.w3.org/2000/svg"></svg>', encoding="utf-8"
            )
            (root / "SUMMARY.md").write_text(
                "# Summary\n\n# Python\n- [Overview](PYTHON_README.md)\n"
                "  - [Unit 1](unit01.md)\n",
                encoding="utf-8",
            )
            (root / "PYTHON_README.md").write_text(
                "# Python overview\n\n![Diagram](images/diagram.svg)\n"
                "[Unit 1](unit01.md#lesson)\n",
                encoding="utf-8",
            )
            (root / "unit01.md").write_text(
                "# Unit 1\n\nA lesson page.\n", encoding="utf-8"
            )
            output = root / "dist" / "curriculum.imscc"

            result = build_common_cartridge(root, root / "SUMMARY.md", output, "Test Course")

            self.assertEqual(result["modules"], 1)
            self.assertEqual(result["pages"], 2)
            self.assertTrue(output.is_file())
            with zipfile.ZipFile(output) as package:
                self.assertIsNone(package.testzip())
                names = set(package.namelist())
                self.assertIn("imsmanifest.xml", names)
                self.assertIn("web_resources/assets/images/diagram.svg", names)
                manifest = ET.fromstring(package.read("imsmanifest.xml"))
                root_folder = manifest.find(
                    f".//{{{CC_NS}}}organization/{{{CC_NS}}}item"
                )
                self.assertIsNotNone(root_folder)
                modules = root_folder.findall(f"{{{CC_NS}}}item")
                self.assertEqual(len(modules), 1)
                self.assertEqual(
                    len(modules[0].findall(f"{{{CC_NS}}}item")), 2
                )
                overview_name = next(
                    name for name in names
                    if name.startswith("web_resources/pages/0001_")
                )
                overview = package.read(overview_name).decode("utf-8")
                self.assertIn("../assets/images/diagram.svg", overview)
                self.assertIn("0002_unit01.html#lesson", overview)

    def test_missing_summary_link_fails_without_creating_package(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir)
            (root / "SUMMARY.md").write_text(
                "# Course\n- [Missing](missing.md)\n", encoding="utf-8"
            )
            output = root / "missing.imscc"
            with self.assertRaises(FileNotFoundError):
                build_common_cartridge(root, root / "SUMMARY.md", output)
            self.assertFalse(output.exists())

    def test_rejects_paths_outside_source_directory(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            root = Path(temp_dir) / "book"
            root.mkdir()
            (root / "SUMMARY.md").write_text(
                "# Course\n- [Outside](../outside.md)\n", encoding="utf-8"
            )
            with self.assertRaises(ValueError):
                build_common_cartridge(root, root / "SUMMARY.md", root / "out.imscc")


if __name__ == "__main__":
    unittest.main()
