# Exercícios: Aula 08 - Caixa Branca ⚪

## 🟢 Básico

1.  **Visibilidade**: O que diferencia o teste de Caixa Branca do teste de Caixa Preta em relação ao acesso do testador ao código-fonte?
2.  **Cobertura**: O que significa dizer que um projeto tem "80% de code coverage"?

## 🟡 Intermediário

3.  **Complexidade Ciclomática**: Imagine uma função com 10 comandos `if` encadeados. Por que essa função é considerada difícil de testar via Caixa Branca?
4.  **Cobertura de Decisão**: Se eu tenho um código `if (A && B)`, quantos casos de teste eu preciso, no mínimo, para garantir que todas as condições da decisão foram testadas (Verdadeiro/Falso)?

## 🔴 Desafio

5.  **Análise de Fluxo**: Desenhe o grafo de fluxo de controle para o código abaixo e identifique o "caminho feliz" e o "caminho de exceção":
```python
def check_status(active, balance):
    if active:
        if balance > 0:
            return "Pode Comprar"
        else:
            return "Saldo Insuficiente"
    return "Conta Inativa"
```
