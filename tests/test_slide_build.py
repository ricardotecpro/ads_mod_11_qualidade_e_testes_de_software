"""
Testes para verificar se os slides foram copiados corretamente para o build
"""
import pytest
from pathlib import Path


def test_slide_markdown_copied_to_site():
    """Verifica se todos os arquivos markdown foram copiados para site/slides/"""
    site_slides = Path("site/slides")
    
    if not site_slides.exists():
        pytest.skip("Diretório site/slides/ não existe. Execute 'mkdocs build' primeiro.")
    
    for i in range(1, 17):
        slide_md = site_slides / f"slide-{i:02d}.md"
        assert slide_md.exists(), (
            f"Slide markdown {slide_md.name} não foi copiado para {site_slides}. "
            f"Verifique o hook copy_slides.py"
        )


def test_slide_html_copied_to_site():
    """Verifica se todos os arquivos HTML foram copiados para site/slides/"""
    site_slides = Path("site/slides")
    
    if not site_slides.exists():
        pytest.skip("Diretório site/slides/ não existe. Execute 'mkdocs build' primeiro.")
    
    for i in range(1, 17):
        slide_html = site_slides / f"slide-{i:02d}.html"
        assert slide_html.exists(), (
            f"Slide HTML {slide_html.name} não foi copiado para {site_slides}. "
            f"Verifique o hook copy_slides.py"
        )


def test_slide_markdown_content_valid_in_site():
    """Verifica se o markdown copiado tem conteúdo válido"""
    site_slides = Path("site/slides")
    
    if not site_slides.exists():
        pytest.skip("Diretório site/slides/ não existe. Execute 'mkdocs build' primeiro.")
    
    slide_md = site_slides / "slide-01.md"
    if not slide_md.exists():
        pytest.fail(f"Arquivo {slide_md} não existe no build")
    
    content = slide_md.read_text(encoding='utf-8')
    assert len(content) > 50, "Markdown copiado tem conteúdo muito pequeno"
    assert '---' in content or '#' in content, "Markdown copiado não tem conteúdo válido"


def test_all_slides_present_in_site():
    """Verifica se todos os 16 slides (HTML + MD) estão presentes no build"""
    site_slides = Path("site/slides")
    
    if not site_slides.exists():
        pytest.skip("Diretório site/slides/ não existe. Execute 'mkdocs build' primeiro.")
    
    # Contar arquivos
    html_files = list(site_slides.glob("slide-*.html"))
    md_files = list(site_slides.glob("slide-*.md"))
    
    assert len(html_files) == 16, (
        f"Esperado 16 arquivos HTML, encontrado {len(html_files)}"
    )
    assert len(md_files) == 16, (
        f"Esperado 16 arquivos Markdown, encontrado {len(md_files)}. "
        f"Verifique se o hook copy_slides.py está usando o padrão correto (slide-*.md)"
    )


def test_slide_index_exists_in_site():
    """Verifica se o index.html dos slides existe no build"""
    site_slides = Path("site/slides")
    
    if not site_slides.exists():
        pytest.skip("Diretório site/slides/ não existe. Execute 'mkdocs build' primeiro.")
    
    index_html = site_slides / "index.html"
    assert index_html.exists(), "index.html dos slides não foi gerado no build"
