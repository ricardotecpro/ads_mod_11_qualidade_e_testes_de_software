
import os
import re
import shutil
import yaml
from pathlib import Path

PROJECT_ROOT = Path("d:/SourceCode/REPOS/github.io/ads_spec_backend_com_python")
DOCS_DIR = PROJECT_ROOT / "docs"
UNUSED_DIR = PROJECT_ROOT / "unused_files_review"

# Add constructor for !ENV tag
yaml.SafeLoader.add_constructor('!ENV', lambda loader, node: str(node.value))

# Regex patterns for finding references
LINK_PATTERN = re.compile(r'\[.*?\]\((.*?)\)')
IMAGE_PATTERN = re.compile(r'!\[.*?\]\((.*?)\)')
SRC_PATTERN = re.compile(r'src=["\'](.*?)["\']')
HREF_PATTERN = re.compile(r'href=["\'](.*?)["\']')

def get_all_files(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            files.append(Path(root) / filename)
    return files

def get_referenced_files():
    referenced = set()
    
    # Check mkdocs.yml
    mkdocs_path = PROJECT_ROOT / "mkdocs.yml"
    if mkdocs_path.exists():
        try:
            content = mkdocs_path.read_text(encoding="utf-8")
            # Regex to find potential file paths
            # Matches strings that shouldn't contain spaces usually in this context
            # Look for typical extensions
            potential_paths = re.findall(r'[\w\-./]+\.(?:md|png|jpg|jpeg|gif|svg|css|js|webp|ico)', content)
            
            for path in potential_paths:
                # Resolve relative to docs_dir (usually)
                # Some might be relative to root (like theme logo?)
                # We check both
                p1 = DOCS_DIR / path
                if p1.exists():
                    referenced.add(p1.resolve())
                
                p2 = PROJECT_ROOT / path
                if p2.exists():
                    referenced.add(p2.resolve())
                    
        except Exception as e:
            print(f"Error scanning mkdocs.yml: {e}")

    # Scan all markdown and HTML files in docs for links/images
    for f in get_all_files(DOCS_DIR):
        if f.suffix in ['.md', '.html']:
            try:
                content = f.read_text(encoding="utf-8")
                # Find all links
                for pattern in [LINK_PATTERN, IMAGE_PATTERN, SRC_PATTERN, HREF_PATTERN]:
                    for match in pattern.finditer(content):
                        ref = match.group(1).split('#')[0].split('?')[0]
                        if not ref or ref.startswith(('http', 'mailto:', 'tel:')):
                            continue
                        
                        # Resolve path
                        # If starts with /, relative to docs root? Or site root?
                        # MkDocs uses relative links usually.
                        if ref.startswith('/'):
                            # Assuming relative to docs root for assets
                            resolved = DOCS_DIR / ref.lstrip('/')
                        else:
                            resolved = (f.parent / ref).resolve()
                        
                        referenced.add(resolved)
            except Exception as e:
                 print(f"Error reading {f}: {e}")
                 
    return referenced

def main():
    print("Starting audit...")
    if not UNUSED_DIR.exists():
        UNUSED_DIR.mkdir()

    all_docs_files = set(get_all_files(DOCS_DIR))
    referenced_files = get_referenced_files()
    
    # Normalize paths
    all_docs_files = {f.resolve() for f in all_docs_files}
    referenced_files = {f.resolve() for f in referenced_files}
    
    # Whitelist specific files
    whitelist = {
        (DOCS_DIR / "CNAME").resolve(),
        (DOCS_DIR / "index.md").resolve(),
        (DOCS_DIR / "print_page.md").resolve(),
    }
    
    # Whitelist Markdown slides (used as source for HTML generation)
    for f in all_docs_files:
        if "slides" in str(f) and "src" in str(f) and f.name.endswith("-slides.md"):
            whitelist.add(f)
        # Also whitelist the runtime markdown files in docs/slides/ (generated)
        if "slides" in str(f) and f.parent.name == "slides" and f.name.endswith("-slides.md"):
            whitelist.add(f)
            
    # Whitelist Quiz source files
    for f in all_docs_files:
        if "quizzes" in str(f) and ".src" in str(f):
            whitelist.add(f)
    
    unused = all_docs_files - referenced_files - whitelist
    
    # Filter out trash dir itself if it was scanned (it shouldn't be if we check existence)
    # Filter out sub-files of already moved dirs?
    
    print(f"Found {len(unused)} unused files in docs/.")
    
    report_file = UNUSED_DIR / "audit_report.txt"
    with open(report_file, "w", encoding="utf-8") as f:
        f.write("Unused Files Report\n===================\n")
        f.write("These files were not found referenced in mkdocs.yml or other files.\n\n")
        
        for file in sorted(unused):
            try:
                rel_path = file.relative_to(PROJECT_ROOT)
                f.write(f"{rel_path}\n")
                
                # Move file
                target = UNUSED_DIR / rel_path
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.move(str(file), str(target))
                print(f"Moved {rel_path} to {target}")
            except Exception as e:
                f.write(f"Error processing {file}: {e}\n")

    print(f"Report written to {report_file}")
    print("Modify script to enable moving.")

if __name__ == "__main__":
    main()
