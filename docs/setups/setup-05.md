# Setup 05: Node.js & Playwright / Cypress 🟢

O ecossistema JavaScript/TypeScript é hoje um dos mais populares para automação de testes "Shift Left".

## 1. Instalando o Node.js
1.  Baixe a versão **LTS** (Long Term Support) em [nodejs.org](https://nodejs.org/).
2.  Teste: `node -v` e `npm -v`.

## 2. Playwright (O sucessor do Selenium)
Moderno, rápido e com suporte nativo a execução paralela.
```bash
npm init playwright@latest
```

## 3. Cypress (Focado em Desenvolvedores)
Excelente para testes E2E com uma interface visual incrível.
```bash
npm install cypress --save-dev
npx cypress open
```

## 4. TypeScript (Recomendado)
Para automação robusta, prefira TypeScript ao invés de JS puro para ter autocompletar e tipagem nos seus seletores.

## 5. Solução de Problemas Comuns ⚠️
*   **npm ERR!**: Tente limpar o cache: `npm cache clean --force`.
*   **npx não funciona**: Verifique se o Node foi instalado com permissões de administrador.