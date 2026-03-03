# Aula 08 - Persistência de Dados 💾

<!-- .slide: data-transition="slide" -->

---

## 💾 Onde guardamos os dados?

Apps precisam lembrar das coisas quando fechados.

* Configurações simples. <!-- .element: class="fragment" -->
* Listas complexas. <!-- .element: class="fragment" -->
* Arquivos multimídia. <!-- .element: class="fragment" -->

---

## 1. SharedPreferences 🔑

A forma mais simples: Chave e Valor.

* "nome" -> "Ricardo" <!-- .element: class="fragment" -->
* "notificacoes_on" -> true <!-- .element: class="fragment" -->
* "tema" -> 1 <!-- .element: class="fragment" -->

---

### Usando PreferenceManager

```kotlin
val prefs = getSharedPreferences("config", MODE_PRIVATE)

// Gravar
prefs.edit().putString("USER", "Android").apply()

// Ler
val user = prefs.getString("USER", "Ninguém")
```

> **Atenção**: Não use para dados grandes ou listas!

---

## 🏛️ Banco de Dados: SQLite

O Android tem o SQLite no seu coração.

* Banco Relacional. <!-- .element: class="fragment" -->
* Leve e embutido. <!-- .element: class="fragment" -->
* Mas... o código puro é horrível (SQL strings). <!-- .element: class="fragment" -->

---

## 🔨 Conheça o ROOM

A biblioteca do Jetpack que salva vidas.

1. **Entity**: Sua tabela (Classe de dados). <!-- .element: class="fragment" -->
2. **DAO**: Seus comandos (Queries). <!-- .element: class="fragment" -->
3. **Database**: O gerente do banco. <!-- .element: class="fragment" -->

<!-- .slide: data-transition="convex" -->

---

### Passo 1: A Entidade (@Entity)

```kotlin
@Entity
data class User(
    @PrimaryKey val id: Int,
    val name: String
)
```

---

### Passo 2: O DAO (@Dao)

```kotlin
@Dao
interface UserDao {
    @Insert
    void save(User user)

    @Query("SELECT * FROM User")
    LiveData<List<User>> getAll()
}
```

---

## 🧵 A Regra de Ouro do Banco

**NUNCA** acesse o banco na Main Thread.

* O Room vai travar seu app (Crash) se você tentar. <!-- .element: class="fragment" -->
* Use **Coroutines** ou **LiveData**. <!-- .element: class="fragment" -->
* Por que? Porque ler o disco é lento e trava a tela. <!-- .element: class="fragment" -->

---

## 🧬 Ciclo Completo: MVVM + Room

```mermaid
graph TD
    UI[Activity/View] -->|Observa| VM[ViewModel]
    VM -->|Pede| REPO[Repository]
    REPO -->|Query| DB[(Room DB)]
    DB -->|Retorna| REPO
    REPO -->|State| VM
    VM -->|LiveData| UI
```

---

## 📂 Arquivos Externos

Para fotos e vídeos.

* **Cache**: Temporário. <!-- .element: class="fragment" -->
* **Arquivos Privados**: Só seu app vê. <!-- .element: class="fragment" -->
* **Arquivos Públicos**: Galeria, Downloads (Precisa de permissão). <!-- .element: class="fragment" -->

---

## 🆚 Persistência: Android vs iOS

| Recurso | Android | iOS |
| :---: | :---: | :--- |
| **Simples** | SharedPreferences | UserDefaults |
| **Banco** | Room (SQLite) | Core Data / SwiftData |
| **Arquivos** | Scoped Storage | Sandbox |

---

## 🕵️ Ferramenta: App Inspection

No Android Studio, você pode ver o banco de dados **ao vivo**.

1. Rode o app. <!-- .element: class="fragment" -->
2. Aba `App Inspection` -> `Database Inspector`. <!-- .element: class="fragment" -->
3. Você pode editar os dados e ver a tela do celular mudar! 🎩 <!-- .element: class="fragment" -->

<!-- .slide: data-background-color="#003049" -->

---

## 🛠️ Prática: Lista de Tarefas

Vamos criar um banco para salvar textos.

1. Configure o Room no `build.gradle`. <!-- .element: class="fragment" -->
2. Crie a Entity `Task`. <!-- .element: class="fragment" -->
3. Salve um texto vindo de um `EditText`. <!-- .element: class="fragment" -->

---

### Dica: O Singleton do Banco

Não crie várias instâncias do banco. Use o padrão **Singleton**.

```kotlin
val db = Room.databaseBuilder(
    applicationContext,
    AppDatabase::class.java, "database-name"
).build()
```

---

## 🏁 Conclusão

* Escolha a ferramenta certa para o dado certo. <!-- .element: class="fragment" -->
* Room é o padrão para dados estruturados. <!-- .element: class="fragment" -->
* Sempre use threads de background (IO). <!-- .element: class="fragment" -->

---

## ❓ Dúvidas sobre Dados?

---

### Próxima Aula: Listas com RecyclerView! 📋👋
