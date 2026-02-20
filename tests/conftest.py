"""
Configuração compartilhada para testes com Playwright
"""
import pytest
import subprocess
import requests
import os
from pathlib import Path
from time import sleep
from playwright.sync_api import Page, expect


@pytest.fixture(autouse=True)
def start_server():
    """
    Inicia um servidor HTTP local para servir o site gerado (site/)
    para cada teste (escopo de função).
    """
    site_dir = Path("site").absolute()
    
    # Verifica se o site foi gerado
    if not site_dir.exists() or not (site_dir / "index.html").exists():
        pytest.fail("Diretório 'site/' não encontrado ou inválido. Execute 'poetry run task build' antes dos testes.")

    # Porta fixa para teste (definida também no pyproject.toml)
    port = "8766"
    url = f"http://localhost:{port}"
    
    # Start HTTP server in background
    # Usamos shell=True para o windows encontrar o python se necessário, mas array é melhor
    server_process = subprocess.Popen(
        ["python", "-m", "http.server", port, "--directory", str(site_dir)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    
    # Wait for server to be ready with retry
    max_retries = 10
    server_started = False
    
    for i in range(max_retries):
        try:
            response = requests.get(url, timeout=1)
            if response.status_code == 200:
                server_started = True
                break
        except requests.exceptions.RequestException:
            sleep(1)
            
    if not server_started:
        server_process.terminate()
        pytest.fail(f"Servidor HTTP falhou ao iniciar em {url}")
    
    yield
    
    # Cleanup: terminate server
    server_process.terminate()
    server_process.wait()


@pytest.fixture
def page_with_base_url(page: Page, base_url: str):
    """Página do Playwright com URL base configurada"""
    page.set_default_timeout(30000)  # 30 segundos
    return page
