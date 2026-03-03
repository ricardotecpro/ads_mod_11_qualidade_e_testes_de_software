# Exercícios 07 - Arquitetura MVVM 🏗️

## 🟢 Fáceis

1.  **Responsabilidades**: No padrão MVVM, quem é responsável por decidir _o que_ mostrar na tela? (Model, View ou ViewModel?)
2.  **Ciclo de Vida**: O que acontece com os dados dentro de um `ViewModel` quando a tela gira (rotaciona)?

## 🟡 Médios

3.  **LiveData**:
    Explique o conceito de "Oberver Pattern" usado no LiveData. Por que a Activity precisa "observar" os dados?
4.  **Separação**:
    Por que não devemos passar uma referência da `View` (ex: um `TextView`) para dentro do `ViewModel`? (Dica: pense em vazamento de memória e ciclo de vida).

## 🔴 Desafio

5.  **Arquitetura Real**:
    Imagine um app de Clima.
    *   **Model**: Classe `ClimaRepository` que pega dados da API.
    *   **ViewModel**: Chama o repositório e guarda `val temperatura = MutableLiveData<Float>()`.
    *   **View**: Mostra o texto "25°C".
    
    Se a internet cair no meio da requisição, quem deve tratar o erro e onde deve ficar a mensagem de erro (String) para ser exibida? No Model, ViewModel ou View?