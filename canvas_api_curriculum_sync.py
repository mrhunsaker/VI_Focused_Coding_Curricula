import os
import re
import markdown
from canvasapi import Canvas

# --- CONFIGURATION ---
API_URL = "https://your-institution.instructure.com"  # Your Canvas instance URL
API_KEY = "your_canvas_bearer_token_here"            # Your Canvas Generated Access Token
COURSE_ID = 123456                                   # Your Canvas Course ID
SUMMARY_FILE = "SUMMARY.md"
SOURCE_DIR = "."
POINTS_PER_ASSIGNMENT = 10                           # Default points for each lesson assignment
# ---------------------

def parse_summary():
    """Parses mdBook SUMMARY.md into modules and lessons."""
    modules = []
    current_module = {"title": "General", "items": []}
    
    if not os.path.exists(SUMMARY_FILE):
        print(f"Error: {SUMMARY_FILE} not found.")
        return modules
        
    with open(SUMMARY_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line_stripped = line.strip()
            if not line_stripped:
                continue
                
            # Check for section headers (e.g., # C, # PYTHON)
            if line_stripped.startswith('#'):
                if current_module["items"]:
                    modules.append(current_module)
                mod_title = line_stripped.lstrip('#').strip()
                current_module = {"title": mod_title, "items": []}
                continue
                
            # Check for markdown links (e.g., - [Unit 0](C/unit00...md))
            match = re.search(r'\[([^\]]+)\]\(([^)]+)\)', line_stripped)
            if match:
                title, path = match.groups()
                if not path.startswith('http') and not path.startswith('#'):
                    current_module["items"].append({"title": title, "path": path})
                    
        if current_module["items"]:
            modules.append(current_module)
            
    return modules

def sync_to_canvas():
    canvas = Canvas(API_URL, API_KEY)
    try:
        course = canvas.get_course(COURSE_ID)
        print(f"Connected to Canvas Course: {course.name}")
    except Exception as e:
        print(f"Failed to connect to Canvas. Check your URL, Token, and Course ID. Error: {e}")
        return

    modules_data = parse_summary()
    
    for mod_idx, mod_info in enumerate(modules_data):
        mod_title = mod_info["title"]
        print(f"\nProcessing Module [{mod_title}]...")
        
        # 1. Create or get the Canvas Module container
        canvas_module = course.create_module({'name': mod_title})
        
        for item in mod_info["items"]:
            lesson_title = item["title"]
            md_rel_path = item["path"]
            full_md_path = os.path.join(SOURCE_DIR, md_rel_path)
            
            # Read and convert Markdown to HTML
            html_body = f"<p>Content missing for {md_rel_path}</p>"
            if os.path.exists(full_md_path):
                with open(full_md_path, 'r', encoding='utf-8', errors='ignore') as mf:
                    md_content = mf.read()
                    html_body = markdown.markdown(md_content, extensions=['fenced_code', 'tables', 'nl2br'])
            
            # 2. Create the Lesson Page in Canvas
            print(f"  Creating Page: {lesson_title}")
            page = course.create_page({
                'wiki_page': {
                    'title': lesson_title,
                    'body': html_body,
                    'published': True
                }
            })
            
            # Add Page to the Canvas Module
            canvas_module.create_module_item({
                'module_item': {
                    'type': 'Page',
                    'content_id': page.page_id,
                    'title': lesson_title,
                    'page_url': page.url
                }
            })
            
            # 3. Create a Native Assignment for File Uploads
            assignment_title = f"Assignment: {lesson_title}"
            print(f"  Creating Assignment: {assignment_title}")
            
            assignment_description = f"""
            <p><strong>Lesson Deliverable Upload</strong></p>
            <p>Please upload all completed code files, scripts, exercises, or project deliverables associated with <em>{lesson_title}</em>.</p>
            <p>Accepted formats include source code files (.py, .c, .cpp, .rs, .js, etc.), PDFs, or zipped workspace folders.</p>
            """
            
            assignment = course.create_assignment({
                'assignment': {
                    'name': assignment_title,
                    'description': assignment_description,
                    'points_possible': POINTS_PER_ASSIGNMENT,
                    'submission_types': ['online_upload'],
                    'allowed_extensions': ['zip', 'tar', 'gz', 'c', 'cpp', 'py', 'rs', 'js', 'go', 'java', 'cs', 'txt', 'pdf'],
                    'published': True
                }
            })
            
            # Add Native Assignment to the Canvas Module right after the page
            canvas_module.create_module_item({
                'module_item': {
                    'type': 'Assignment',
                    'content_id': assignment.id,
                    'title': assignment_title
                }
            })

    print("\nCurriculum synchronization completed successfully!")

if __name__ == "__main__":
    sync_to_canvas()