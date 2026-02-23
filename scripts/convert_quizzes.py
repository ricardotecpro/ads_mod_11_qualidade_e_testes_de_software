"""
Script para converter automaticamente todos os quizzes de markdown para HTML interativo
"""
import pathlib
import re
from rich import print
from rich.progress import track


def parse_quiz_markdown(content: str) -> list:
    """
    Parse quiz markdown format e extrai perguntas
    
    Formato esperado:
    1. Pergunta aqui?
    
        - [ ] Opção incorreta
        - [x] Opção correta
        - [ ] Outra incorreta
    """
    questions = []
    
    # Regex para encontrar perguntas numeradas
    question_pattern = r'(\d+)\.\s+(.+?)(?=\n\n|\n\s*-|\Z)'
    
    # Encontrar todas as perguntas
    for match in re.finditer(question_pattern, content, re.DOTALL):
        question_num = match.group(1)
        question_text = match.group(2).strip()
        
        # Encontrar opções após esta pergunta
        # Procurar até a próxima pergunta ou fim do arquivo
        start_pos = match.end()
        next_question = re.search(r'\n\d+\.\s+', content[start_pos:])
        end_pos = start_pos + next_question.start() if next_question else len(content)
        
        options_text = content[start_pos:end_pos]
        
        # Parse opções
        options = []
        option_pattern = r'-\s+\[([ x])\]\s+(.+?)(?=\n\s*-|\n\n|\Z)'
        
        for opt_match in re.finditer(option_pattern, options_text, re.DOTALL):
            is_correct = opt_match.group(1) == 'x'
            option_text = opt_match.group(2).strip()
            options.append({
                'text': option_text,
                'correct': is_correct
            })
        
        if options:  # Só adiciona se encontrou opções
            questions.append({
                'number': question_num,
                'text': question_text,
                'options': options
            })
    
    return questions


def generate_quiz_html(quiz_number: int, questions: list) -> str:
    """Gera HTML completo do quiz"""
    
    # Cabeçalho
    html_parts = [
        f"# Quiz {quiz_number:02d} - Introdução\n",
        '\n--8<-- "assets/quiz.html"\n\n'
    ]
    
    # Gerar cada pergunta
    for q in questions:
        html_parts.append('<div class="quiz-container">\n')
        html_parts.append(f'  <div class="quiz-question">{q["number"]}. {q["text"]}</div>\n')
        
        for opt in q['options']:
            correct_attr = 'true' if opt['correct'] else 'false'
            feedback = f"✅ Correto! {opt['text']}" if opt['correct'] else f"Incorreto. Tente novamente."
            
            html_parts.append(
                f'  <div class="quiz-option" data-correct="{correct_attr}" '
                f'data-feedback="{feedback}">{opt["text"]}</div>\n'
            )
        
        html_parts.append('  <div class="quiz-feedback"></div>\n')
        html_parts.append('</div>\n\n')
    
    return ''.join(html_parts)


def convert_quiz(quiz_path: pathlib.Path) -> bool:
    """Converte um arquivo de quiz"""
    try:
        content = quiz_path.read_text(encoding='utf-8')
        
        # Parse perguntas
        questions = parse_quiz_markdown(content)
        
        if not questions:
            print(f"  [yellow]⚠[/yellow] Nenhuma pergunta encontrada em {quiz_path.name}")
            return False
        
        # Extrair número do quiz
        quiz_num = int(re.search(r'quiz-(\d+)', quiz_path.name).group(1))
        
        # Gerar HTML
        html_content = generate_quiz_html(quiz_num, questions)
        
        # Salvar em docs/quizzes (um nível acima de src)
        output_path = quiz_path.parent.parent / quiz_path.name
        output_path.write_text(html_content, encoding='utf-8')
        
        print(f"  [green]✓[/green] Converteu {quiz_path.name} -> {output_path} ({len(questions)} perguntas)")
        return True
        
    except Exception as e:
        print(f"  [red]✗[/red] Erro em {quiz_path.name}: {e}")
        return False


def convert_all_quizzes():
    """Converte todos os quizzes"""
    # Usar pasta .src como fonte
    quizzes_src_dir = pathlib.Path('docs/quizzes/src')
    
    if not quizzes_src_dir.exists():
        print("[yellow]⚠ Pasta docs/quizzes/src/ não encontrada. Criando...[/yellow]")
        quizzes_src_dir.mkdir(parents=True, exist_ok=True)
        print("[yellow]⚠ Por favor, coloque os arquivos markdown originais em docs/quizzes/src/[/yellow]")
        return
    
    print("\n[bold cyan]🧠 Convertendo Quizzes para HTML...[/bold cyan]")
    print(f"Fonte: {quizzes_src_dir}")
    
    quiz_files = sorted(quizzes_src_dir.glob('quiz-*.md'))
    
    if not quiz_files:
        print("[yellow]⚠ Nenhum arquivo de quiz encontrado em docs/quizzes/src/[/yellow]")
        return
    
    converted = 0
    for quiz_path in track(quiz_files, description="Processando quizzes..."):
        if convert_quiz(quiz_path):
            converted += 1
    
    print(f"\n[green]✓ {converted}/{len(quiz_files)} quizzes convertidos com sucesso![/green]")


def main():
    """Função principal"""
    print("[bold]🚀 Conversão Automática de Quizzes[/bold]")
    print("=" * 50)
    
    convert_all_quizzes()
    
    print("\n[green]✅ Conversão concluída![/green]")
    print("\n[cyan]💡 Dica:[/cyan] Teste os quizzes em http://localhost:8000/quizzes/")


if __name__ == '__main__':
    main()
