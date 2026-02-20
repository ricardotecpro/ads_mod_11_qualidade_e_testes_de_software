"""
Script para validar todos os diagramas Mermaid no projeto
"""
import pathlib
import re
from rich import print
from rich.progress import track


def extract_mermaid_blocks(content: str) -> list:
    """Extrai todos os blocos mermaid de um arquivo"""
    pattern = r'```mermaid\n(.*?)```'
    matches = re.findall(pattern, content, re.DOTALL)
    return matches


def validate_mermaid_file(file_path: pathlib.Path) -> dict:
    """Valida diagramas Mermaid em um arquivo"""
    try:
        content = file_path.read_text(encoding='utf-8')
        blocks = extract_mermaid_blocks(content)
        
        if not blocks:
            return None
        
        issues = []
        for i, block in enumerate(blocks, 1):
            # Verificar sintaxe básica
            lines = block.strip().split('\n')
            if not lines:
                issues.append(f"Block {i}: Empty diagram")
                continue
            
            first_line = lines[0].strip()
            
            # Verificar tipo de diagrama válido
            valid_types = ['graph', 'flowchart', 'sequenceDiagram', 'classDiagram', 
                          'stateDiagram', 'erDiagram', 'gantt', 'pie', 'mindmap',
                          'timeline', 'gitGraph', 'journey']
            
            if not any(first_line.startswith(t) for t in valid_types):
                issues.append(f"Block {i}: Invalid diagram type '{first_line}'")
            
            # Verificar se tem conteúdo
            if len(lines) < 2:
                issues.append(f"Block {i}: No content after diagram type")
        
        if issues:
            return {
                'file': str(file_path),
                'blocks': len(blocks),
                'issues': issues
            }
        
        return None
        
    except Exception as e:
        return {
            'file': str(file_path),
            'error': str(e)
        }


def main():
    """Função principal"""
    print("\n[bold cyan]🔍 Validando Diagramas Mermaid...[/bold cyan]\n")
    
    # Encontrar todos os arquivos markdown
    docs_dir = pathlib.Path('docs')
    md_files = list(docs_dir.rglob('*.md'))
    
    print(f"Encontrados {len(md_files)} arquivos markdown\n")
    
    # Validar cada arquivo
    problematic_files = []
    total_blocks = 0
    
    for md_file in track(md_files, description="Validando arquivos..."):
        result = validate_mermaid_file(md_file)
        if result:
            problematic_files.append(result)
            if 'blocks' in result:
                total_blocks += result['blocks']
    
    # Relatório
    print(f"\n[bold]📊 Resultados:[/bold]")
    print(f"Total de blocos Mermaid: {total_blocks}")
    print(f"Arquivos com problemas: {len(problematic_files)}\n")
    
    if problematic_files:
        print("[bold red]❌ Arquivos com Problemas:[/bold red]\n")
        for item in problematic_files:
            print(f"[yellow]📄 {item['file']}[/yellow]")
            if 'error' in item:
                print(f"  [red]Erro: {item['error']}[/red]")
            elif 'issues' in item:
                for issue in item['issues']:
                    print(f"  [red]• {issue}[/red]")
            print()
    else:
        print("[green]✅ Nenhum problema encontrado![/green]")


if __name__ == '__main__':
    main()
