import os
import re
import markdown
from dotenv import load_dotenv
from canvasapi import Canvas

# Load environment variables from .env file
load_dotenv()

# --- CONFIGURATION FROM .ENV ---
API_URL = os.getenv("CANVAS_API_URL")
API_KEY = os.getenv("CANVAS_API_KEY")
COURSE_ID_RAW = os.getenv("CANVAS_COURSE_ID")
POINTS_PER_ASSIGNMENT = int(os.getenv("POINTS_PER_ASSIGNMENT", 10))
# -------------------------------

SUMMARY_FILE = "SUMMARY.md"
SOURCE_DIR = "."

def validate_config():
    if not API_URL or not API_KEY or not COURSE_ID_RAW:
        print("❌ Error: Missing configuration variables in your .env file.")
        print("Please ensure CANVAS_API_URL, CANVAS_API_KEY, and CANVAS_COURSE_ID are set.")
        return False
    return True

def parse_summary_with_tracks():
    """Parses mdBook SUMMARY.md, capturing all files and tracking indentation/tracks."""
    modules = []
    current_module = {"title": "General", "items": []}
    
    if not os.path.exists(SUMMARY_FILE):
        print(f"❌ Error: {SUMMARY_FILE} not found.")
        return modules
        
    with open(SUMMARY_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            leading_spaces = len(line) - len(line.lstrip(' '))
            line_stripped = line.strip()
            
            if not line_stripped:
                continue
                
            # Capture Top-Level Headers (#) as Canvas Modules
            if line_stripped.startswith('#'):
                if current_module["items"]:
                    modules.append(current_module)
                mod_title = line_stripped.lstrip('#').strip()
                current_module = {"title": mod_title, "items": []}
                continue
                
            # Extract Markdown Links: [Title](Path)
            match = re.search(r'\[([^\]]+)\]\(([^)]+)\)', line_stripped)
            if match:
                title, path = match.groups()
                
                if path.startswith('http') or path.startswith('#'):
                    continue
                
                indent_level = 1 if leading_spaces > 0 else 0
                
                current_module["items"].append({
                    "title": title,
                    "path": path,
                    "indent": indent_level
                })
                
    if current_module["items"]:
        modules.append(current_module)
        
    return modules

def sync_to_canvas():
    if not validate_config():
        return

    canvas = Canvas(API_URL, API_KEY)
    try:
        course = canvas.get_course(int(COURSE_ID_RAW))
        print(f"🔗 Connected to Canvas Course: {course.name}")
    except Exception as e:
        print(f"❌ Failed to connect to Canvas. Check credentials and Course ID. Error: {e}")
        return

    modules_data = parse_summary_with_tracks()
    
    for mod_info in modules_data:
        mod_title = mod_info["title"]
        print(f"\n📦 Processing Module: [{mod_title}]")
        
        canvas_module = course.create_module({'name': mod_title})
        
        for item in mod_info["items"]:
            title = item["title"]
            md_rel_path = item["path"]
            indent_lvl = item["indent"]
            full_md_path = os.path.join(SOURCE_DIR, md_rel_path)
            
            html_body = f"<p>Content missing for {md_rel_path}</p>"
            if os.path.exists(full_md_path):
                with open(full_md_path, 'r', encoding='utf-8', errors='ignore') as mf:
                    md_content = mf.read()
                    html_body = markdown.markdown(md_content, extensions=['fenced_code', 'tables', 'nl2br'])
            
            # 1. Create the Canvas Page
            print(f"  Creating Page (Indent: {indent_lvl}): {title}")
            page = course.create_page({
                'wiki_page': {
                    'title': title,
                    'body': html_body,
                    'published': True
                }
            })
            
            canvas_module.create_module_item({
                'module_item': {
                    'type': 'Page',
                    'content_id': page.page_id,
                    'title': title,
                    'page_url': page.url,
                    'indent': indent_lvl
                }
            })
            
            # 2. Conditionally append assignment for lesson/track files
            is_lesson_file = any(keyword in md_rel_path.lower() for keyword in ["unit", "lesson", "bash", "powershell"])
            
            if is_lesson_file:
                assignment_title = f"Assignment: {title}"
                print(f"    ↳ Creating Assignment for: {title}")
                
                assignment = course.create_assignment({
                    'assignment': {
                        'name': assignment_title,
                        'description': f"<p>Please upload all completed files, scripts, or workspace deliverables for <strong>{title}</strong>.</p>",
                        'points_possible': POINTS_PER_ASSIGNMENT,
                        'submission_types': ['online_upload'],
                        'allowed_extensions': ['zip', 'tar', 'py', 'c', 'cpp', 'rs', 'js', 'go', 'java', 'cs', 'txt', 'pdf'],
                        'published': True
                    }
                })
                
                canvas_module.create_module_item({
                    'module_item': {
                        'type': 'Assignment',
                        'content_id': assignment.id,
                        'title': assignment_title,
                        'indent': indent_lvl
                    }
                })

    print("\n✅ Curriculum synchronization completed successfully!")

if __name__ == "__main__":
    sync_to_canvas()