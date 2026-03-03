import pytest
import re
import yaml
import pathlib
from playwright.sync_api import Page, expect

def load_mkdocs_config():
    """Carrega o título do site do mkdocs.yml para agnosticismo nos testes"""
    config_path = pathlib.Path("mkdocs.yml")
    if config_path.exists():
        with open(config_path, "r", encoding="utf-8") as f:
            return yaml.load(f, Loader=yaml.UnsafeLoader)
    return {}

CONFIG = load_mkdocs_config()
SITE_NAME = CONFIG.get("site_name", "Curso")

class TestNavigation:
    """Testes para navegação do site (Totalmente Agnóstico)"""

    def test_home_page_loads(self, page_with_base_url: Page, base_url: str):
        """Verifica se a página inicial carrega com o título correto"""
        page = page_with_base_url
        page.goto(base_url)
        
        # O título deve conter o site_name definido no mkdocs.yml
        expect(page).to_have_title(re.compile(rf".*{re.escape(SITE_NAME)}.*"))

    def _ensure_menu_visible(self, page: Page):
        """Helper to ensure menu is visible (opens drawer if needed)"""
        drawer_button = page.locator("label.md-header__button[for='__drawer']")
        if drawer_button.is_visible() and not page.locator(".md-sidebar--primary").is_visible():
            drawer_button.click()

    def test_aulas_menu_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se o menu 'Aulas' existe"""
        page = page_with_base_url
        page.goto(base_url)
        self._ensure_menu_visible(page)
        
        link = page.get_by_role("link", name="Aulas").first
        expect(link).to_be_visible()

    def test_print_version_link_exists(self, page_with_base_url: Page, base_url: str):
        """Verifica se o link 'Impressão' existe"""
        page = page_with_base_url
        page.goto(base_url)
        
        print_link = page.locator("a[href*='print_page']")
        expect(print_link.first).to_be_attached()

    def test_navigation_to_lesson_01(self, page_with_base_url: Page, base_url: str):
        """Verifica se é possível navegar para Aula 01 e se o título da aula está presente"""
        page = page_with_base_url
        page.goto(base_url)
        self._ensure_menu_visible(page)
        
        # Clica em Aulas para expandir ou navegar
        page.get_by_role("link", name="Aulas").first.click(force=True)
        
        # Clica na Aula 01 (exact para evitar pegar sub-menus)
        page.get_by_role("link", name="Aula 01", exact=False).first.click()
        
        # Verifica URL
        expect(page).to_have_url(re.compile(r".*/aulas/aula-01/?$"))
        
        # Verifica se existe um H1 (agnóstico ao conteúdo)
        expect(page.locator("h1")).to_be_visible()
        expect(page.locator("h1")).to_contain_text("Aula 01")
