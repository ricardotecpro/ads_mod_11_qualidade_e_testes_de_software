import pathlib
import re
import sys
import io
import yaml

# Fix for Windows encoding issues with emojis
if sys.platform == "win32":
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding="utf-8")

from rich import print
from rich.progress import track

def load_config():
    """Carrega configuração do mkdocs.yml"""
    with open("mkdocs.yml", "r", encoding="utf-8") as f:
        # Usamos UnsafeLoader pois mkdocs.yml pode conter tags !!python/name
        return yaml.load(f, Loader=yaml.UnsafeLoader)

CONFIG = load_config()
SITE_NAME = CONFIG.get("site_name", "Curso")

def generate_slide_html(slide_id: str) -> str:
    """Gera HTML para um slide específico"""
    return f'''<!doctype html>
<html lang="pt-BR">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{slide_id.upper()} - {SITE_NAME}</title>
    
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/reset.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/reveal.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/dist/theme/black.css">
    <link rel="stylesheet" href="https://unpkg.com/reveal.js@4.5.0/plugin/highlight/monokai.css">
</head>
<body>
    <div class="reveal">
        <div class="slides">
            <section data-markdown="src/{slide_id}.md"
                     data-separator="^\\n---\\n$"
                     data-separator-vertical="^\\n--\\n$">
            </section>
        </div>
    </div>
    
    <style>
        /* Modern Reveal.js tweaks */
        .reveal .slides section {{ padding: 20px; text-align: left; }}
        .reveal .slides h1, .reveal .slides h2, .reveal .slides h3 {{ text-align: center; }}
        
        /* Admonitions Simulation */
        .admonition {{
            margin: 1em 0;
            padding: 0.6em 1em;
            border-left: 0.4em solid #448aff;
            background-color: rgba(68, 138, 255, 0.1);
            font-size: 0.8em;
        }}
        .admonition-title {{
            font-weight: bold;
            margin-bottom: 0.5em;
        }}
        .admonition.info {{ border-left-color: #00b0ff; background-color: rgba(0, 176, 255, 0.1); }}
        .admonition.warning {{ border-left-color: #ff9100; background-color: rgba(255, 145, 0, 0.1); }}
        .admonition.success {{ border-left-color: #00e676; background-color: rgba(0, 230, 118, 0.1); }}
        
        /* Grid Cards Simulation */
        .grid-cards-pro {{ display: flex; gap: 10px; flex-wrap: wrap; }}
        .card {{ 
            flex: 1; min-width: 200px; padding: 15px; 
            border: 1px solid #444; border-radius: 8px; background: #222; 
        }}
    </style>

    <script src="https://unpkg.com/reveal.js@4.5.0/dist/reveal.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/markdown/markdown.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/highlight/highlight.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/notes/notes.js"></script>
    <script src="https://unpkg.com/reveal.js@4.5.0/plugin/math/math.js"></script>
    <script src="https://unpkg.com/mermaid@11.12.3/dist/mermaid.min.js"></script>
    <script>
        Reveal.initialize({{
            hash: true,
            slideNumber: 'c/t',
            showSlideNumber: 'all',
            controls: true,
            progress: true,
            transition: 'slide',
            center: false,
            plugins: [ RevealMarkdown, RevealHighlight, RevealNotes, RevealMath.MathJax3 ],
            mathjax3: {{
                mathjax: 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js',
                tex: {{
                    inlineMath: [ [ '$', '$' ], [ '\\(', '\\)' ] ]
                }}
            }}
        }}).then(() => {{
            // Inicialização Pós-Load
            initializePlugins();
        }});

        Reveal.on('slidechanged', event => {{ initializePlugins(); }});

        function initializePlugins() {{
            // Mermaid
            if (window.mermaid) {{
                document.querySelectorAll('.mermaid, pre code.language-mermaid').forEach(el => {{
                    if (el.getAttribute('data-processed')) return;
                    
                    // Se for um bloco de código, extraímos o texto
                    const code = el.tagName === 'CODE' ? el.textContent : el.innerText;
                    const div = document.createElement('div');
                    div.className = 'mermaid';
                    div.textContent = code;
                    el.closest('pre')?.replaceWith(div) || el.replaceWith(div);
                }});
                mermaid.initialize({{ startOnLoad: false, theme: 'dark' }});
                mermaid.run({{ querySelector: '.mermaid' }});
            }}
            // MathJax
            if (window.MathJax) {{
                MathJax.typesetPromise();
            }}
            // Termynal
            if (window.Termynal) {{
                document.querySelectorAll('[data-termynal]').forEach(el => {{
                    if (!el.getAttribute('data-termynal-initialized')) {{
                        new Termynal(el);
                        el.setAttribute('data-termynal-initialized', 'true');
                    }}
                }});
            }}
        }}
    </script>
</body>
</html>
'''


