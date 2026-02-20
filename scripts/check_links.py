import os
import re

def check_links(base_path):
    print(f"Checking links in {base_path}...")
    docs_path = os.path.join(base_path, "docs")
    errors = []
    
    link_pattern = re.compile(r'\[.*?\]\((.*?)\)')
    image_pattern = re.compile(r'!\[.*?\]\((.*?)\)')
    
    ignored_links = ["URL", "URL-da-Imagem", "url", "url-da-imagem.png", "link", "seu@email.com"]

    for root, dirs, files in os.walk(docs_path):
        for file in files:
            if not file.endswith(".md"):
                continue
                
            filepath = os.path.join(root, file)
            rel_path_from_docs = os.path.relpath(filepath, docs_path)
            
            with open(filepath, "r", encoding="utf-8") as f:
                content = f.read()
            
            # Check Links
            for match in link_pattern.findall(content):
                if match.startswith("http") or match.startswith("#") or match.startswith("mailto:") or match in ignored_links:
                    continue
                
                # Resolve relative path
                target_path = os.path.join(os.path.dirname(filepath), match)
                # Handle anchor links like file.md#section (strip anchor)
                if "#" in target_path:
                    target_path = target_path.split("#")[0]
                
                if not os.path.exists(target_path):
                     # Try checking if it's a directory (mkdocs handles directory/index.md)
                     if os.path.isdir(target_path):
                         continue
                     errors.append(f"BROKEN LINK in {rel_path_from_docs}: {match}")

            # Check Images
            for match in image_pattern.findall(content):
                if match.startswith("http") or match in ignored_links:
                    continue
                
                target_path = os.path.join(os.path.dirname(filepath), match)
                if not os.path.exists(target_path):
                    errors.append(f"MISSING IMAGE in {rel_path_from_docs}: {match}")

    if errors:
        print("\n❌ LINK/ASSET ERRORS FOUND:")
        for e in errors:
            print(f"  - {e}")
        return False
    else:
        print("\n✅ No broken internal links or missing images found.")
        return True

if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    check_links(base)
