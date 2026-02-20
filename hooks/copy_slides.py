"""
Hook para copiar slides HTML gerados para o site após build
"""
import shutil
import pathlib
from rich import print


def copy_slides(config, **kwargs):
    """
    Copia slides HTML e Markdown do diretório docs/slides/ para site/slides/
    após o build do MkDocs
    
    Args:
        config: Configuração do MkDocs
        **kwargs: Argumentos adicionais
    """
    site_dir = config['site_dir']
    slides_dest = pathlib.Path(site_dir) / 'slides'
    slides_dest.mkdir(exist_ok=True)
    
    # Diretório fonte dos slides
    slides_source = pathlib.Path('docs/slides')
    if not slides_source.exists():
        print("[yellow]⚠ Pasta docs/slides/ não encontrada[/yellow]")
        return
    
    # Copiar todos os slides HTML e Markdown
    html_copied = 0
    md_copied = 0
    
    # Copiar HTML
    print("[cyan]Copiando slides HTML...[/cyan]")
    for slide in slides_source.glob('slide-*.html'):
        dest_file = slides_dest / slide.name
        shutil.copy(slide.resolve(), dest_file.resolve())
        print(f"  [blue]→ {slide.name}[/blue]")
        html_copied += 1
    
    # Copiar Markdown
    print("[cyan]Copiando slides Markdown...[/cyan]")
    for slide in slides_source.glob('slide-*.md'):  # CORRIGIDO: era *-slides.md
        dest_file = slides_dest / slide.name
        shutil.copy(slide.resolve(), dest_file.resolve())
        print(f"  [blue]→ {slide.name}[/blue]")
        md_copied += 1
    
    if html_copied > 0:
        print(f"[green]✓ {html_copied} slide(s) HTML copiados[/green]")
    if md_copied > 0:
        print(f"[green]✓ {md_copied} slide(s) Markdown copiados[/green]")
    
    if html_copied == 0 and md_copied == 0:
        print("[yellow]⚠ Nenhum slide encontrado em docs/slides/[/yellow]")


def on_post_build(config):
    """Hook chamado após o build do MkDocs"""
    copy_slides(config)
