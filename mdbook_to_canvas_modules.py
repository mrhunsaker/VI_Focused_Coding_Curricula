import os
import re
import zipfile
import markdown
import xml.etree.ElementTree as ET

SUMMARY_FILE = "SUMMARY.md"
SOURCE_DIR = "."  # Root directory containing your markdown folders
OUTPUT_CC = "curriculum_canvas_modules.imscc"

def parse_summary():
    """Parses mdBook SUMMARY.md into modules and pages."""
    modules = []
    current_module = {"title": "General", "items": []}
    
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
                # Ignore external links or anchor links
                if not path.startswith('http') and not path.startswith('#'):
                    current_module["items"].append({"title": title, "path": path})
                    
        if current_module["items"]:
            modules.append(current_module)
            
    return modules

def build_common_cartridge():
    os.makedirs("build_temp", exist_ok=True)
    modules = parse_summary()
    
    # 1. Initialize Common Cartridge Namespace
    ET.register_namespace('', 'http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1')
    manifest = ET.Element('{http://www.imsglobal.org/xsd/imsccv1p1/imscp_v1p1}manifest', {
        'identifier': 'manifest_curriculum',
        'xmlns:xsi': 'http://www.w3.org/2001/XMLSchema-instance',
        'xsi:schemaLocation': 'http://www.imsglobal.org/xsd/imsccv1p1/imsmanifest_v1p1.xsd'
    })
    
    organizations = ET.SubElement(manifest, 'organizations')
    org = ET.SubElement(organizations, 'organization', {'identifier': 'org_curriculum'})
    resources = ET.SubElement(manifest, 'resources')
    
    file_counter = 1
    
    # 2. Iterate through parsed modules and items
    for mod_idx, mod in enumerate(modules):
        # Create a Canvas Module container item
        mod_item_id = f"mod_item_{mod_idx}"
        mod_element = ET.SubElement(org, 'item', {
            'identifier': mod_item_id,
            'identifierref': f"folder_res_{mod_idx}"
        })
        ET.SubElement(mod_element, 'title').text = mod["title"]
        
        for item in mod["items"]:
            md_rel_path = item["path"]
            full_md_path = os.path.join(SOURCE_DIR, md_rel_path)
            
            # Read and convert Markdown to HTML if the file exists
            html_body = f"<p>Content missing for {md_rel_path}</p>"
            if os.path.exists(full_md_path):
                with open(full_md_path, 'r', encoding='utf-8', errors='ignore') as mf:
                    md_content = mf.read()
                    html_body = markdown.markdown(md_content, extensions=['fenced_code', 'tables', 'nl2br'])
            
            html_filename = f"page_{file_counter}.html"
            html_out_path = os.path.join("build_temp", html_filename)
            
            with open(html_out_path, 'w', encoding='utf-8') as out_f:
                out_f.write(f"<html><head><meta charset='utf-8'></head><body>{html_body}</body></html>")
            
            # Add Resource definition
            res_id = f"res_{file_counter}"
            ET.SubElement(resources, 'resource', {
                'identifier': res_id,
                'type': 'webcontent',
                'href': html_filename
            })
            
            # Add child item under module
            child_item = ET.SubElement(mod_element, 'item', {
                'identifier': f"item_{file_counter}",
                'identifierref': res_id
            })
            ET.SubElement(child_item, 'title').text = item["title"]
            
            file_counter += 1

    # 3. Write out imsmanifest.xml
    tree = ET.ElementTree(manifest)
    tree.write(os.path.join("build_temp", "imsmanifest.xml"), encoding='utf-8', xml_declaration=True)

    # 4. Zip into .imscc package
    print(f"Packaging into {OUTPUT_CC}...")
    with zipfile.ZipFile(OUTPUT_CC, 'w', zipfile.ZIP_DEFLATED) as zf:
        for foldername, subfolders, filenames in os.walk("build_temp"):
            for filename in filenames:
                filePath = os.path.join(foldername, filename)
                zf.write(filePath, arcname=filename)
                
    print(f"Success! Canvas-ready Common Cartridge package created: {OUTPUT_CC}")

if __name__ == "__main__":
    build_common_cartridge()
