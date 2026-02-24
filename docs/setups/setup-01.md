# Setup 01: Selenium & WebDriver 🤖

O Selenium é o padrão de mercado para automação de navegadores web. Nele, usamos o **WebDriver** para controlar o navegador.

## 1. Instalando o Selenium (Python)
Se você estiver usando Python, instale via pip:
```bash
pip install selenium
```

## 2. WebDrivers (Navegadores)
Para que o código consiga "clicar" no navegador, você precisa do driver correspondente:

*   **Google Chrome**: Recomenda-se usar o `webdriver-manager` para baixar automaticamente.
*   **Firefox**: Baixe o **GeckoDriver** em [github.com/mozilla/geckodriver](https://github.mozilla.com/geckodriver/releases).

## 3. Gestão Automática de Drivers
A melhor prática hoje é usar bibliotecas que gerenciam os drivers para você:

```python
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
```

## 4. Playwright (Alternativa Moderna)
Se preferir usar o Playwright (muito comum em JS/TS e Python):
```bash
pip install playwright
playwright install
```

## 5. Solução de Problemas ⚠️
*   **Drivers Desatualizados**: Sempre garanta que a versão do seu navegador (Chrome) é a mesma da versão do driver (ChromeDriver).
*   **Path**: Se não usar o manager, o executável do driver deve estar no PATH do sistema.