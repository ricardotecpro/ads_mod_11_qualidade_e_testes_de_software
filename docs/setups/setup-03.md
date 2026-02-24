# Setup 03: Python para QA 🐍

O Python é uma das linguagens mais amigáveis para quem está começando na automação de testes.

## 1. Instalando o Python
1.  Baixe a versão mais recente em [python.org](https://www.python.org/).
2.  **IMPORTANTE**: Marque a caixa **"Add Python to PATH"** na instalação!
3.  Teste no terminal: `python --version`.

## 2. Ambientes Virtuais (VENV)
Sempre crie ambientes isolados para seus projetos de teste para evitar conflitos de bibliotecas:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate   # Windows
```

## 3. Gerenciando Dependências (PIP)
Use o `pip` para instalar bibliotecas como `pytest`, `selenium` e `behave` (BDD):
```bash
pip install pytest selenium behave
```

## 4. PyTest (O Framework de Escolha)
O PyTest é o padrão para testes em Python. Crie um arquivo `test_exemplo.py` e rode:
```bash
pytest
```

## 5. Solução de Problemas ⚠️
*   **'python' não encontrado**: Certifique-se de que o PATH foi configurado corretamente.
*   **Permissão no Windows**: Se não conseguir ativar o venv, rode `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser` no PowerShell (como Admin).