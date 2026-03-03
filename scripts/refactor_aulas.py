import os
import re
import json

AULAS_DIR = r"d:\SourceCode\REPOS\github.io\adm_gestao_tiaa\docs\aulas"

def load_intermediate_content():
    """Carrega conteúdo educativo variável do content_overlay.json externo"""
    json_path = os.path.join(os.path.dirname(__file__), "content_overlay.json")
    if os.path.exists(json_path):
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

intermediate_content = load_intermediate_content()

for i in range(1, 17):
    num_str = f"{i:02d}"
    file_path = os.path.join(AULAS_DIR, f"aula-{num_str}.md")
    if not os.path.exists(file_path):
        print(f"Skipping {file_path}")
        continue
    
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Re-numerar seções para inserir conteúdo intermediário
    content = content.replace("## 7. Exercício", "## 8. Exercício")
    content = content.replace("## 6. Mini-Projeto", "## 7. Mini-Projeto")
    
    # Inserir conteúdo educativo específico do TI Administrativa
    intro = intermediate_content.get(num_str, "")
    
    if intro:
        content = content.replace("## 6. Conclusão", f"{intro}\n## 6. Conclusão")
    
    print(f"Processing {file_path}")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)

print("✅ Refatoração das aulas concluída com content_overlay.json!")