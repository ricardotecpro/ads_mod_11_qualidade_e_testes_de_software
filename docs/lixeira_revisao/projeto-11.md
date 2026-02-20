# Projeto 11 - Simulador de Corrida (Async) 🏎️

**Objetivo**: Dominar o uso de Coroutines e CoroutineScopes.

## O Desafio
Simule dois carros correndo no log em paralelo:
1.  Crie duas funções `suspend` que representam Carro A e Carro B.
2.  Cada função deve fazer um loop de 1 a 10, com `delay()` aleatório entre as iterações.
3.  Use o `viewModelScope.launch` para iniciar as duas coroutines simultaneamente.
4.  Imprima no Logcat: "Carro A: 50m...", "Carro B: 60m...".
5.  Ao final, mostre quem ganhou a corrida em um `TextView`.

## Dica
Use `withContext(Dispatchers.Main)` para atualizar o `TextView` quando a corrida terminar, caso esteja dentro do `Dispatchers.Default`.