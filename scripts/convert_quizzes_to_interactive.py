import re
import os

def convert_quizzes(base_path):
    print(f"Converting quizzes in {base_path}...")
    quizzes_dir = os.path.join(base_path, "docs", "quizzes")
    
    for i in range(1, 17):
        filename = f"quiz-{i:02d}.md"
        filepath = os.path.join(quizzes_dir, filename)
        
        if not os.path.exists(filepath):
            print(f"Skipping {filename} (not found)")
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Parse content
        # 1. Extract questions
        # Pattern: N. **Question** ... Options ...
        
        # Split by Gabarito to separate questions from answers
        parts = content.split("## Gabarito")
        questions_part = parts[0]
        answers_part = parts[1] if len(parts) > 1 else ""
        
        # Parse answers
        correct_answers = {}
        for line in answers_part.splitlines():
            match = re.search(r"(\d+):\s*([A-D])", line)
            if match:
                correct_answers[int(match.group(1))] = match.group(2)
        
        # Parse questions
        questions = []
        # Split by number. **
        question_blocks = re.split(r'\n\d+\.\s*\*\*', questions_part)
        
        for block in question_blocks[1:]: # Skip preamble
            # The split removes the number and marker, so we just have the question text and options
            # Extract question text (until next new line or list)
            lines = block.strip().split('\n')
            question_text = lines[0].strip('*') # Remove trailing ** if present
            
            options = []
            for line in lines[1:]:
                line = line.strip()
                match = re.match(r"-\s*([A-D])\)\s*(.*)", line)
                if match:
                    options.append({
                        "letter": match.group(1),
                        "text": match.group(2)
                    })
            
            if question_text and options:
                questions.append({
                    "text": question_text,
                    "options": options
                })

        # Generate HTML
        html_content = f"""# Quiz {i:02d}

<link rel="stylesheet" href="../../assets/css/quiz.css">
<script src="../../assets/js/quiz.js" defer></script>

<div class="quiz-container">
"""
        
        for idx, q in enumerate(questions, 1):
            html_content += f"""  <div class="quiz-item" id="q{idx}">
    <div class="quiz-question">{idx}. {q['text']}</div>
    <div class="quiz-options">
"""
            correct_letter = correct_answers.get(idx, "A") # Default to A if not found (shouldn't happen)
            
            for opt in q['options']:
                is_correct = "true" if opt['letter'] == correct_letter else "false"
                feedback = "Correto!" if is_correct == "true" else "Incorreto."
                html_content += f"""      <div class="quiz-option" data-correct="{is_correct}" data-feedback="{feedback}">
        <span class="option-letter">{opt['letter']})</span> {opt['text']}
      </div>
"""
            html_content += """    </div>
    <div class="quiz-feedback"></div>
  </div>
"""

        html_content += "</div>\n"
        
        # Write back to file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(html_content)
            print(f"Converted {filename}")

if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    convert_quizzes(base)
