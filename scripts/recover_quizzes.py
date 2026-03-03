
import pathlib
import re
from rich import print

def recover_quiz(html_path: pathlib.Path, src_dir: pathlib.Path):
    content = html_path.read_text(encoding='utf-8')
    
    # Regex to extract questions from HTML
    # <div class="quiz-question">1. Question text</div>
    q_pattern = r'<div class="quiz-question">(\d+)\.\s+(.*?)</div>'
    
    # <div class="quiz-option" data-correct="true/false" ...>Option text</div>
    opt_pattern = r'<div class="quiz-option" data-correct="(true|false)"[^>]*>(.*?)</div>'
    
    questions = []
    
    # Split by quiz-container to handle order
    containers = content.split('<div class="quiz-container">')
    
    for container in containers[1:]: # Skip preamble
        q_match = re.search(q_pattern, container)
        if not q_match:
            continue
            
        q_num = q_match.group(1)
        q_text = q_match.group(2)
        
        options = []
        for opt_match in re.finditer(opt_pattern, container):
            is_correct = opt_match.group(1) == 'true'
            opt_text = opt_match.group(2)
            options.append((opt_text, is_correct))
            
        questions.append({
            'num': q_num,
            'text': q_text,
            'options': options
        })
        
    if not questions:
        print(f"[yellow]Skipping {html_path.name}: No questions found (maybe already Markdown?)[/yellow]")
        return

    # Generate Markdown
    md_lines = [f"# Quiz {html_path.name.replace('quiz-', '').replace('.md', '')}\n"]
    
    for q in questions:
        md_lines.append(f"{q['num']}. {q['text']}\n")
        for text, correct in q['options']:
            mark = 'x' if correct else ' '
            md_lines.append(f"    - [{mark}] {text}")
        md_lines.append("")
        
    # Write to src
    src_path = src_dir / html_path.name
    src_path.write_text("\n".join(md_lines), encoding='utf-8')
    print(f"[green]Recovered {src_path}[/green]")

def main():
    docs_dir = pathlib.Path("docs/quizzes")
    src_dir = docs_dir / ".src"
    src_dir.mkdir(exist_ok=True)
    
    for f in docs_dir.glob("quiz-*.md"):
        recover_quiz(f, src_dir)

if __name__ == "__main__":
    main()
