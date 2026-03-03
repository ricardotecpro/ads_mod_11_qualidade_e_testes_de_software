import glob
import re
import os

def process_slides():
    src_dir = os.path.join("f:\\SourceCode\\REPOS\\github.io\\ads_mod_02_logica_e_algoritmos\\docs\\slides\\.src")
    files = glob.glob(os.path.join(src_dir, "slide-*.md"))
    
    print(f"Found {len(files)} slide files.")

    for file_path in files:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        new_lines = []
        in_code_block = False
        
        for line in lines:
            stripped = line.strip()
            
            # Toggle code block status
            if stripped.startswith('```'):
                in_code_block = not in_code_block
                new_lines.append(line)
                continue
            
            # If in code block, do nothing
            if in_code_block:
                new_lines.append(line)
                continue
            
            # Check for list items
            # Matches: "- Item", "* Item", "1. Item"
            # Does not match if already has { .fragment }
            # Does not match horizontal rules "---"
            is_list_item = (stripped.startswith('- ') or stripped.startswith('* ') or re.match(r'^\d+\. ', stripped))
            is_horizontal_rule = stripped == '---' or stripped == '***'
            
            if is_list_item and not is_horizontal_rule and '{ .fragment }' not in line:
                # Add fragment
                new_lines.append(line.rstrip() + ' { .fragment }\n')
            else:
                new_lines.append(line)
                
        with open(file_path, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        print(f"Processed {os.path.basename(file_path)}")

if __name__ == "__main__":
    process_slides()
