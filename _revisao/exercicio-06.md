# Exercícios 06 - Navegação 🗺️

## 🟢 Fáceis

1.  **Conceito**: O que é uma `Intent` no Android?
2.  **Tipos**: Qual a diferença entre uma Intent **Explícita** e uma **Implícita**?

## 🟡 Médios

3.  **Passagem de Dados**:
    Escreva um trecho de código (Kotlin) para enviar o número `42` para a Activity `RespostaActivity` com a chave "RESPOSTA_FIXA".
4.  **Ciclo de Vida**:
    Quando abrimos a Activity B a partir da A, o método `onStop()` da A é chamado? E o `onDestroy()`? Justifique.

## 🔴 Desafio

5.  **Fluxo de Navegação**:
    Você tem 3 telas: A -> B -> C.
    *   Na tela C, existe um botão "Home" que deve levar para a tela A, mas **limpando** a tela B e C da pilha (para que o botão voltar não funcione). Qual flag de Intent você usaria ou qual a lógica para isso?