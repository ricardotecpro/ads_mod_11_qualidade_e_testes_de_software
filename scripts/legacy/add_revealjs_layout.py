import glob
import os

files = glob.glob('docs/slides/*-slides.md')
print(f"Found {len(files)} files to update.")

for file_path in files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'layout: revealjs' in content:
        print(f"Skipping {file_path} (already has layout)")
        continue
    
    # Insert layout: revealjs after the first ---
    if content.startswith('---\n'):
        new_content = content.replace('---\n', '---\nlayout: revealjs\n', 1)
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"Skipping {file_path} (no frontmatter found)")
