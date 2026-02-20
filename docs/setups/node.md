# Setup do Ambiente: Node.js e Playwright 🎭

Para a automação de testes Web (E2E), utilizaremos o ecossistema Node.js.

## 1. Instalando o Node.js
- Baixe a versão **LTS** (Long Term Support) em [nodejs.org](https://nodejs.org/).
- Após instalar, verifique no terminal:
  ```bash
  node -v
  npm -v
  ```

## 2. Iniciando um Projeto de Teste
Crie uma pasta para seus testes e inicie o Playwright:
```bash
mkdir meus-testes-web
cd meus-testes-web
npm init playwright@latest
```

## 3. Configurações Iniciais
Durante a instalação, o Playwright perguntará se deseja instalar os navegadores (Chromium, Firefox, WebKit). Responda **Sim (Y)**.

## 4. Executando os Testes Exemplo
```bash
npx playwright test
```

## 5. Visualizando o Relatório (Report)
```bash
npx playwright show-report
```

---
> [!IMPORTANT]
> O Playwright requer que o Node.js esteja atualizado. Se encontrar erros, verifique sua versão com `node -v`.
