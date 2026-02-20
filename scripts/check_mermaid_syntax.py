"""
Script para testar diagramas Mermaid individualmente e encontrar erros
"""
import pathlib
import re
import subprocess
from rich import print
from rich.progress import track


def extract_mermaid_blocks_with_location(file_path: pathlib.Path) -> list:
    """Extrai blocos mermaid com informação de localização"""
    content = file_path.read_text(encoding='utf-8')
    
    # Padrão para encontrar blocos mermaid
    pattern = r'```mermaid\n(.*?)```'
    blocks = []
    
    for match in re.finditer(pattern, content, re.DOTALL):
        block_content = match.group(1)
        start_pos = match.start()
        
        # Contar linha
        line_num = content[:start_pos].count('\n') + 1
        
        blocks.append({
            'content': block_content,
            'line': line_num,
            'file': str(file_path)
        })
    
    return blocks


def test_mermaid_syntax(block_content: str) -> dict:
    """Testa sintaxe de um bloco Mermaid"""
    issues = []
    
    lines = block_content.strip().split('\n')
    if not lines:
        return {'valid': False, 'issues': ['Empty diagram']}
    
    first_line = lines[0].strip()
    
    # Tipos válidos de diagrama
    valid_types = [
        'graph', 'flowchart', 'sequenceDiagram', 'classDiagram',
        'stateDiagram', 'erDiagram', 'gantt', 'pie', 'mindmap',
        'timeline', 'gitGraph', 'journey', 'quadrantChart'
    ]
    
    # Verificar tipo
    diagram_type = None
    for vtype in valid_types:
        if first_line.startswith(vtype):
            diagram_type = vtype
            break
    
    if not diagram_type:
        issues.append(f"Unknown diagram type: '{first_line}'")
        return {'valid': False, 'issues': issues}
    
    # Verificações específicas por tipo
    if diagram_type in ['graph', 'flowchart']:
        # Verificar direção
        if diagram_type == 'graph':
            valid_directions = ['TD', 'TB', 'BT', 'RL', 'LR']
            parts = first_line.split()
            if len(parts) < 2:
                issues.append("Missing direction (TD, LR, etc.)")
            elif parts[1] not in valid_directions:
                issues.append(f"Invalid direction: '{parts[1]}'")
        
        # Verificar sintaxe de nós e setas
        for i, line in enumerate(lines[1:], 2):
            line = line.strip()
            if not line or line.startswith('%%'):
                continue
            
            # Verificar parênteses balanceados
            if line.count('[') != line.count(']'):
                issues.append(f"Line {i}: Unbalanced brackets")
            if line.count('(') != line.count(')'):
                issues.append(f"Line {i}: Unbalanced parentheses")
            if line.count('{') != line.count('}'):
                issues.append(f"Line {i}: Unbalanced braces")
    
    elif diagram_type == 'mindmap':
        # Mindmap precisa de indentação correta
        if len(lines) < 2:
            issues.append("Mindmap needs content")
    
    if issues:
        return {'valid': False, 'issues': issues}
    
    return {'valid': True}


def main():
    """Função principal"""
    print("\n[bold cyan]🔍 Testando Diagramas Mermaid...[/bold cyan]\n")
    
    # Encontrar arquivos das aulas
    docs_dir = pathlib.Path('docs')
    lesson_files = [docs_dir / f"{i:02d}.md" for i in range(1, 17)]
    lesson_files = [f for f in lesson_files if f.exists()]
    
    print(f"Testando {len(lesson_files)} arquivos de aula\n")
    
    all_blocks = []
    for lesson_file in lesson_files:
        blocks = extract_mermaid_blocks_with_location(lesson_file)
        all_blocks.extend(blocks)
    
    print(f"Total de blocos Mermaid encontrados: {len(all_blocks)}\n")
    
    # Testar cada bloco
    problematic = []
    for block in track(all_blocks, description="Testando blocos..."):
        result = test_mermaid_syntax(block['content'])
        if not result['valid']:
            problematic.append({
                **block,
                'issues': result['issues']
            })
    
    # Relatório
    print(f"\n[bold]📊 Resultados:[/bold]")
    print(f"Blocos testados: {len(all_blocks)}")
    print(f"Blocos com problemas: {len(problematic)}\n")
    
    if problematic:
        print("[bold red]❌ Blocos Problemáticos:[/bold red]\n")
        for item in problematic:
            print(f"[yellow]📄 {item['file']}:{item['line']}[/yellow]")
            for issue in item['issues']:
                print(f"  [red]• {issue}[/red]")
            print(f"  [dim]Preview: {item['content'][:100]}...[/dim]\n")
    else:
        print("[green]✅ Todos os blocos parecem válidos![/green]")
        print("\n[yellow]Nota: Erros podem ser de versão do Mermaid ou sintaxe avançada.[/yellow]")


if __name__ == '__main__':
    main()
