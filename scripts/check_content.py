"""
Script de auditoria de conteúdo do curso
Verifica a existência e estrutura de:
- Conteúdo das aulas (Markdown)
- Slides (RevealJS)
- Quizzes
- Projetos e Testes
"""
import glob
import re
import os
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich import print

console = Console()

def check_lesson_content(lesson_path: Path) -> dict:
    """Verifica o conteúdo de uma aula específica"""
    content = lesson_path.read_text(encoding='utf-8')
    
    # Extrair número da aula do nome do arquivo (ex: 01.md -> 1)
    try:
        lesson_num = int(lesson_path.stem)
        lesson_str = f"{lesson_num:02d}"
    except ValueError:
        return None

    # Caminhos esperados
    slide_path = Path(f"docs/slides/{lesson_str}-slides.md")
    quiz_path = Path(f"docs/quizzes/quiz-{lesson_str}.md")
    exercise_path = Path(f"docs/exercicios/exercicios-{lesson_str}.md")
    project_path = Path(f"docs/projetos/projeto-{lesson_str}.md")
    
    report = {
        "lesson": lesson_str,
        "path": lesson_path,
        "mermaid_count": content.count('```mermaid'),
        "slides_exists": slide_path.exists(),
        "slides_revealjs": False,
        "quiz_exists": quiz_path.exists(),
        "quiz_questions": 0,
        "project_exists": project_path.exists(),
        "project_has_tests": False,
        "project_has_pytest": False
    }

    # Verificar Slides
    if report["slides_exists"]:
        slide_content = slide_path.read_text(encoding='utf-8')
        # Verifica se tem 'layout: revealjs' no frontmatter OU se é usado pelo gerador
        # O gerador novo usa um template HTML, então a presença do arquivo MD na pasta correta já é um bom sinal
        # Mas vamos verificar se tem conteúdo
        if len(slide_content) > 100: 
             report["slides_revealjs"] = True

    # Verificar Quiz
    if report["quiz_exists"]:
        quiz_content = quiz_path.read_text(encoding='utf-8')
        # Conta questões (busca por div com classe quiz-question)
        questions = re.findall(r'class="quiz-question"', quiz_content)
        report["quiz_questions"] = len(questions)

    # Verificar Projeto
    if report["project_exists"]:
        project_content = project_path.read_text(encoding='utf-8')
        lower_content = project_content.lower()
        if "test" in lower_content or "teste" in lower_content:
            report["project_has_tests"] = True
        if "pytest" in lower_content:
            report["project_has_pytest"] = True

    return report

def main():
    console.print("\n[bold blue]🔍 Iniciando Auditoria de Conteúdo...[/bold blue]\n")
    
    # Encontrar todas as aulas em docs/*.md (assumindo que são arquivos numéricos 01.md, 02.md etc)
    lesson_files = sorted(glob.glob("docs/[0-9][0-9].md"))
    
    if not lesson_files:
        console.print("[red]❌ Nenhuma aula encontrada em docs/![/red]")
        return

    # Tabela de Resultados
    table = Table(title="Status do Conteúdo do Curso")
    table.add_column("Aula", style="cyan", justify="center")
    table.add_column("Mermaid", justify="center")
    table.add_column("Slides", justify="center")
    table.add_column("Quiz (Qtd)", justify="center")
    table.add_column("Projeto", justify="center")
    table.add_column("Testes", justify="center")

    issues = []
    
    for lesson_file in lesson_files:
        path = Path(lesson_file)
        r = check_lesson_content(path)
        if not r:
            continue
            
        # Formatação dos status
        mermaid_icon = "✅" if r["mermaid_count"] > 0 else "[dim]-[/dim]"
        
        slide_icon = "✅" if r["slides_revealjs"] else "❌"
        if not r["slides_exists"]: slide_icon = "[red]Ausente[/red]"
        
        quiz_val = r["quiz_questions"]
        if r["quiz_exists"]:
            quiz_icon = f"✅ ({quiz_val})" if quiz_val >= 5 else f"⚠ ({quiz_val})"
        else:
            quiz_icon = "[red]Ausente[/red]"

        proj_icon = "✅" if r["project_exists"] else "[dim]-[/dim]"
        
        test_status = "[dim]-[/dim]"
        if r["project_exists"]:
            if r["project_has_tests"]:
                test_status = "✅"
            else:
                test_status = "❌"

        table.add_row(
            r["lesson"],
            f"{mermaid_icon} {r['mermaid_count'] if r['mermaid_count'] > 0 else ''}",
            slide_icon,
            quiz_icon,
            proj_icon,
            test_status
        )

        # Coletar Issues
        lesson_num = int(r["lesson"])
        
        if r["mermaid_count"] == 0:
            # Talvez nem todas as aulas precisem, mas vamos logar como info
            pass 
            
        if not r["slides_revealjs"]:
            issues.append(f"Aula {r['lesson']}: Check slides (missing or empty)")
            
        if r["quiz_exists"] and r["quiz_questions"] < 5:
            issues.append(f"Aula {r['lesson']}: Quiz has few questions ({r['quiz_questions']})")
        
        if not r["quiz_exists"]:
             issues.append(f"Aula {r['lesson']}: Quiz missing")

        # Regras específicas de negócio (ex: projetos a partir da aula 9)
        if lesson_num >= 9 and not r["project_has_tests"]:
            issues.append(f"Aula {r['lesson']}: Project missing tests")

    console.print(table)

    if issues:
        console.print("\n[bold yellow]⚠ Problemas Encontrados:[/bold yellow]")
        for issue in issues:
            console.print(f"  - {issue}")
    else:
        console.print("\n[bold green]✨ Todo o conteúdo verificado está ok![/bold green]")

if __name__ == "__main__":
    main()
