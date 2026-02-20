# Aula 10 - APIs REST & Retrofit 🌍

<!-- .slide: data-transition="zoom" -->

---

## 📡 O App e a Internet

Raramente um app vive sozinho. Ele precisa de dados externos.

* Previsão do tempo. <!-- .element: class="fragment" -->
* Posts de redes sociais. <!-- .element: class="fragment" -->
* Salvar pedidos em um servidor. <!-- .element: class="fragment" -->

---

## 🍕 O Conceito de API REST

Pense em um restaurante (Servidor) e você (Cliente).

1. **Request**: Você pede um prato. <!-- .element: class="fragment" -->
2. **Endpoint**: A mesa do restaurante (`/pedidos`). <!-- .element: class="fragment" -->
3. **Response**: O prato chega (JSON). <!-- .element: class="fragment" -->

---

### O Formato JSON 📦

É como o mundo troca dados hoje.

```json
{
  "usuario": "Ricardo",
  "idade": 30,
  "ativo": true
}
```

---

## 🚀 Conheça o Retrofit

A biblioteca da Square que é o padrão absoluto no Android.

* Transforma APIs em interfaces Kotlin. <!-- .element: class="fragment" -->
* Faz o "parse" do JSON automaticamente. <!-- .element: class="fragment" -->
* Suporte nativo a Coroutines. <!-- .element: class="fragment" -->

---

## 🔨 Implementação em 3 Passos

---

### 1. A Data Class (O Modelo)

Deve ser o espelho do JSON.

```kotlin
data class Post(
    val userId: Int,
    val id: Int,
    val title: String,
    val body: String
)
```

---

### 2. A Interface (O Contrato)

```kotlin
interface ApiService {
    @GET("posts")
    suspend fun obterPosts(): List<Post>

    @GET("posts/{id}")
    suspend fun obterPostUnico(@Path("id") id: Int): Post
}
```

---

### 3. A Instância (O Cliente)

```kotlin
val retrofit = Retrofit.Builder()
    .baseUrl("https://jsonplaceholder.typicode.com/")
    .addConverterFactory(GsonConverterFactory.create())
    .build()

val api = retrofit.create(ApiService::class.java)
```

---

## 🧠 Chamando na ViewModel

Nunca trave a UI Thread!

```kotlin
viewModelScope.launch {
    try {
        val lista = api.obterPosts()
        _posts.value = lista
    } catch (e: Exception) {
        // Tratar erro (falta de internet, 404...)
    }
}
```

---

## 🔐 Autenticação (JWT Tokens)

A maioria das APIs exige login.

* **Bearer Token**: Um código que você envia no Header. <!-- .element: class="fragment" -->
* **Interceptor**: Adiciona o token em TODAS as chamadas automaticamente. <!-- .element: class="fragment" -->

<!-- .slide: data-background-color="#002d04" -->

---

## 🆚 Android vs iOS (Rede)

| Recurso | Android (Retrofit) | iOS (URLSession) |
| :--- | :--- | :--- |
| **Linguagem** | Interface + Annotations | Native Classes / URLRequest |
| **Conversão** | Gson / Moshi | Codable |
| **Async** | Coroutines (suspend) | Async / Await |

---

## 🌐 Permissão de Internet

No `AndroidManifest.xml`:

```xml
<uses-permission android:name="android.permission.INTERNET" />
```

> Esqueceu? O App crasha com **SecurityException**. 💥 <!-- .element: class="fragment" -->

---

## 🛠️ Ferramentas de Apoio

* **Postman / Insomnia**: Teste sua API antes de codar. <!-- .element: class="fragment" -->
* **JSON Placeholder**: APIs falsas gratuitas para teste. <!-- .element: class="fragment" -->
* **QuickType.io**: Gera a Data Class Kotlin direto do JSON. <!-- .element: class="fragment" -->

---

## 🧪 Desafio da Aula: App de Repositórios

1. Use a API pública do GitHub: `https://api.github.com/users/{seuUser}/repos`. <!-- .element: class="fragment" -->
2. Crie a Data Class e a Interface. <!-- .element: class="fragment" -->
3. Exiba o nome dos seus repositórios em uma `RecyclerView`. <!-- .element: class="fragment" -->

---

## ⚠️ Cuidado com o Main Thread

O Android não permite rede na Main Thread.
Sempre use `viewModelScope.launch` ou troque o Dispatcher para `Dispatchers.IO`.

---

## 🏁 Conclusão

* APIs conectam seu app ao mundo. <!-- .element: class="fragment" -->
* Retrofit + Gson = Produtividade máxima. <!-- .element: class="fragment" -->
* Atenção às permissões e erros de rede. <!-- .element: class="fragment" -->

---

## ❓ Perguntas sobre Internet?

---

### Próxima Aula: Threads e Coroutines! 🧵👋
