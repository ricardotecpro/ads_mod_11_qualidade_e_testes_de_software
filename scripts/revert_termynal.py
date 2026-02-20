
from pathlib import Path

def fix_file(file_path):
    content = file_path.read_text(encoding="utf-8")
    # Replace ```console with ```termynal
    new_content = content.replace("```console", "```termynal")
    
    if new_content != content:
        file_path.write_text(new_content, encoding="utf-8")
        print(f"Fixed {file_path}")

def main():
    root = Path(".") / "docs"
    for md_file in root.rglob("*.md"):
        fix_file(md_file)

if __name__ == "__main__":
    main()
