"""
Testes para verificar a geração correta dos slides
"""
import pytest
from pathlib import Path


def test_slide_markdown_files_exist():
    """Verifica se todos os arquivos markdown dos slides existem em docs/slides/"""
    slides_dir = Path("docs/slides")
    
    for i in range(1, 17):
        slide_md = slides_dir / f"slide-{i:02d}.md"
        assert slide_md.exists(), f"Slide markdown {slide_md.name} não encontrado em {slides_dir}"


def test_slide_html_files_exist():
    """Verifica se todos os arquivos HTML dos slides existem em docs/slides/"""
    slides_dir = Path("docs/slides")
    
    for i in range(1, 17):
        slide_html = slides_dir / f"slide-{i:02d}.html"
        assert slide_html.exists(), f"Slide HTML {slide_html.name} não encontrado em {slides_dir}"


def test_slide_html_references_correct_markdown():
    """Verifica se cada HTML referencia o arquivo markdown correto"""
    slides_dir = Path("docs/slides")
    
    for i in range(1, 17):
        slide_html = slides_dir / f"slide-{i:02d}.html"
        content = slide_html.read_text(encoding='utf-8')
        expected_ref = f'data-markdown="slide-{i:02d}.md"'
        assert expected_ref in content, (
            f"HTML {slide_html.name} não referencia markdown correto. "
            f"Esperado: {expected_ref}"
        )


def test_slide_markdown_has_content():
    """Verifica se os arquivos markdown têm conteúdo válido"""
    slides_dir = Path("docs/slides")
    
    for i in range(1, 17):
        slide_md = slides_dir / f"slide-{i:02d}.md"
        content = slide_md.read_text(encoding='utf-8')
        
        # Deve ter conteúdo mínimo
        assert len(content) > 50, f"Slide {slide_md.name} tem conteúdo muito pequeno"
        
        # Deve ter separadores de slide (---) ou conteúdo markdown
        assert '---' in content or '#' in content, (
            f"Slide {slide_md.name} não parece ter conteúdo markdown válido"
        )


def test_slide_html_has_revealjs_structure():
    """Verifica se os HTML têm a estrutura básica do RevealJS"""
    slides_dir = Path("docs/slides")
    slide_html = slides_dir / "slide-01.html"
    content = slide_html.read_text(encoding='utf-8')
    
    # Verificar elementos essenciais do RevealJS
    assert '<div class="reveal">' in content, "HTML não tem div.reveal"
    assert '<div class="slides">' in content, "HTML não tem div.slides"
    assert 'reveal.js' in content.lower(), "HTML não referencia reveal.js"
    assert 'data-markdown' in content, "HTML não usa data-markdown"
