
import re
from pathlib import Path

def parse_termynal_block(block_content):
    lines = block_content.strip().split('\n')
    html_lines = ['<div data-termynal class="termy">']
    
    for line in lines:
        line = line.rstrip()
        if not line:
            continue
            
        if line.startswith('$ '):
            cmd = line[2:]
            html_lines.append(f'    <span data-ty="input">{cmd}</span>')
        elif line.startswith('> '):
            progress = line[2:]
            html_lines.append(f'    <span data-ty="progress">{progress}</span>')
        else:
            # Assume output
            html_lines.append(f'    <span data-ty>{line}</span>')
            
    html_lines.append('</div>')
    return '\n'.join(html_lines)

def fix_file(file_path):
    content = file_path.read_text(encoding="utf-8")
    
    # Regex to find ```termynal ... ``` blocks
    pattern = re.compile(r'```termynal\n(.*?)```', re.DOTALL)
    
    def replacer(match):
        code_block = match.group(1)
        return parse_termynal_block(code_block)
        
    new_content = pattern.sub(replacer, content)
    
    if new_content != content:
        file_path.write_text(new_content, encoding="utf-8")
        print(f"Fixed {file_path}")

def main():
    root = Path(".") / "docs"
    for md_file in root.rglob("*.md"):
        fix_file(md_file)

if __name__ == "__main__":
    main()
