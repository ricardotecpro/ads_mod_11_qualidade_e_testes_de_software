import os
from pathlib import Path

# --- Configuration ---
SYLLABUS = [
    # Módulo 1 – Fundamentos
    {"id": 1, "module": "Módulo 1 – Fundamentos", "title": "Introdução à Computação e Python"},
    {"id": 2, "module": "Módulo 1 – Fundamentos", "title": "Variáveis, Tipos de Dados e Operadores"},
    {"id": 3, "module": "Módulo 1 – Fundamentos", "title": "Entrada e Saída de Dados (I/O)"},
    
    # Módulo 2 – Estruturas de Controle e Dados
    {"id": 4, "module": "Módulo 2 – Estruturas de Dados", "title": "Estruturas Condicionais (if/elif/else)"},
    {"id": 5, "module": "Módulo 2 – Estruturas de Dados", "title": "Estruturas de Repetição (for/while)"},
    {"id": 6, "module": "Módulo 2 – Estruturas de Dados", "title": "Listas e Tuplas"},
    
    # Módulo 3 – Funções e Dicionários
    {"id": 7, "module": "Módulo 3 – Funções", "title": "Dicionários e Sets"},
    {"id": 8, "module": "Módulo 3 – Funções", "title": "Funções (Parte 1: Básico)"},
    {"id": 9, "module": "Módulo 3 – Funções", "title": "Funções (Parte 2: Parâmetros, Return, Escopo)"},
    
    # Módulo 4 – Arquivos e Exceções
    {"id": 10, "module": "Módulo 4 – Arquivos", "title": "Manipulação de Arquivos e JSON"},
    {"id": 11, "module": "Módulo 4 – Arquivos", "title": "Tratamento de Exceções e Debugging"},
    
    # Módulo 5 – POO
    {"id": 12, "module": "Módulo 5 – POO", "title": "Introdução a Classes e Objetos"},
    {"id": 13, "module": "Módulo 5 – POO", "title": "Herança e Polimorfismo"},
    
    # Módulo 6 – Ecossistema
    {"id": 14, "module": "Módulo 6 – Ecossistema", "title": "Bancos de Dados (SQLite) e APIs"},
    {"id": 15, "module": "Módulo 6 – Ecossistema", "title": "Projeto Final e Próximos Passos"},
]

DIRS = [
    "docs/slides",
    "docs/quizzes",
    "docs/exercicios",
    "docs/projetos",
    "docs/assets/images"
]

# --- Templates ---

TEMPLATE_AULA = """# {title}

## Objetivos da Aula
- [ ] Compreender ...
- [ ] Aplicar ...

## Conteúdo

### Introdução
O comando abaixo mostra como iniciar...

```python
print("Olá Mundo")
```

```termynal-exec
python app.py
Olá Mundo
```

!!! tip "Dica Importante"
    Este é um bloco de dica.

!!! failure "Erro Comum"
    Cuidado com indentation error!

## Em Prática
Vamos praticar o conceito aprendendo...

## Resumo
Nesta aula aprendemos sobre...

---
## 🎯 Próximos Passos

<div class="grid cards" markdown>

-   :material-presentation: **Acessar Slides**
    -   [Ver Slides da Aula](slides/{id:02d}-slides.md)

-   :material-school: **Quiz**
    -   [Responder Quiz](quizzes/quiz-{id:02d}.md)

-   :material-dumbbell: **Exercícios**
    -   [Lista de Exercícios](exercicios/exercicios-{id:02d}.md)

-   :material-rocket: **Projeto**
    -   [Mini Projeto](projetos/projeto-{id:02d}.md)

</div>
"""

TEMPLATE_SLIDE = """---
theme: material
---

# {title}
## Aula {id:02d}

---

## Objetivos
- Objetivo 1
- Objetivo 2

---

## Tópico 1
Conteúdo do tópico...

---

## Exemplo de Código

```python
def hello():
    print("Mundo")
```

---

## Resumo
- Ponto chave 1
- Ponto chave 2

---

<!-- _class: lead -->
# Próxima Aula: ...
"""

TEMPLATE_QUIZ = """# Quiz {id:02d}: {title}

**Teste seus conhecimentos.**

1. Qual a saída do código abaixo?
    ```python
    x = 10
    print(x * 2)
    ```
    - ( ) 10
    - (x) 20
    - ( ) 100

2. Python é uma linguagem compilada?
    - ( ) Verdadeiro
    - (x) Falso
"""

