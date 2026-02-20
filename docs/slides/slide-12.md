# Unitários e Integração 🔗
## Aula 12 - A Pirâmide de Automação

---

## A Pirâmide de Testes 🏗️

- **Topo (UI/E2E)**: Poucos, lentos e caros
- **Meio (Integração)**: Equilíbrio
- **Base (Unitários)**: Muitos, rápidos e baratos

---

## Padrão AAA 📐

1.  **Arrange (Organizar)**: Preparar os dados
2.  **Act (Agir)**: Executar a função
3.  **Assert (Verificar)**: Validar o resultado

---

## Mocks e Dublês 🎭

- Isolar o teste de dependências reais
- Simular banco de dados, APIs e serviços externos
- Garante que o teste seja determinístico

---

## Testes de Integração 🛰️

- Validar como as unidades conversam entre si
- Encontrar erros de contrato e comunicação
- Testar a jornada de dados entre módulos

---

## Cobertura de Testes 📊

- Use métricas para saber onde ainda faltam testes
- No Python: `pytest --cov`
- Lembre-se: 100% de cobertura não é 0% de bugs!

---

## Fim da Aula 12 🏁
### Próximo passo: Automação Web com Playwright!
