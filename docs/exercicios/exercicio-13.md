# Exercícios: Aula 13 - Automação Web 🤖

## 🟢 Básico

1.  **Seletores**: Quais são os três principais tipos de seletores (IDs, Classes, etc.) usados para localizar elementos em uma página web? Qual deles é o mais estável?
2.  **Happy Path**: O que significa o termo "Caminho Feliz" (Happy Path) na automação E2E?

## 🟡 Intermediário

3.  **Auto-waiting**: Como ferramentas modernas como o Playwright lidam com elementos que demoram para carregar na página? Por que isso é melhor do que usar `sleep(5)`?
4.  **Localizadores**: Por que é uma má prática usar o **XPath Absoluto** (ex: `/html/body/div[1]/div[2]/...`) em seus testes automatizados?

## 🔴 Desafio

5.  **Script de Teste**: Imagine que você precisa testar um formulário que contém:
    - Um campo de texto para o Nome.
    - Um checkbox para "Aceito os termos".
    - Um botão de "Enviar".
    **Escreva o roteiro** (passo a passo) de como o robô deve interagir com esses elementos e qual seria a validação (assertion) final para confirmar o envio com sucesso.