TEMPLATE_EXERCICIO = """# Exercícios Aula {id:02d}

## Nível: Fácil
1. Crie um programa que...

## Nível: Médio
2. Faça uma função que...

## Nível: Difícil
3. Implemente um algoritmo que...
"""

TEMPLATE_PROJETO = """# Projeto Aula {id:02d}

## Descrição
Desenvolva uma ferramenta que...

## Requisitos
- [ ] Usar variáveis
- [ ] Usar input

## Desafio
Tente adicionar uma funcionalidade extra de...
"""

TEMPLATE_INDEX = """# Bem-vindo ao Curso de Python Backend

## O Curso
Este curso foi desenhado para te levar do zero ao profissional.

## Estrutura
- 15 Módulos práticos
- Exercícios e Projetos a cada aula
- Slides e Quizzes interativos

<div class="grid cards" markdown>

-   :material-rocket: **Começar Agora**
    -   [Ir para Aula 01](aulas/aula-01.md)

</div>
"""

# --- Execution ---

def create_files():
    # 1. Ensure Directories
    for d in DIRS:
        Path(d).mkdir(parents=True, exist_ok=True)
    
    # 2. Create Index if missing
    if not Path("docs/index.md").exists():
        Path("docs/index.md").write_text(TEMPLATE_INDEX, encoding="utf-8")
        print("Created index.md")

    # 3. Generate Content
    for lesson in SYLLABUS:
        lid = lesson["id"]
        title = lesson["title"]
        
        # Paths
        p_aula = Path(f"docs/aulas/aula-{lid:02d}.md")
        p_slide = Path(f"docs/slides/slide-{lid:02d}.md")
        p_quiz = Path(f"docs/quizzes/quiz-{lid:02d}.md")
        p_exerc = Path(f"docs/exercicios/exercicio-{lid:02d}.md")
        p_proj = Path(f"docs/projetos/projeto-{lid:02d}.md")
        
        # Write Files
        if not p_aula.exists():
            p_aula.write_text(TEMPLATE_AULA.format(id=lid, title=title), encoding="utf-8")
        
        if not p_slide.exists():
            p_slide.write_text(TEMPLATE_SLIDE.format(id=lid, title=title), encoding="utf-8")
            
        if not p_quiz.exists():
            p_quiz.write_text(TEMPLATE_QUIZ.format(id=lid, title=title), encoding="utf-8")
            
        if not p_exerc.exists():
            p_exerc.write_text(TEMPLATE_EXERCICIO.format(id=lid, title=title), encoding="utf-8")
            
        if not p_proj.exists():
            p_proj.write_text(TEMPLATE_PROJETO.format(id=lid, title=title), encoding="utf-8")
            
        print(f"Generated Lesson {lid:02d}: {title}")

def generate_nav_yaml():
    nav = ["nav:", "  - Início: index.md"]
    
    nav.append("  - Aulas:")
    nav.append("      - aulas/index.md")
    
    current_module = None
    
    for lesson in SYLLABUS:
        module = lesson["module"]
        title = lesson["title"]
        lid = lesson["id"]
        filename = f"aulas/aula-{lid:02d}.md"
        
        if module != current_module:
            nav.append(f"      - {module}:")
            current_module = module
        
        nav.append(f"        - 'Aula {lid:02d} - {title}': {filename}")
    
    nav.append("  - Materiais:")
    nav.append("      - materiais.md")
    nav.append("      - Slides: slides/index.md")
    nav.append("      - Exercícios: exercicios/index.md")
    nav.append("      - Quizzes: quizzes/")
    nav.append("      - Projetos: projetos/")
    nav.append("      - Setups: setups/index.md")
    nav.append("  - Impressão: print_page.md")
    
    return "\n".join(nav)

def update_mkdocs():
    mkdocs_path = Path("mkdocs.yml")
    content = mkdocs_path.read_text(encoding="utf-8")
    
    # Remove existing 'nav:' if present (simplistic approach, assumes nav is at end or distinct)
    # We will append the new nav
    # Better: finding where nav starts
    
    if "nav:" in content:
        content = content.split("nav:")[0] # Truncate everything after nav:
    
    new_nav = generate_nav_yaml()
    
    final_content = content.strip() + "\n\n" + new_nav + "\n"
    mkdocs_path.write_text(final_content, encoding="utf-8")
    print("Updated mkdocs.yml navigation")

if __name__ == "__main__":
    create_files()
    update_mkdocs()
