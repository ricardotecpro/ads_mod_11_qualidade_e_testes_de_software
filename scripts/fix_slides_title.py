import pathlib

slides_dir = pathlib.Path("docs/slides")

for html_file in slides_dir.glob("slide-*.html"):
    content = html_file.read_text(encoding="utf-8")
    if "Python Backend" in content:
        new_content = content.replace("Python Backend", "Git e GitHub")
        html_file.write_text(new_content, encoding="utf-8")
        print(f"Updated {html_file.name}")
    else:
        print(f"Skipped {html_file.name} (no match)")
