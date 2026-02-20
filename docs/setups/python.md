# Setup do Ambiente: Python e Pytest 🐍

Para realizar as automações de testes unitários e TDD, você precisará configurar o Python em sua máquina.

## 1. Instalando o Python
- **Windows**: Baixe o instalador em [python.org](https://www.python.org/downloads/). Certifique-se de marcar a opção **"Add Python to PATH"**.
- **Linux/Mac**: Geralmente já vem instalado. Use `python3 --version` para conferir.

## 2. Criando um Ambiente Virtual (Venv)
É uma boa prática isolar as dependências de cada projeto:
```bash
# Criar o ambiente
python -m venv venv

# Ativar (Windows)
.\venv\Scripts\activate

# Ativar (Linux/Mac)
source venv/bin/activate
```

## 3. Instalando o Pytest e Coverage
Com o ambiente ativado, instale as ferramentas de teste:
```bash
pip install pytest pytest-cov
```

## 4. Verificando a Instalação
Execute o comando abaixo para garantir que tudo está pronto:
```bash
pytest --version
```

---
> [!TIP]
> Use o arquivo `requirements.txt` para gerenciar suas dependências de forma profissional!