def convert_quiz_md_to_html(md_content: str) -> str:
    """Converte o formato MarkDown de quiz para o formato HTML interativo"""
    # Regex para capturar Perguntas, Opções e Explicações
    # 1. Título
    title_match = re.search(r'# (.*)', md_content)
    title = title_match.group(1) if title_match else "Quiz"
    
    html_output = [f"# {title}\n", '--8<-- "assets/quiz.html"\n']
    
    # Split by questions
    questions = re.split(r'\n\d+\. ', md_content)
    if not questions[0].strip().startswith('1.'):
        # The first element might be the title, discard it if it doesn't have a question
        questions = questions[1:]
    else:
        # If it starts with 1., the first split will have it
        questions[0] = questions[0].replace('1. ', '', 1)

    for i, q_block in enumerate(questions, 1):
        lines = q_block.strip().split('\n')
        if not lines: continue
        
        question_text = lines[0].strip()
        options = []
        explanation = ""
        
        for line in lines[1:]:
            line = line.strip()
            if line.startswith('- ['):
                is_correct = 'x' in line.lower()[:5]
                option_text = line[line.find(']')+1:].strip()
                options.append((option_text, is_correct))
            elif line.startswith('*Explicação:'):
                explanation = line.replace('*Explicação:', '').strip('*').strip()
        
        # Build HTML
        html_output.append('<div class="quiz-container">')
        html_output.append(f'  <div class="quiz-question">{i}. {question_text}</div>')
        
        for opt_text, is_correct in options:
            correct_attr = "true" if is_correct else "false"
            feedback = f"✅ Correto! {explanation}" if is_correct else f"❌ Incorreto. {explanation}"
            html_output.append(f'  <div class="quiz-option" data-correct="{correct_attr}" data-feedback="{feedback}">{opt_text}</div>')
        
        html_output.append('  <div class="quiz-feedback"></div>')
        html_output.append('</div>\n')
        
    return "\n".join(html_output)


def generate_all_slides():
    """Gera arquivos HTML wrapper externos para todos os 16 slides"""
    slides_dst_dir = pathlib.Path('docs/slides')
    
    if not slides_dst_dir.exists():
        print("[yellow]WARNING: Pasta docs/slides/ não encontrada.[/yellow]")
        return
    
    print("\n[bold cyan]PROCESSO: Gerando Slides HTML (Wrappers)...[/bold cyan]")
    
    for i in track(range(1, 17), description="Gerando HTML dos slides..."):
        name_stem = f"slide-{i:02d}"
        html_path = slides_dst_dir / f"{name_stem}.html"
        html_path.write_text(generate_slide_html(name_stem), encoding='utf-8')


def generate_all_quizzes():
    """Ignorado: Quizzes já foram convertidos e marcados no repositório"""
    print("\n[bold magenta]PROCESSO: Quizzes interativos já compilados em docs/quizzes/.[/bold magenta]")


def main():
    print(f"[bold]START: Automação de Conteúdo: {SITE_NAME}[/bold]")
    print("=" * 50)
    
    generate_all_slides()
    generate_all_quizzes()
    
    print("\n[green]OK: Conteúdo de Slides e Quizzes gerado com sucesso![/green]")


if __name__ == '__main__':
    main()
