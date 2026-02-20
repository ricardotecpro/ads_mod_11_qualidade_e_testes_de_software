# Aula 10 - Consumindo API REST (Retrofit) 🌍

!!! tip "Objetivo"
    **Objetivo**: Conectar o aplicativo à internet, baixar dados JSON de uma API REST e convertê-los em objetos Kotlin usando a biblioteca Retrofit.

---

## 1. O que é uma API REST? 🔌

É como um garçom.
1.  **Client (Você)**: Faz um pedido (Request). "Quero a lista de usuários".
2.  **API (Garçom)**: Leva o pedido à cozinha (Servidor).
3.  **Response**: Traz a comida (Dados JSON).

Trabalharemos com **JSON** JavaScript Object Notation):
```json
{
  "id": 1,
  "nome": "Ricardo",
  "linguagens": ["Kotlin", "Swift"]
}
```

---

## 2. A Biblioteca Retrofit 🚀

No Android, ninguém faz requisições HTTP "na mão" (abrindo Socket). Usamos o **Retrofit** (da Square). Ele é o padrão de mercado.

Ele faz 3 mágicas:
1.  Conecta na internet.
2.  Converte JSON para Objetos Kotlin (usando **Gson** ou **Moshi**).
3.  Gerencia Threads (com Coroutines).

### 🆚 Comparação: URLSession / Alamofire (iOS)
*   **Nativo**: No Android tínhamos `HttpUrlConnection` (horrível), no iOS tem `URLSession` (muito bom).
*   **Bibliotecas**: Android usa Retrofit. iOS usa muito Alamofire (embora o nativo hoje seja suficiente).

---

## 3. Implementando em 3 Passos 👣

### Passo 1: O Modelo (Data Class)
Deve bater com o JSON.

```kotlin
data class Usuario(
    val id: Int,
    val name: String, // O nome do campo deve ser IGUAL ao do JSON
    val email: String
)
```

### Passo 2: A Interface (Contrato)
Definimos as rotas da API.

```kotlin
interface ApiService {
    @GET("users") // Endpoint: https://api.site.com/users
    suspend fun listarUsuarios(): List<Usuario>
    
    @GET("users/{id}")
    suspend fun obterUsuario(@Path("id") id: Int): Usuario
}
```
*Note o `suspend`: indica que é assíncrono (Coroutines).*

### Passo 3: O Cliente (Instância)

```kotlin
val retrofit = Retrofit.Builder()
    .baseUrl("https://jsonplaceholder.typicode.com/")
    .addConverterFactory(GsonConverterFactory.create()) // Conversor JSON
    .build()

val servico = retrofit.create(ApiService::class.java)
```

---

## 4. Chamando na ViewModel 🧠

Nunca chame a API direto na Activity!

```kotlin
class UserViewModel : ViewModel() {
    val usuarios = MutableLiveData<List<Usuario>>()

    fun buscarDados() {
        viewModelScope.launch { // Coroutine
            try {
                val lista = servico.listarUsuarios()
                usuarios.value = lista
            } catch (e: Exception) {
                // Tratar erro (falta de net, 404, etc)
            }
        }
    }
}
```

---

## 5. Permissão de Internet 🌐

Não esqueça! No `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```
Sem isso, o app crasha com `SecurityException`.

---

## 6. Autenticação e Segurança 🔐

Apps reais quase sempre precisam de login. Os padrões mais comuns são:

1.  **Basic Auth**: Envia usuário e senha em cada pedido (Inseguro sozinho).
2.  **Bearer Token (JWT)**: Após o login, o servidor devolve um "Token". Você envia esse token no cabeçalho (Header) de todas as próximas chamadas.
3.  **OAuth2**: Padrão para "Login com Google/Facebook".

### Adicionando Token no Retrofit (Interceptor)
Não precisamos colocar o token manualmente em cada função. Usamos um `Interceptor` do OkHttp:

```kotlin
val client = OkHttpClient.Builder().addInterceptor { chain ->
    val novoRequest = chain.request().newBuilder()
        .addHeader("Authorization", "Bearer $MEU_TOKEN")
        .build()
    chain.proceed(novoRequest)
}.build()

val retrofit = Retrofit.Builder()
    .client(client) // Vincula o cliente customizado
    .baseUrl(...)
    .build()
```

---

## 7. Ferramentas Úteis 🛠️

*   **Postman / Insomnia**: Para testar a API antes de codar.
*   **Mocky.io**: Para criar APIs falsas (Mock) para teste.
*   **QuickType.io**: Cola o JSON lá, ele gera a Data Class Kotlin pronta! (Dica de ouro ✨).

---

## 7. Desafio: Consumindo o GitHub 🐙

1.  Crie uma data class `Repo` (nome, stars, url).
2.  Use a API pública do GitHub: `https://api.github.com/users/{SEU_USER}/repos`.
3.  Exiba o nome dos seus repositórios no Logcat (`Log.d`).

---

**Próxima Aula**: O que é esse `suspend` e `launch`? Vamos entender o mundo **Assíncrono**. [Threads e Coroutines](./aula-11.md) 🧵