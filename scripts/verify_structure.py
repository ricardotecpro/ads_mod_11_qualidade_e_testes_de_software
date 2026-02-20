import os
import re

def verify_structure(base_path):
    print(f"Verifying structure in {base_path}...")
    required_sections = [
        r"^## 🎯 Objetivos de Aprendizagem",
        r"^## 📚 Conteúdo",
        r"^## 📽 Roteiro de Slides",
        r"^## 📝 Quiz",
        r"^## Gabarito",
        r"^## 🛠 Exercícios",
        r"^## 🚀 Projeto da Aula"
    ]
    
    errors = []
    
    for i in range(1, 17):
        filename = f"aula-{i:02d}.md"
        filepath = os.path.join(base_path, "docs", "aulas", filename)
        
        if not os.path.exists(filepath):
            errors.append(f"MISSING FILE: {filename}")
            continue
            
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
            
        missing_in_file = []
        for section_regex in required_sections:
            if not re.search(section_regex, content, re.MULTILINE):
                missing_in_file.append(section_regex.replace("^## ", "").replace(r" ", " "))
        
        if missing_in_file:
            errors.append(f"{filename} is missing sections: {', '.join(missing_in_file)}")

    if errors:
        print("\n❌ STRUCTURE ERRORS FOUND:")
        for e in errors:
            print(f"  - {e}")
        return False
    else:
        print("\n✅ All 16 lesson files have valid structure.")
        return True

if __name__ == "__main__":
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    verify_structure(base)
