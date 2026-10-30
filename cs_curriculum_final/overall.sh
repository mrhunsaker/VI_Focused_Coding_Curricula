#!/usr/bin/env bash
set -euo pipefail

# ---------------------------------------------------------------------------
# Defaults (override via command-line flags)
# ---------------------------------------------------------------------------
OUTPUT_DIR="output"
SKIP_PDF=0
NO_PDF_LOGS=0
PDF_ENGINE="xelatex"
MAIN_FONT="DejaVu Serif"
MONO_FONT="DejaVu Sans Mono"
TEMPLATE="template.tex"

usage() {
    cat <<EOF
Usage: $0 [OPTIONS]

Options:
  -o DIR          Output directory (default: output)
  --skip-pdf      Assemble markdown files only; skip PDF generation
  --no-pdf-logs   Disable per-PDF log files and warning summary
  --pdf-engine E  PDF engine passed to pandoc (default: xelatex)
  --main-font F   Body font (default: "DejaVu Serif")
  --mono-font F   Monospace font (default: "DejaVu Sans Mono")
  -h, --help      Show this help message
EOF
}

while [[ $# -gt 0 ]]; do
    case "$1" in
        -o)           OUTPUT_DIR="$2"; shift 2 ;;
        --skip-pdf)   SKIP_PDF=1; shift ;;
        --no-pdf-logs) NO_PDF_LOGS=1; shift ;;
        --pdf-engine) PDF_ENGINE="$2"; shift 2 ;;
        --main-font)  MAIN_FONT="$2"; shift 2 ;;
        --mono-font)  MONO_FONT="$2"; shift 2 ;;
        -h|--help)    usage; exit 0 ;;
        *) echo "Unknown option: $1" >&2; usage; exit 1 ;;
    esac
done

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
OUTPUT_PATH="$SCRIPT_DIR/$OUTPUT_DIR"
LOG_PATH="$OUTPUT_PATH/logs"
RUN_STAMP="$(date '+%Y%m%d_%H%M%S')"

# ---------------------------------------------------------------------------
# Source file lists
# ---------------------------------------------------------------------------
PYTHON_FILES=(
    "python/teachers-guide.md"
    "python/unit00-setup.md"
    "python/unit01-foundations.md"
    "python/unit02-numeric-computations.md"
    "python/unit03-control-flow.md"
    "python/unit04-06-data-functions.md"
    "python/unit07-09-oop-files.md"
    "python/unit10-11-projects-capstone.md"
)

JAVASCRIPT_FILES=(
    "javascript/README.md"
    "javascript/teachers-guide.md"
    "javascript/unit00-01-setup-foundations.md"
    "javascript/unit02-04-io-control-data.md"
    "javascript/unit05-08-strings-functions-oop-files.md"
    "javascript/unit09-11-modules-collections-projects.md"
)

JAVA_FILES=(
    "java/README.md"
    "java/teachers-guide.md"
    "java/unit00-01-setup-foundations.md"
    "java/unit02-04-io-control-arrays.md"
    "java/unit05-08-strings-methods-oop-files.md"
    "java/unit09-11-collections-projects.md"
)

OVERALL_FILES=(
    "${PYTHON_FILES[@]}"
    "${JAVASCRIPT_FILES[@]}"
    "${JAVA_FILES[@]}"

)

# ---------------------------------------------------------------------------
# resolve_required_files <relative_path>...
#   Prints each full path after verifying it exists; exits on first missing.
# ---------------------------------------------------------------------------
resolve_required_files() {
    local full_path
    for relative in "$@"; do
        full_path="$SCRIPT_DIR/$relative"
        if [[ ! -f "$full_path" ]]; then
            echo "ERROR: Missing required file: $relative" >&2
            exit 1
        fi
        echo "$full_path"
    done
}

