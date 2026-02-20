
import re
import os
from pathlib import Path

# Mapping of GFM types to Admonition types
TYPE_MAP = {
    "TIP": "tip",
    "NOTE": "note",
    "WARNING": "warning",
    "IMPORTANT": "info", # 'important' is acceptable too usually
    "CAUTION": "failure", # or 'danger'
    "SUCCESS": "success"
}

def fix_file(file_path):
    content = file_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    new_lines = []
    
    i = 0
    while i < len(lines):
        line = lines[i]
        match = re.match(r'^> \[!([A-Z]+)\]', line)
        
        if match:
            gfm_type = match.group(1)
            adm_type = TYPE_MAP.get(gfm_type, "note")
            
            # Look ahead for title or content
            # If next line starts with > **Title**: Content, we can extract title.
            # Otherwise use generic type name as title implicitly.
            
            # Start the admonition block
            # We need to process subsequent lines that start with "> "
            
            # Check specifically for the common "Objetivo" pattern:
            # > [!TIP]
            # > **Objetivo**: Text
            
            title = "" # Default title (empty means capitalized label by default)
            block_content = []
            
            i += 1 # Move to next line to consume content
            while i < len(lines) and (lines[i].startswith(">") or lines[i].strip() == ""):
                sub_line = lines[i]
                if sub_line.startswith(">"):
                    # Remove the quote marker and optional space
                    stripped = sub_line[1:].lstrip()
                    if stripped:
                        block_content.append(stripped)
                    else:
                        block_content.append("") # Empty line inside block query
                else:
                    # Empty line (no >), might be end of block or implicit continuation?
                    # GFM allows lazy continuation?
                    # Usually `> [!TIP]` blocks are contiguous `>`.
                    # Breaking on non `>` line.
                    if sub_line.strip() == "":
                         # Blank line might break the block in some parsers, 
                         # but if we are converting, we might want to keep it if it was intended inside.
                         # But standard GFM requires `>` on blank lines too usually.
                         # If we hit a non-`>` line, we stop.
                         break
                    break
                i += 1
            
            # Heuristic for Title extraction
            # If first line starts with **Title**:
            if block_content and block_content[0].startswith("**") and "**:" in block_content[0]:
                # Extract title
                match_title = re.match(r'\*\*(.*?)\*\*:', block_content[0])
                if match_title:
                    extracted_title = match_title.group(1)
                    title = f' "{extracted_title}"'
                    # Should we remove the **Title**: prefix?
                    # Usually cleaner if we do, but maybe risky.
                    # Admonition header: !!! type "Title"
                    # Body: The rest of the text.
                    # Let's keep the text as is for safety, or just duplicate the title?
                    # If we keep `**Objetivo**: ...` inside the body, it's redundant but safe.
                    pass 
            
            # Reconstruct
            new_lines.append(f'!!! {adm_type}{title}')
            for cl in block_content:
                new_lines.append(f'    {cl}')
            
            # Ensure a blank line after admonition if needed?
            # Standard markdown usually benefits from one.
            continue
            
        else:
            new_lines.append(line)
            i += 1
            
    # Write back
    new_content = "\n".join(new_lines)
    if new_content != content:
        print(f"Fixed {file_path}")
        file_path.write_text(new_content, encoding="utf-8")

def main():
    root = Path(".") / "docs"
    for md_file in root.rglob("*.md"):
        fix_file(md_file)

if __name__ == "__main__":
    main()
