"""
Invoke tasks para automação avançada do projeto
"""
from pathlib import Path
from invoke import task
from rich.console import Console

console = Console()


@task
def clean(c):
    """Limpa arquivos gerados (site/, slides/html/)"""
    console.print("[yellow]🧹 Limpando arquivos gerados...[/yellow]")
    
    # Limpar site
    if Path("site").exists():
        c.run("rm -rf site/", warn=True)
        console.print("[green]  ✓ site/ removido[/green]")
    
    # Limpar slides HTML
    if Path("slides/html").exists():
        c.run("rm -rf slides/html/", warn=True)
        console.print("[green]  ✓ slides/html/ removido[/green]")
    
    console.print("[green]✨ Limpeza concluída![/green]")


@task
def build_all(c):
    """Build completo: slides + site"""
    console.print("[blue]🚀 Iniciando build completo...[/blue]")
    
    # Gerar slides
    console.print("[cyan]📊 Gerando slides HTML...[/cyan]")
    result = c.run("poetry run task slides", warn=True)
    if result and result.ok:
        console.print("[green]  ✓ Slides gerados[/green]")
    else:
        console.print("[yellow]  ⚠ Erro ao gerar slides[/yellow]")

    # Gerar quizzes
    console.print("[cyan]📝 Gerando quizzes interativos...[/cyan]")
    result_quiz = c.run("poetry run task quizzes", warn=True)
    if result_quiz and result_quiz.ok:
        console.print("[green]  ✓ Quizzes gerados[/green]")
    else:
        console.print("[yellow]  ⚠ Erro ao gerar quizzes[/yellow]")
    
    # Build site
    console.print("[cyan]🏗️  Building site com MkDocs...[/cyan]")
    c.run("poetry run task build")
    console.print("[green]  ✓ Site gerado[/green]")
    
    console.print("[green]✅ Build completo finalizado![/green]")


@task
def serve_all(c):
    """Serve site localmente"""
    console.print("[blue]🌐 Iniciando servidor local...[/blue]")
    console.print("[cyan]📍 Acesse: http://localhost:8000[/cyan]")
    c.run("poetry run task serve", pty=True)


@task
def test_links(c):
    """Testa todos os links do site"""
    console.print("[blue]🔍 Testando links...[/blue]")
    
    if not Path("tests/test_links.py").exists():
        console.print("[yellow]⚠ Arquivo de testes não encontrado[/yellow]")
        console.print("[cyan]💡 Crie tests/test_links.py para testar links[/cyan]")
        return
    
    c.run("poetry run pytest tests/test_links.py -v")
    console.print("[green]✅ Testes de links concluídos[/green]")


@task
def update_deps(c):
    """Atualiza todas as dependências do Poetry"""
    console.print("[yellow]📦 Atualizando dependências...[/yellow]")
    c.run("poetry update")
    console.print("[green]✅ Dependências atualizadas[/green]")


@task
def install(c):
    """Instala todas as dependências"""
    console.print("[blue]📦 Instalando dependências com Poetry...[/blue]")
    c.run("poetry install")
    console.print("[green]✅ Dependências instaladas[/green]")


@task
def lint(c):
    """Executa linting do código Python"""
    console.print("[blue]🔍 Executando linting...[/blue]")
    
    # Verificar se ruff está instalado
    result = c.run("poetry run ruff --version", warn=True)
    if not result or not result.ok:
        console.print("[yellow]⚠ Ruff não instalado, pulando linting[/yellow]")
        return
    
    c.run("poetry run ruff check .")
    console.print("[green]✅ Linting concluído[/green]")


@task
def check_content(c):
    """Verifica a integridade do conteúdo (aulas, slides, quizzes)"""
    console.print("[blue]🔍 Verificando conteúdo...[/blue]")
    c.run("poetry run task check")



@task
def format_code(c):
    """Formata código Python com ruff"""
    console.print("[blue]✨ Formatando código...[/blue]")
    
    result = c.run("poetry run ruff --version", warn=True)
    if not result or not result.ok:
        console.print("[yellow]⚠ Ruff não instalado, pulando formatação[/yellow]")
        return
    
    c.run("poetry run ruff format .")
    console.print("[green]✅ Código formatado[/green]")


@task
def deploy(c):
    """Deploy para produção com Mike"""
    console.print("[blue]🚀 Fazendo deploy para produção...[/blue]")
    c.run("poetry run task deploy")
    console.print("[green]✅ Deploy concluído[/green]")


@task
def help_tasks(c):
    """Mostra todos os comandos disponíveis"""
    console.print("\n[bold cyan]📋 Comandos Disponíveis:[/bold cyan]\n")
    
    tasks_list = [
        ("invoke clean", "Limpa arquivos gerados"),
        ("invoke build-all", "Build completo (slides + site)"),
        ("invoke serve-all", "Servidor local"),
        ("invoke test-links", "Testa links"),
        ("invoke update-deps", "Atualiza dependências"),
        ("invoke install", "Instala dependências"),
        ("invoke lint", "Linting do código"),
        ("invoke format-code", "Formata código"),
        ("invoke deploy", "Deploy produção"),
        ("", ""),
        ("poetry run task serve", "Servidor MkDocs"),
        ("poetry run task build", "Build site"),
        ("poetry run task slides", "Gera slides"),
        ("poetry run task test", "Executa testes"),
    ]
    
    for cmd, desc in tasks_list:
        if cmd:
            console.print(f"  [green]{cmd:25}[/green] - {desc}")
        else:
            console.print("")
