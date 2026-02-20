"""
Script para corrigir links de slides em todas as aulas
Muda de .md para .html
"""
import pathlib
import re
from rich import print


def fix_slide_links():
    """Corrige links de slides em todos os arquivos de aula"""
    docs_dir = pathlib.Path('docs')
    
    # Encontrar todos os arquivos de aula (01.md até 16.md)
    lesson_files = []
    for i in range(1, 17):
        lesson_file = docs_dir / f"{i:02d}.md"
        if lesson_file.exists():
            lesson_files.append(lesson_file)
    
    print(f"\n[bold cyan]🔧 Corrigindo links de slides...[/bold cyan]")
    print(f"Encontrados {len(lesson_files)} arquivos de aula\n")
    
    fixed_count = 0
    for lesson_file in lesson_files:
        content = lesson_file.read_text(encoding='utf-8')
        original_content = content
        
        # Substituir links de slides .md por .html
        # Padrão: (slides/XX-slides.md) -> (slides/XX-slides.html)
        content = re.sub(
            r'\(slides/(\d{2})-slides\.md\)',
            r'(slides/\1-slides.html)',
            content
        )
        
        if content != original_content:
            lesson_file.write_text(content, encoding='utf-8')
            print(f"  [green]✓[/green] Corrigido {lesson_file.name}")
            fixed_count += 1
        else:
            print(f"  [yellow]•[/yellow] {lesson_file.name} (sem alterações)")
    
    print(f"\n[green]✅ {fixed_count} arquivo(s) corrigido(s)![/green]")


if __name__ == '__main__':
    fix_slide_links()
