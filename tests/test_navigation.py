"""
Testes automatizados para navegação do site
"""
import pytest
import re
from playwright.sync_api import Page, expect


class TestNavigation:
    """Testes para navegação do site"""

    def test_home_page_loads(self, page_with_base_url: Page, base_url: str):
        """Verifica se a página inicial carrega"""
        page = page_with_base_url
        page.goto(base_url)
        
        expect(page).to_have_title("Lógica e Algoritmos - Curso")

    def _ensure_menu_visible(self, page: Page):
        """Helper to ensure menu is visible (opens drawer if needed)"""
        # Use more specific selector for the header button to avoid ambiguity
        drawer_button = page.locator("label.md-header__button[for='__drawer']")
        if drawer_button.is_visible():
            drawer_button.click()

    def test_curso_menu_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se o menu 'Aulas' existe"""
        page = page_with_base_url
        page.goto(base_url)
        
        # Open menu if mobile
        self._ensure_menu_visible(page)
        
        # Procura pelo item de menu "Aulas"
        # Usando match flexível
        link = page.get_by_role("link", name="Aulas").first
        expect(link).to_be_visible()

    def test_plano_ensino_menu_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se o menu 'Plano de Ensino' existe"""
        page = page_with_base_url
        page.goto(base_url)
        
        self._ensure_menu_visible(page)
        
        # Procura pelo item de menu "Plano de Ensino"
        link = page.get_by_role("link", name="Plano de Ensino", exact=True).first
        expect(link).to_be_visible()

    def test_print_version_link_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se o link 'Impressão' existe"""
        page = page_with_base_url
        page.goto(base_url)
        
        # Link de impressão geralmente é um ícone no header ou footer
        # Verificamos a presença no DOM, searching for print_page
        print_link = page.locator("a[href*='print_page']")
        expect(print_link.first).to_be_attached()

    def test_navigation_to_lesson_01(self, page_with_base_url: Page, base_url: str):
        """Verifica se é possível navegar para Aula 01"""
        page = page_with_base_url
        page.goto(base_url)
        
        self._ensure_menu_visible(page)
        
        # Navigate Aulas -> Módulo 1: Fundamentos -> Aula 01
        # Click Aulas
        page.get_by_role("link", name="Aulas").first.click(force=True)
        
        # Click Módulo 1: Fundamentos
        page.get_by_text("Módulo 1: Fundamentos").first.click()
        
        # Click Aula 01
        page.get_by_role("link", name="Aula 01", exact=True).first.click()
        
        # Verifica se chegou na página correta
        expect(page).to_have_url(re.compile(r".*/aulas/aula-01/?$"))
        # H1 is "Aula 01 - Introdução à Lógica..."
        expect(page.locator("h1")).to_contain_text("Introdução à Lógica")
