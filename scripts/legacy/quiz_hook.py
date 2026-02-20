"""
Hook customizado para processar quizzes no markdown
Baseado no FastAPI do Zero
"""
import markdown
import ast


def format_quiz(source, *args, **kwargs):
    """
    Formata quizzes customizados em HTML
    
    Exemplo de uso no markdown:
    ```quiz
    {
        'questao': 'Qual é a saída do código?',
        'code': '```python\nprint("Hello")\n```',
        'opcoes': {
            'a': 'Hello',
            'b': 'hello',
            'c': 'HELLO'
        },
        'correta': 'a'
    }
    ```
    
    Args:
        source: Código do quiz em formato de dicionário Python
        
    Returns:
        HTML formatado do quiz
    """
    try:
        block = ast.literal_eval(source)
    except (ValueError, SyntaxError) as e:
        return f"<div class='quiz-error'>Erro ao processar quiz: {e}</div>"
    
    # Processar código se existir
    code = ""
    if 'code' in block and block['code']:
        code = markdown.markdown(
            block['code'],
            extensions=['pymdownx.superfences', 'pymdownx.highlight'],
        )
    
    # Gerar opções
    ops = []
    for chave, valor in block.get('opcoes', {}).items():
        input_id = f'{block.get("questao", "q")[:2]}-{chave}'
        
        if chave == block.get('correta'):
            ops.append(f'''
            <div>
            <input type="radio" name="answer" value="{valor}" id="{input_id}" correct="">
            <label for="{input_id}">{valor}</label>
            </div>
            ''')
        else:
            ops.append(f'''
            <div>
            <input type="radio" name="answer" value="{valor}" id="{input_id}">
            <label for="{input_id}">{valor}</label>
            </div>
            ''')
    
    return f'''
    <div class="quiz"><h3>{block.get("questao", "Questão")}</h3>
    {code}
    <form>
    <fieldset>
    {chr(10).join(ops)}
    </fieldset>
    <button type="submit" class="quiz-button">Enviar</button>
    </form>
    <section class="content hidden"></section>
    </div>
    '''


def on_page_markdown(markdown_text, *args, **kwargs):
    """
    Processa quizzes no markdown antes da conversão para HTML
    
    Args:
        markdown_text: Texto markdown da página
        
    Returns:
        Markdown processado com quizzes convertidos
    """
    if '```quiz' in markdown_text:
        md = markdown.markdown(
            markdown_text,
            extensions=['pymdownx.superfences', 'pymdownx.highlight'],
            extension_configs={
                'pymdownx.superfences': {
                    'custom_fences': [
                        {'name': 'quiz', 'class': 'quiz', 'format': format_quiz}
                    ]
                }
            },
        )
        return md
    return markdown_text


def on_page_content(html, *args, **kwargs):
    """
    Pós-processa o HTML da página
    Traduz botões e textos para português
    
    Args:
        html: HTML da página
        
    Returns:
        HTML processado
    """
    # Traduzir textos padrão
    html = html.replace('Submit', 'Enviar')
    html = html.replace('Check Answer', 'Verificar Resposta')
    
    return html
