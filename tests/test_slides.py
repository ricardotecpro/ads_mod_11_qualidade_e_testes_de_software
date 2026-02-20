"""
Testes automatizados para verificar renderização de slides com RevealJS
"""
import pytest
from playwright.sync_api import Page, expect


class TestSlides:
    """Testes para slides RevealJS"""

    def test_slides_index_loads(self, page_with_base_url: Page, base_url: str):
        """Verifica se a página de índice de slides carrega"""
        page = page_with_base_url
        page.goto(f"{base_url}/slides/")
        
        # Verifica se não é 404
        expect(page).not_to_have_title("404")
        expect(page.locator("h1")).to_contain_text("Slides")

    @pytest.mark.parametrize("lesson_number", range(1, 17))
    def test_slide_page_loads(self, page_with_base_url: Page, base_url: str, lesson_number: int):
        """Verifica se cada página de slide carrega sem erro 404"""
        page = page_with_base_url
        # Check for the standalone HTML file generated/copied by the hook
        slide_url = f"{base_url}/slides/slide-{lesson_number:02d}.html"
        
        page.goto(slide_url, wait_until="networkidle")
        
        # Verifica se não é 404
        expect(page).not_to_have_title("404")
        
        # Verify it's a RevealJS presentation (with longer timeout for CI)
        # RevealJS needs time to load from CDN and initialize
        expect(page.locator(".reveal")).to_be_attached(timeout=20000)

    def test_revealjs_present_on_slide_01(self, page_with_base_url: Page, base_url: str):
        """Verifica se RevealJS está presente no slide 01"""
        page = page_with_base_url
        page.goto(f"{base_url}/slides/slide-01.html")
        
        # Verifica se a estrutura RevealJS existe
        reveal_container = page.locator(".reveal")
        expect(reveal_container).to_be_visible()

    def test_slide_navigation_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se controles de navegação de slides existem"""
        page = page_with_base_url
        page.goto(f"{base_url}/slides/slide-01.html")
        
        # RevealJS adiciona controles de navegação
        # Check if controls exist in DOM (might be disabled/hidden on first slide)
        controls = page.locator(".navigate-right")
        expect(controls).to_be_attached()

    def test_slide_content_visible(self, page_with_base_url: Page, base_url: str):
        """Verifica se o conteúdo do slide está visível"""
        page = page_with_base_url
        page.goto(f"{base_url}/slides/slide-01.html")
        
        # RevealJS usa .slides como container de slides
        slides_container = page.locator(".slides")
        expect(slides_container).to_be_visible()
        
        # Verifica se há pelo menos um slide
        slide = page.locator(".slides section").first
        expect(slide).to_be_visible()

    def test_slide_markdown_loads_without_404(self, page_with_base_url: Page, base_url: str):
        """Verifica que markdown carrega sem erro 404 - TESTE CRÍTICO"""
        page = page_with_base_url
        
        # Interceptar requisições de rede para detectar 404
        errors_404 = []
        def handle_response(response):
            if response.status == 404:
                errors_404.append(response.url)
        
        page.on("response", handle_response)
        
        # Acessar slide
        page.goto(f"{base_url}/slides/slide-01.html", wait_until="networkidle")
        
        # Aguardar RevealJS carregar e processar markdown
        page.wait_for_timeout(3000)
        
        # Verificar que não houve 404
        assert len(errors_404) == 0, (
            f"Erros 404 encontrados ao carregar slide: {errors_404}. "
            f"Verifique se os arquivos .md foram copiados para site/slides/ pelo hook."
        )
