
import pytest
import re
from pathlib import Path

# Path to the docs directory
DOCS_DIR = Path(__file__).parent.parent / "docs"

def get_mermaid_blocks():
    """
    Generator that yields (file_path, line_number, mermaid_content)
    for every mermaid block found in markdown files.
    """
    for md_file in DOCS_DIR.rglob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        lines = content.splitlines()
        in_mermaid = False
        block_lines = []
        start_line = 0
        
        for i, line in enumerate(lines):
            if line.strip().startswith("```mermaid"):
                in_mermaid = True
                start_line = i + 1
                block_lines = []
            elif line.strip().startswith("```") and in_mermaid:
                in_mermaid = False
                yield (md_file, start_line, block_lines)
            elif in_mermaid:
                block_lines.append(line)

@pytest.mark.parametrize("file_path, start_line, block", list(get_mermaid_blocks()))
def test_mermaid_syntax_safety(file_path, start_line, block):
    """
    Scans Mermaid blocks for common syntax errors, specifically unquoted parentheses in node labels.
    """
    for i, line in enumerate(block):
        line_num = start_line + i + 1
        
        # Check 1: Node labels with parentheses must be quoted
        # Pattern: id[Text (Info)] -> Error
        # Valid: id["Text (Info)"]
        
        # Regex explanation:
        # \[\s*       : Starts with [ and optional whitespace
        # [^"']       : Next char is NOT a quote (meaning it's unquoted start)
        # .*[\(\)].*  : Contains ( or ) anywhere
        # [^"']       : Ends with NOT a quote
        # \s*\]       : Ends with ]
        
        # We need to be careful with simple matches. 
        # A simpler check: if [] contains ( or ), it MUST start with " or '
        
        # Extract content inside []
        matches = re.findall(r'\[(.*?)\]', line)
        for content in matches:
            if '(' in content or ')' in content:
                # Ignore Database shape [()] usage
                if content.strip().startswith('(') and content.strip().endswith(')'):
                    continue
                
                # Check if it is NOT quoted
                stripped = content.strip()
                if not (stripped.startswith('"') and stripped.endswith('"')) and \
                   not (stripped.startswith("'") and stripped.endswith("'")):
                    
                    pytest.fail(
                        f"Mermaid Syntax Error in {file_path}:{line_num}\n"
                        f"Line: {line.strip()}\n"
                        f"Issue: Node label containing parentheses must be quoted.\n"
                        f"Found: [{content}]\n"
                        f"Suggestion: Change to [\"{content}\"]"
                    )
            
            # Check 2: Node labels containing double quotes must be quoted (and escaped if needed)
            if '"' in content:
                 stripped = content.strip()
                 # If it contains " but does NOT start/end with ", it's definitely wrong (e.g. [Text "Quoted"])
                 # If it starts with ", it might be ["Text 'Quoted'"] which is fine, or ["Text "Quoted""] which needs escape.
                 # Simplified check: valid quoted string should start and end with " or '.
                 if not (stripped.startswith('"') and stripped.endswith('"')) and \
                    not (stripped.startswith("'") and stripped.endswith("'")):
                     safe_content = content.replace('"', "'")
                     pytest.fail(
                        f"Mermaid Syntax Error in {file_path}:{line_num}\n"
                        f"Line: {line.strip()}\n"
                        f"Issue: Node label containing quotes must be enclosed in quotes.\n"
                        f"Found: [{content}]\n"
                        f"Suggestion: Change to [\"{safe_content}\"] or escape quotes."
                    )

        # Check 2: Edge labels with parentheses must be quoted (if using -- Text --> style)
        # Check for -- Text (Info) --> pattern
        # This is harder to regex perfectly, but we can look for -- followed by unquoted text with parens
        
        if '--' in line and ('(' in line or ')' in line):
            # Very naive check for unquoted edge labels
            # If we see -- [space] Text (Info) [space] --> 
            # We assume it should be -- "Text (Info)" -->
            pass # Skipping edge check for now as it triggers false positives easily, focusing on Nodes first.