# ---------------------------------------------------------------------------
# new_combined_markdown <output_file> <source_file>...
#   Concatenates source files into a single markdown file, separated by
#   \newpage directives.  Applies heading-link normalization and glyph fixes.
# ---------------------------------------------------------------------------
new_combined_markdown() {
    local output_file="$1"; shift
    local source_files=("$@")
    local count="${#source_files[@]}"
    local tmp
    tmp="$(mktemp)"

    for (( i = 0; i < count; i++ )); do
        local src="${source_files[$i]}"
        local relative
        local is_language_readme="0"
        relative="$(realpath --relative-to="$SCRIPT_DIR" "$src" 2>/dev/null || python3 -c "import os; print(os.path.relpath('$src', '$SCRIPT_DIR'))")"
        relative="${relative//\\//}"   # normalise Windows back-slashes if present

        if [[ "$relative" =~ ^(python|javascript|java)/README\.md$ ]]; then
            is_language_readme="1"
        fi

        echo "<!-- Source: $relative -->" >> "$tmp"

        # Read content, normalize heading anchor links, replace unsupported glyphs.
        # Anchor normalization: (#1-some-heading) -> (#some-heading); collapse --
        IS_LANGUAGE_README="$is_language_readme" perl -0777 \
            -e 'my $c = do { local $/; <STDIN> };
                # Replace unsupported checkmark glyph
                $c =~ s/\x{2713}/[OK]/g;
                # Normalize anchor links: strip leading digit prefix, collapse hyphens
                $c =~ s/\(#([^)]+)\)/
                    my $a = $1;
                    $a =~ s{^\d+-}{};
                    $a =~ s{-{2,}}{-}g;
                    "(#$a)"
                /ge;
                # For language README files, make first H1 an unnumbered chapter
                # so it is not listed in TOC.
                if ($ENV{IS_LANGUAGE_README} && $ENV{IS_LANGUAGE_README} eq "1") {
                    $c =~ s/^#\s+([^\n]+)\n/\\chapter*{$1}\n\n/m;
                }
                print $c' < "$src" >> "$tmp"

        # Trim trailing whitespace/newlines from last appended content
        # then add separator unless this is the last file
        if (( i < count - 1 )); then
            printf '\n\n\\newpage\n\n' >> "$tmp"
        fi
    done

    # Write final output (no BOM --- UTF-8 plain)
    cp "$tmp" "$output_file"
    rm -f "$tmp"
}

# ---------------------------------------------------------------------------
# add_overall_language_dividers <overall_markdown_file>
#   Inserts LaTeX \part dividers into the omnibus markdown so they appear in
#   the PDF table of contents as parts, while curriculum H1 headings remain
#   chapters.
# ---------------------------------------------------------------------------
add_overall_language_dividers() {
    local overall_md_file="$1"

        perl -0777 -i -pe '
        # Python may be first in the file (no leading newline), so handle
        # beginning-of-file and newline-prefixed matches.
        s/\A(<!-- Source: python\/(?:README|teachers-guide)\.md -->)/
    \\part{Python Curriculum}\n\n$1/;
        s/\n(<!-- Source: python\/(?:README|teachers-guide)\.md -->)/
    \n\\part{Python Curriculum}\n\n$1/g;
        s/\n<!-- Source: javascript\/README\.md -->/
\n\\part{JavaScript Curriculum}\n\n<!-- Source: javascript\/README.md -->/g;
        s/\n<!-- Source: java\/README\.md -->/
\n\\part{JAVA Curriculum}\n\n<!-- Source: java\/README.md -->/g;
    ' "$overall_md_file"
}

# ---------------------------------------------------------------------------
# new_pdf_from_markdown <markdown_file> <pdf_file> [log_file] [introduction_tex_file] [rendered_tex_file]
# ---------------------------------------------------------------------------
new_pdf_from_markdown() {
    local md_file="$1"
    local pdf_file="$2"
    local log_file="${3-}"
    local introduction_tex_file="${4-}"
    local rendered_tex_file="${5-}"

    local tex_exit_code=0
    local pdf_exit_code=0

    run_pandoc_to_tex() {
        if [[ -n "$introduction_tex_file" ]]; then
            pandoc "$md_file" \
                -o "$rendered_tex_file" \
                -t latex \
                --standalone \
                -V "mainfont=$MAIN_FONT" \
                -V "monofont=$MONO_FONT" \
                -V "introduction_tex_file=$introduction_tex_file" \
                --template="$TEMPLATE"
        else
            pandoc "$md_file" \
                -o "$rendered_tex_file" \
                -t latex \
                --standalone \
                -V "mainfont=$MAIN_FONT" \
                -V "monofont=$MONO_FONT" \
                --template="$TEMPLATE"
        fi
    }

    if [[ -n "$log_file" ]]; then
        local log_dir
        log_dir="$(dirname "$log_file")"
        mkdir -p "$log_dir"

        {
            echo "Started: $(date '+%Y-%m-%d %H:%M:%S')"
            echo "Markdown: $md_file"
            echo "PDF: $pdf_file"
            echo ""
        } > "$log_file"

        set +e
        if [[ -n "$rendered_tex_file" ]]; then
            run_pandoc_to_tex 2>&1 | tee -a "$log_file"
            tex_exit_code="${PIPESTATUS[0]}"
        fi

        if [[ "$tex_exit_code" -eq 0 ]]; then
        if [[ -n "$introduction_tex_file" ]]; then
            pandoc "$md_file" \
                -o "$pdf_file" \
                --pdf-engine="$PDF_ENGINE" \
                -V "mainfont=$MAIN_FONT" \
                -V "monofont=$MONO_FONT" \
                -V "introduction_tex_file=$introduction_tex_file" \
                --template="$TEMPLATE" \
                2>&1 | tee -a "$log_file"
        else
            pandoc "$md_file" \
                -o "$pdf_file" \
                --pdf-engine="$PDF_ENGINE" \
                -V "mainfont=$MAIN_FONT" \
                -V "monofont=$MONO_FONT" \
                --template="$TEMPLATE" \
                2>&1 | tee -a "$log_file"
        fi
            pdf_exit_code="${PIPESTATUS[0]}"
        fi
        set -e

        local exit_code="$tex_exit_code"
        if [[ "$exit_code" -eq 0 ]]; then
            exit_code="$pdf_exit_code"
        fi

        echo "Completed: $(date '+%Y-%m-%d %H:%M:%S') ExitCode=$exit_code" >> "$log_file"
    else
        if [[ -n "$rendered_tex_file" ]]; then
            set +e
            run_pandoc_to_tex
            tex_exit_code=$?
            set -e
        fi

        if [[ "$tex_exit_code" -eq 0 ]]; then
            set +e
            if [[ -n "$introduction_tex_file" ]]; then
                pandoc "$md_file" \
                    -o "$pdf_file" \
                    --pdf-engine="$PDF_ENGINE" \
                    -V "mainfont=$MAIN_FONT" \
                    -V "monofont=$MONO_FONT" \
                    -V "introduction_tex_file=$introduction_tex_file" \
                    --template="$TEMPLATE"
            else
                pandoc "$md_file" \
                    -o "$pdf_file" \
                    --pdf-engine="$PDF_ENGINE" \
                    -V "mainfont=$MAIN_FONT" \
                    -V "monofont=$MONO_FONT" \
                    --template="$TEMPLATE"
            fi
            pdf_exit_code=$?
            set -e
        fi

        local exit_code="$tex_exit_code"
        if [[ "$exit_code" -eq 0 ]]; then
            exit_code="$pdf_exit_code"
        fi
    fi

    if [[ "${exit_code:-0}" -ne 0 ]]; then
        echo "ERROR: Pandoc failed while creating: $pdf_file" >&2
        exit 1
    fi
}

# ---------------------------------------------------------------------------
# new_introduction_tex_from_readme <readme_md> <intro_tex>
#   Converts root README markdown into a LaTeX fragment for front-matter
#   Introduction (drops the first H1 heading).
# ---------------------------------------------------------------------------
new_introduction_tex_from_readme() {
    local readme_md="$1"
    local intro_tex="$2"

    perl -0777 -pe 's/\A#\s+[^\n]+\n+//' "$readme_md" \
        | pandoc -f markdown -t latex --top-level-division=chapter \
        > "$intro_tex"
}

# ---------------------------------------------------------------------------
# write_pdf_warning_summary <summary_file> <log_file>...
# ---------------------------------------------------------------------------
write_pdf_warning_summary() {
    local summary_file="$1"; shift
    local log_files=("$@")

    {
        echo "PDF Warning Summary"
        echo "Generated: $(date '+%Y-%m-%d %H:%M:%S')"
        echo ""

        local all_warnings=()
        for lf in "${log_files[@]}"; do
            if [[ -f "$lf" ]]; then
                while IFS= read -r line; do
                    all_warnings+=("$line")
                done < <(grep '\[WARNING\]' "$lf" | sed 's/^[[:space:]]*//' || true)
            fi
        done

        if [[ ${#all_warnings[@]} -eq 0 ]]; then
            echo "No warnings were found in PDF logs."
        else
            # Count unique warnings, sort by frequency descending
            printf '%s\n' "${all_warnings[@]}" \
                | sort \
                | uniq -c \
                | sort -rn \
                | awk '{ count=$1; $1=""; sub(/^ /,""); printf "%dx %s\n", count, $0 }'
        fi
    } > "$summary_file"
}

# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
mkdir -p "$OUTPUT_PATH"

if [[ "$SKIP_PDF" -eq 0 ]] && ! command -v pandoc &>/dev/null; then
    echo "ERROR: Pandoc is required unless --skip-pdf is specified." >&2
    exit 1
fi

pdf_log_files=()

# Per-language builds
declare -A LANG_FILES_MAP
# Bash 4 doesn't support arrays-of-arrays; iterate per language directly.

build_language() {
    local lang="$1"; shift
    local lang_files=("$@")

    local resolved_files=()
    while IFS= read -r f; do
        resolved_files+=("$f")
    done < <(resolve_required_files "${lang_files[@]}")

    local lang_md="$OUTPUT_PATH/${lang}_curriculum.md"
    local lang_tex="$OUTPUT_PATH/${lang}_curriculum.tex"
    local lang_pdf="$OUTPUT_PATH/${lang}_curriculum.pdf"

    new_combined_markdown "$lang_md" "${resolved_files[@]}"
    echo "Created: $lang_md"

    if [[ "$SKIP_PDF" -eq 0 ]]; then
        local log_file=""
        if [[ "$NO_PDF_LOGS" -eq 0 ]]; then
            log_file="$LOG_PATH/pdf_${lang}_${RUN_STAMP}.log"
            pdf_log_files+=("$log_file")
        fi
        new_pdf_from_markdown "$lang_md" "$lang_pdf" "$log_file" "" "$lang_tex"
        echo "Created: $lang_tex"
        echo "Created: $lang_pdf"
    fi
}

build_language "python"     "${PYTHON_FILES[@]}"
build_language "java"       "${JAVA_FILES[@]}"
build_language "javascript" "${JAVASCRIPT_FILES[@]}"

# Combined all-curricula build
overall_resolved=()
while IFS= read -r f; do
    overall_resolved+=("$f")
done < <(resolve_required_files "${OVERALL_FILES[@]}")

overall_md="$OUTPUT_PATH/all_curricula.md"
overall_tex="$OUTPUT_PATH/all_curricula.tex"
overall_pdf="$OUTPUT_PATH/all_curricula.pdf"
overall_intro_tex="$OUTPUT_PATH/overall_introduction_from_readme.tex"

new_combined_markdown "$overall_md" "${overall_resolved[@]}"
add_overall_language_dividers "$overall_md"
new_introduction_tex_from_readme "$SCRIPT_DIR/README.md" "$overall_intro_tex"
echo "Created: $overall_md"

if [[ "$SKIP_PDF" -eq 0 ]]; then
    overall_log=""
    if [[ "$NO_PDF_LOGS" -eq 0 ]]; then
        overall_log="$LOG_PATH/pdf_all_curricula_${RUN_STAMP}.log"
        pdf_log_files+=("$overall_log")
    fi
    new_pdf_from_markdown "$overall_md" "$overall_pdf" "$overall_log" "$overall_intro_tex" "$overall_tex"
    echo "Created: $overall_tex"
    echo "Created: $overall_pdf"

    if [[ "$NO_PDF_LOGS" -eq 0 ]]; then
        summary_file="$LOG_PATH/pdf_warning_summary_${RUN_STAMP}.txt"
        write_pdf_warning_summary "$summary_file" "${pdf_log_files[@]}"
        echo "Created: $summary_file"
    fi
fi

echo "Curriculum build complete."
