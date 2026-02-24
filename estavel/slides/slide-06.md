# Controle de Versão e CI 🐙
## Aula 06 - Automação de Processos

---

## Por que Git? 🏛️

- Histórico de mudanças
- Trabalho em equipe
- Branches para isolar novas features

---

## Integração Contínua (CI) 🚀

- Integrar o código várias vezes ao dia
- Build e Testes rodam automaticamente
- Feedback rápido para o time

---

## GitHub Actions ⚙️

- Workflows baseados em eventos
- Arquivos `.yml` na pasta `.github/workflows`
- Execução em containers (Ubuntu, Mac, Windows)

---

## Estrutura da Pipeline 🏗️

1.  **Checkout**: Baixa o código
2.  **Setup**: Instala linguagens e dependências
3.  **Lint**: Checa o estilo do código
4.  **Test**: Roda os testes automatizados
5.  **Build**: Gera os artefatos finais

---

## Fail Fast! 🛑

- O objetivo é falhar o mais rápido possível
- Se o lint falhou, não precisa rodar os testes caros
- Economiza tempo e recursos

---

## Fim da Aula 06 🏁
### Próximo passo: Técnicas de Caixa Preta!
