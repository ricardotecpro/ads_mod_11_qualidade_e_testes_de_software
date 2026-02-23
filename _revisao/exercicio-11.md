# Exercícios 11 - Threads e Async 🧵

## 🟢 Fáceis

1.  **ANR**: O que significa a sigla ANR e o que causa esse erro?
2.  **Main Thread**: O que deve e o que NÃO deve rodar na Main Thread?

## 🟡 Médios

3.  **Dispatchers**:
    Qual `Dispatcher` você usaria para:
    a) Ordenar uma lista de 10.000 nomes (CPU intensive).
    b) Salvar um arquivo no disco (IO).
    c) Atualizar um TextView (UI).
4.  **Suspensão**:
    O que acontece com a Thread Principal quando ela encontra uma função `suspend` que chama `delay(5000)`? Ela trava por 5 segundos ou continua livre para desenhar a tela?
5.  **Sockets vs REST**:
    Explique a principal diferença entre uma comunicação REST e uma comunicação via Sockets (TCP). Quando você escolheria usar Sockets em vez de REST em um aplicativo Android?

## 🔴 Desafio

6.  **Race Condition (Condição de Corrida)**:
    Duas coroutines tentam alterar a mesma variável `contador = 0` ao mesmo tempo. Ambas leem 0, somam 1 e salvam 1. O resultado final é 1, mas deveria ser 2.
    *   Como resolver isso em Kotlin (Mutex, Atomic, ou Single Thread)?