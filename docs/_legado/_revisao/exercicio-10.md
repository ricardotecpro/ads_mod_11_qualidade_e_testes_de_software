# Exercícios 10 - Consumo de API REST 🌍

## 🟢 Fáceis

1.  **Verbos HTTP**: Qual verbo HTTP usamos para **obter** dados e qual usamos para **enviar** dados novos?
2.  **Permissão**: Qual permissão deve ser adicionada no `AndroidManifest.xml` para que o Retrofit funcione?

## 🟡 Médios

3.  **Conversão**:
    O que acontece se o campo no JSON for `"user_name"` (snake_case) e na sua data class for `val userName: String` (camelCase)? Como o Retrofit/Gson sabe mapear isso? (Pesquise sobre anotação `@SerializedName`).
4.  **Threading**:
    O Retrofit (com Coroutines) precisa que você use `withContext(Dispatchers.IO)` manualmente na chamada, ou ele já faz isso por baixo dos panos?
5.  **Autenticação**:
    Se uma API exige um token JWT no cabeçalho `Authorization`, como você configuraria o Retrofit para enviar esse token em todas as requisições sem repetir código? (Pesquise sobre `OkHttp Interceptors`).

## 🔴 Desafio

6.  **Status Code**:
    Se a API retornar erro 401 (Não Autorizado) ou 500 (Erro no Servidor), como você capturaria isso no bloco `try/catch` do ViewModel para exibir uma mensagem adequada ao usuário?