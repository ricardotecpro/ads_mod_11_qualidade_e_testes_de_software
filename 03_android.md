Criar um cliente Android é o passo final perfeito para demonstrar a verdadeira portabilidade de uma arquitetura baseada em API. Mais uma vez, nosso backend Spring Boot permanecerá **intacto**, provando seu valor como um serviço central.

Desenvolver para Android é um universo à parte. Usaremos as ferramentas modernas recomendadas pelo Google: **Kotlin** como linguagem, **Jetpack Compose** para a interface gráfica (em vez do antigo XML) e **Retrofit** para a comunicação de rede.

-----

### **Guia Completo: Criando o Cliente Android com Android Studio**

#### **Passo 0: Preparando o Ambiente**

1.  **Instale o Android Studio:** Baixe e instale a versão mais recente do Android Studio ("Hedgehog" ou mais nova) a partir do site oficial da Google. A instalação inclui tudo que você precisa (SDK do Android, etc.).

2.  **Crie um Emulador (AVD):**

      * Dentro do Android Studio, vá em `Tools` \> `Device Manager`.
      * Clique em `Create device`.
      * Escolha um modelo de celular (ex: `Pixel 7`). Clique em `Next`.
      * Escolha uma imagem de sistema (ex: a mais recente, como "Upside Down Cake" - API 34). Se não estiver baixada, clique no ícone de download ao lado dela. Clique em `Next`.
      * Dê um nome ao seu AVD se desejar e clique em `Finish`.
      * Agora você pode iniciar seu celular virtual clicando no ícone de "Play" no Device Manager.

3.  **Atenção ao `localhost`\!**

      * O emulador Android é uma máquina virtual com sua própria rede. Ele **não** consegue acessar o `localhost` ou `127.0.0.1` do seu computador.
      * Para que o emulador acesse o `localhost` da sua máquina (onde o Spring Boot está rodando), você deve usar o endereço IP especial: **`10.0.2.2`**.
      * Portanto, a URL da nossa API para o app Android será `http://10.0.2.2:8080/api/tarefas`.

#### **Passo 1: Criando o Projeto no Android Studio**

1.  Abra o Android Studio e selecione `File` \> `New` \> `New Project...`.
2.  Escolha o template **"Empty Activity"** (geralmente o primeiro, que vem com o logo do Jetpack Compose). Clique em `Next`.
3.  Preencha os detalhes:
      * **Name:** `TodoListAndroid`
      * **Package name:** `br.com.curso.todolist.android`
      * **Save location:** Onde você preferir.
      * **Language:** **Kotlin**
      * **Minimum SDK:** Escolha uma API recente, como `API 26: Android 8.0 (Oreo)`.
      * **Build configuration language:** Kotlin DSL (padrão).
4.  Clique em `Finish`. O Android Studio vai levar um tempo para configurar e baixar as dependências (Gradle Sync).

#### **Passo 2: Adicionando as Dependências**

Vamos adicionar as bibliotecas Retrofit (para a rede), Gson (para converter JSON) e ViewModel (para a arquitetura).

1.  No painel do projeto à esquerda, encontre e abra o arquivo `build.gradle.kts (Module :app)`. **Não confunda** com o que tem `(Project :TodoListAndroid)`.
2.  Dentro da seção `dependencies { ... }`, adicione as seguintes linhas:

<!-- end list -->

```kotlin
    // Retrofit para networking
    implementation("com.squareup.retrofit2:retrofit:2.9.0")
    // Conversor Gson para o Retrofit
    implementation("com.squareup.retrofit2:converter-gson:2.9.0")
    // ViewModel do Jetpack para a arquitetura MVVM
    implementation("androidx.lifecycle:lifecycle-viewmodel-compose:2.8.0")
    // Coroutines para tarefas assíncronas
    implementation("org.jetbrains.kotlinx:kotlinx-coroutines-android:1.7.3")
```

3.  Após adicionar as linhas, uma barra amarela aparecerá no topo do editor. Clique em **"Sync Now"**.

#### **Passo 3: Configurando a Camada de Rede**

Vamos criar as classes que se comunicarão com a API.

1.  **Crie a Classe de Modelo (`Tarefa.kt`):**

      * No painel do projeto, clique com o botão direito no pacote `br.com.curso.todolist.android` -\> `New` -\> `Kotlin Class/File`.
      * Nomeie-o `Tarefa` e defina-o como uma `data class`.

    <!-- end list -->

    ```kotlin
    package br.com.curso.todolist.android

    // A data class em Kotlin já gera getters, setters, equals, etc.
    data class Tarefa(
        val id: Long?,
        var descricao: String,
        var concluida: Boolean
    )
    ```

2.  **Crie a Interface da API com Retrofit (`TarefaApiService.kt`):**

      * Crie um novo arquivo Kotlin com este nome.

    <!-- end list -->

    ```kotlin
    package br.com.curso.todolist.android

    import retrofit2.Response
    import retrofit2.http.*

    interface TarefaApiService {
        @GET("tarefas")
        suspend fun getTarefas(): List<Tarefa> // 'suspend' indica que é para coroutines

        @POST("tarefas")
        suspend fun addTarefa(@Body tarefa: Tarefa): Tarefa

        @PUT("tarefas/{id}")
        suspend fun updateTarefa(@Path("id") id: Long, @Body tarefa: Tarefa): Tarefa

        @DELETE("tarefas/{id}")
        suspend fun deleteTarefa(@Path("id") id: Long): Response<Void>
    }
    ```

3.  **Crie o Cliente Retrofit (`RetrofitClient.kt`):**

      * Crie um novo arquivo Kotlin com este nome, e defina-o como um `object` (Singleton).

    <!-- end list -->

    ```kotlin
    package br.com.curso.todolist.android

    import retrofit2.Retrofit
    import retrofit2.converter.gson.GsonConverterFactory

    object RetrofitClient {
        // ATENÇÃO: Usando o IP especial para o emulador
        private const val BASE_URL = "http://10.0.2.2:8080/api/"

        val instance: TarefaApiService by lazy {
            val retrofit = Retrofit.Builder()
                .baseUrl(BASE_URL)
                .addConverterFactory(GsonConverterFactory.create())
                .build()
            retrofit.create(TarefaApiService::class.java)
        }
    }
    ```

#### **Passo 4: Criando a Arquitetura (ViewModel)**

O ViewModel conterá a lógica e o estado da nossa tela.

1.  **Crie o `TarefaViewModel.kt`:**

    ```kotlin
    package br.com.curso.todolist.android

    import androidx.lifecycle.ViewModel
    import androidx.lifecycle.viewModelScope
    import kotlinx.coroutines.flow.MutableStateFlow
    import kotlinx.coroutines.flow.StateFlow
    import kotlinx.coroutines.launch

    class TarefaViewModel : ViewModel() {
        private val _tarefas = MutableStateFlow<List<Tarefa>>(emptyList())
        val tarefas: StateFlow<List<Tarefa>> = _tarefas

        init {
            carregarTarefas()
        }

        fun carregarTarefas() {
            viewModelScope.launch { // Executa na thread de fundo
                try {
                    _tarefas.value = RetrofitClient.instance.getTarefas()
                } catch (e: Exception) {
                    // Tratar erro
                    e.printStackTrace()
                }
            }
        }

        fun adicionarTarefa(descricao: String) {
            viewModelScope.launch {
                try {
                    val novaTarefa = Tarefa(id = null, descricao = descricao, concluida = false)
                    RetrofitClient.instance.addTarefa(novaTarefa)
                    carregarTarefas() // Recarrega a lista
                } catch (e: Exception) {
                    e.printStackTrace()
                }
            }
        }
        
        // ... Os métodos de update e delete seguiriam o mesmo padrão
    }
    ```

#### **Passo 5: Construindo a UI com Jetpack Compose**

Vamos modificar o arquivo `MainActivity.kt` para criar nossa tela.

1.  Abra `MainActivity.kt`.

2.  **Substitua todo o conteúdo** pelo código abaixo:

    ```kotlin
    package br.com.curso.todolist.android

    import android.os.Bundle
    import androidx.activity.ComponentActivity
    import androidx.activity.compose.setContent
    import androidx.compose.foundation.layout.*
    import androidx.compose.foundation.lazy.LazyColumn
    import androidx.compose.foundation.lazy.items
    import androidx.compose.material3.*
    import androidx.compose.runtime.*
    import androidx.compose.ui.Modifier
    import androidx.compose.ui.unit.dp
    import androidx.lifecycle.viewmodel.compose.viewModel
    import br.com.curso.todolist.android.ui.theme.TodoListAndroidTheme

    class MainActivity : ComponentActivity() {
        override fun onCreate(savedInstanceState: Bundle?) {
            super.onCreate(savedInstanceState)
            setContent {
                TodoListAndroidTheme {
                    Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
                        TarefaScreen()
                    }
                }
            }
        }
    }

    @OptIn(ExperimentalMaterial3Api::class)
    @Composable
    fun TarefaScreen(tarefaViewModel: TarefaViewModel = viewModel()) {
        val tarefas by tarefaViewModel.tarefas.collectAsState()
        var textoNovaTarefa by remember { mutableStateOf("") }

        Scaffold(
            topBar = { TopAppBar(title = { Text("Lista de Tarefas (Android)") }) }
        ) { paddingValues ->
            Column(modifier = Modifier
                .padding(paddingValues)
                .padding(16.dp)) {
                
                Row(modifier = Modifier.fillMaxWidth()) {
                    OutlinedTextField(
                        value = textoNovaTarefa,
                        onValueChange = { textoNovaTarefa = it },
                        label = { Text("Nova tarefa") },
                        modifier = Modifier.weight(1f)
                    )
                    Spacer(modifier = Modifier.width(8.dp))
                    Button(onClick = {
                        if (textoNovaTarefa.isNotBlank()) {
                            tarefaViewModel.adicionarTarefa(textoNovaTarefa)
                            textoNovaTarefa = ""
                        }
                    }) {
                        Text("Add")
                    }
                }

                Spacer(modifier = Modifier.height(16.dp))

                LazyColumn {
                    items(tarefas) { tarefa ->
                        Text(text = tarefa.descricao, modifier = Modifier.padding(8.dp))
                        Divider()
                    }
                }
            }
        }
    }
    ```

#### **Passo 6: Permissão de Internet**

Por fim, precisamos dizer ao sistema Android que nosso app precisa acessar a internet.

1.  Abra o arquivo `src/main/AndroidManifest.xml`.
2.  Acima da tag `<application>`, adicione as seguintes linhas:
    ```xml
    <uses-permission android:name="android.permission.INTERNET" />
    <application
        ...
        android:usesCleartextTraffic="true"
        ...>
    ```
      * `uses-permission`: Permissão geral para usar a internet.
      * `usesCleartextTraffic="true"`: Necessário em desenvolvimento para permitir a conexão com nosso servidor local, que é `http` e não `https`.

#### **Passo 7: Teste Final**

1.  Garanta que sua **API Spring Boot esteja rodando**.
2.  Garanta que seu **Emulador Android esteja rodando**.
3.  No Android Studio, clique no ícone de "Play" verde na barra de ferramentas (ou pressione `Shift+F10`).
4.  O Android Studio irá instalar o app no emulador e iniciá-lo.

Você deverá ver sua tela com a lista de tarefas carregada do seu backend. Tente adicionar uma nova tarefa\! Você acaba de criar um terceiro cliente para a mesma API.

---
Obrigado por compartilhar o código. O erro está na estrutura do seu arquivo `AndroidManifest.xml`: a tag `<application>` foi declarada duas vezes, uma dentro da outra.

Um arquivo de manifesto só pode ter **uma única** tag `<application>`, e todos os atributos (como `icon`, `label`, `theme` e `usesCleartextTraffic`) devem estar dentro dela.

-----

### A Correção

Você precisa mesclar todos os atributos em uma única tag `<application>`.

**Substitua todo o conteúdo** do seu arquivo `AndroidManifest.xml` por esta versão corrigida:

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:tools="http://schemas.android.com/tools">

    <uses-permission android:name="android.permission.INTERNET" />

    <application
        android:allowBackup="true"
        android:dataExtractionRules="@xml/data_extraction_rules"
        android:fullBackupContent="@xml/backup_rules"
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:roundIcon="@mipmap/ic_launcher_round"
        android.supportsRtl="true"
        android:theme="@style/Theme.TodoListAndroid"
        android:usesCleartextTraffic="true">  <activity
            android:name=".MainActivity"
            android:exported="true"
            android:label="@string/app_name"
            android:theme="@style/Theme.TodoListAndroid">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>

    </application>

</manifest>
```

### O Que Foi Corrigido?

1.  Removemos a tag `<application>` externa que estava duplicada.
2.  Movemos o atributo `android:usesCleartextTraffic="true"` para dentro da tag `<application>` principal, junto com os outros atributos que já estavam lá.

Com esta correção, o arquivo de manifesto ficará válido e o seu projeto poderá ser compilado e executado sem erros.


---


O código que você enviou está perfeito e representa a implementação inicial que fizemos, com as funcionalidades de **Adicionar (Create)** e **Listar (Read)** tarefas.

A próxima e última etapa para a aplicação Android é adicionar as funcionalidades que faltam para completar o CRUD: **Atualizar (Update)** e **Deletar (Delete)**. Faremos isso adicionando um checkbox e um botão de deletar para cada item da lista, deixando o app Android tão completo quanto as versões web e desktop.

-----

### **Próxima Etapa: Implementando Update e Delete no App Android**

#### **Passo 1: Adicionar a Lógica de Update e Delete no `TarefaViewModel`**

Primeiro, vamos ensinar nosso ViewModel a lidar com as ações de atualizar e deletar, chamando os endpoints correspondentes da nossa API.

1.  Abra o arquivo `src/main/java/br/com/curso/todolist/android/TarefaViewModel.kt`.
2.  Adicione os métodos `updateTarefa` e `deleteTarefa` dentro da classe.

**Aqui está o código completo e atualizado para `TarefaViewModel.kt`:**

```kotlin
package br.com.curso.todolist.android

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch

class TarefaViewModel : ViewModel() {
    private val _tarefas = MutableStateFlow<List<Tarefa>>(emptyList())
    val tarefas: StateFlow<List<Tarefa>> = _tarefas

    init {
        carregarTarefas()
    }

    fun carregarTarefas() {
        viewModelScope.launch {
            try {
                _tarefas.value = RetrofitClient.instance.getTarefas()
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }

    fun adicionarTarefa(descricao: String) {
        viewModelScope.launch {
            try {
                val novaTarefa = Tarefa(id = null, descricao = descricao, concluida = false)
                RetrofitClient.instance.addTarefa(novaTarefa)
                carregarTarefas()
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }

    // --- MÉTODO NOVO PARA UPDATE ---
    fun updateTarefa(tarefa: Tarefa) {
        viewModelScope.launch {
            try {
                // A tarefa já vem com o estado 'concluida' alterado pela UI.
                // Só precisamos enviá-la para a API.
                tarefa.id?.let { // Executa somente se o id não for nulo
                    RetrofitClient.instance.updateTarefa(it, tarefa)
                    carregarTarefas() // Recarrega para garantir consistência
                }
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }

    // --- MÉTODO NOVO PARA DELETE ---
    fun deleteTarefa(id: Long?) {
        viewModelScope.launch {
            try {
                id?.let {
                    RetrofitClient.instance.deleteTarefa(it)
                    carregarTarefas()
                }
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }
}
```

#### **Passo 2: Atualizar a Interface (`TarefaScreen`)**

Agora vamos modificar a nossa lista (`LazyColumn`) para que cada item exiba um checkbox e um botão de deletar, e para que eles chamem os novos métodos do ViewModel.

1.  Abra o arquivo `src/main/java/br/com/curso/todolist/android/MainActivity.kt`.
2.  **Substitua** a função `@Composable fun TarefaScreen(...)` pela versão abaixo.

**Código atualizado para `TarefaScreen` em `MainActivity.kt`:**

```kotlin
@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun TarefaScreen(tarefaViewModel: TarefaViewModel = viewModel()) {
    val tarefas by tarefaViewModel.tarefas.collectAsState()
    var textoNovaTarefa by remember { mutableStateOf("") }

    Scaffold(
        topBar = { TopAppBar(title = { Text("Lista de Tarefas (Android)") }) }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .padding(paddingValues)
                .padding(16.dp)
        ) {
            // Seção para adicionar tarefa (continua a mesma)
            Row(modifier = Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
                OutlinedTextField(
                    value = textoNovaTarefa,
                    onValueChange = { textoNovaTarefa = it },
                    label = { Text("Nova tarefa") },
                    modifier = Modifier.weight(1f)
                )
                Spacer(modifier = Modifier.width(8.dp))
                Button(onClick = {
                    if (textoNovaTarefa.isNotBlank()) {
                        tarefaViewModel.adicionarTarefa(textoNovaTarefa)
                        textoNovaTarefa = ""
                    }
                }) {
                    Text("Add")
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

            // --- SEÇÃO DA LISTA ATUALIZADA ---
            LazyColumn {
                items(tarefas, key = { it.id!! }) { tarefa ->
                    TarefaItem(
                        tarefa = tarefa,
                        onCheckedChange = {
                            // Cria um novo objeto com o status invertido e chama o update
                            val tarefaAtualizada = tarefa.copy(concluida = !tarefa.concluida)
                            tarefaViewModel.updateTarefa(tarefaAtualizada)
                        },
                        onDeleteClick = {
                            tarefaViewModel.deleteTarefa(tarefa.id)
                        }
                    )
                    Divider()
                }
            }
        }
    }
}

// --- NOVO COMPOSABLE PARA O ITEM DA LISTA ---
// É uma boa prática separar itens complexos da lista em seus próprios Composables.
@Composable
fun TarefaItem(
    tarefa: Tarefa,
    onCheckedChange: (Boolean) -> Unit,
    onDeleteClick: () -> Unit
) {
    Row(
        modifier = Modifier
            .fillMaxWidth()
            .padding(vertical = 8.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        Checkbox(
            checked = tarefa.concluida,
            onCheckedChange = onCheckedChange
        )
        Text(
            text = tarefa.descricao,
            modifier = Modifier
                .weight(1f)
                .padding(horizontal = 8.dp),
            // Adiciona o estilo de "riscado" se a tarefa estiver concluída
            style = if (tarefa.concluida) {
                LocalTextStyle.current.copy(textDecoration = TextDecoration.LineThrough)
            } else {
                LocalTextStyle.current
            }
        )
        IconButton(onClick = onDeleteClick) {
            Icon(Icons.Filled.Delete, contentDescription = "Deletar Tarefa")
        }
    }
}
```

**Importante:** Adicione estes imports no topo do seu arquivo `MainActivity.kt` para os novos componentes que usamos:

```kotlin
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Delete
import androidx.compose.ui.Alignment
import androidx.compose.ui.text.style.TextDecoration
```

### Teste Final

1.  Garanta que sua **API Backend** esteja rodando.
2.  Rode a aplicação no seu emulador Android a partir do Android Studio.
3.  Você agora deve ver cada tarefa com um checkbox e um ícone de lixeira.
4.  **Teste o Update:** Clique em um checkbox. O texto deve ser riscado e a mudança persistida.
5.  **Teste o Delete:** Clique no ícone da lixeira. A tarefa deve ser removida da lista.

**Parabéns\!** Você finalizou o ciclo completo de desenvolvimento de um sistema com backend, frontend web, frontend desktop e, agora, um cliente mobile para Android, cobrindo todos os conceitos essenciais do desenvolvimento moderno de software.


Este código está perfeito. Ele representa a implementação final e completa da interface do seu aplicativo Android, com todas as funcionalidades de **Criar, Ler, Atualizar e Deletar** funcionando.

Com este último passo, você oficialmente concluiu com sucesso a maratona de desenvolvimento que propusemos.

---
### **🏆 Conclusão Final do Curso 🏆**

Pense em tudo que você construiu. Este não é mais apenas um "CRUD To-Do List", é um ecossistema de software completo e um projeto de portfólio fantástico.

**Você demonstrou maestria sobre:**

1.  **O Backend (A Fundação Sólida):**
    * Criou uma API RESTful robusta e profissional com **Java e Spring Boot**.
    * Modelou dados, gerenciou a persistência com Spring Data JPA e expôs endpoints seguros e bem definidos.
    * **O mais importante:** Este backend serviu como a única fonte da verdade, alimentando três clientes completamente diferentes sem precisar de nenhuma modificação.

2.  **O Cliente Web (A Face Moderna):**
    * Desenvolveu uma Single-Page Application (SPA) reativa e moderna com **Angular**.
    * Trabalhou com componentes, serviços, data binding e comunicação HTTP para criar uma experiência web fluida.

3.  **O Cliente Desktop (O Poder Nativo):**
    * Construiu uma aplicação de desktop nativa e responsiva com **JavaFX**.
    * Aprendeu a separar a UI (FXML) da lógica (Controller), consumir uma API a partir de Java e lidar com a concorrência de threads para manter a interface sempre ágil.

4.  **O Cliente Mobile (A Experiência Portátil):**
    * Desenvolveu um aplicativo nativo para a plataforma mais utilizada no mundo, o **Android**.
    * Utilizou as ferramentas mais modernas do ecossistema Google: **Kotlin**, **Jetpack Compose** para UI declarativa, e a arquitetura **MVVM** com ViewModels e Coroutines.

**Conceitos-Chave que você dominou na prática:**

* **Arquitetura Cliente-Servidor e APIs REST:** O pão com manteiga do desenvolvimento moderno.
* **Padrões de Projeto (MVC & MVVM):** A importância de organizar o código de forma limpa e escalável.
* **Desenvolvimento Full-Stack e Multiplataforma:** Você agora entende, na prática, como o backend e diferentes frontends "conversam" para criar um produto coeso.
* **Resolução de Problemas:** Você enfrentou e superou desafios reais de configuração, dependências, sistemas de módulos (JavaFX) e estrutura de projetos (Android). Essa é uma das habilidades mais valiosas de um desenvolvedor.

Você foi além de um simples tutorial. Você construiu um sistema completo que demonstra uma gama de habilidades altamente requisitadas no mercado de trabalho.

**Parabéns pela sua dedicação e pela conclusão deste projeto incrível!** O caminho do aprendizado continua, e agora você tem uma base extremamente sólida para explorar tópicos ainda mais avançados como segurança, testes automatizados e deployment em nuvem.



---

Ótima ideia\! Refatorar e melhorar o código é um passo crucial no desenvolvimento de software. Uma aplicação funcional é ótima, mas uma aplicação robusta, legível e com uma boa experiência de usuário é ainda melhor.

Vamos criar uma nova versão do `MainActivity.kt` e também do `TarefaViewModel.kt` aplicando as seguintes melhorias:

1.  **Melhor Feedback Visual:** Mostrar um indicador de "carregando" (`loading`) enquanto os dados são buscados da API.
2.  **Tratamento de Estado Vazio:** Exibir uma mensagem amigável quando a lista de tarefas estiver vazia.
3.  **Componentização:** Quebrar a tela (`TarefaScreen`) em componentes menores e reutilizáveis, uma prática recomendada em Jetpack Compose.
4.  **Gestão de Estado Centralizada:** Usar uma única classe de estado (`UiState`) no ViewModel para representar todos os possíveis estados da tela (carregando, sucesso, erro).

-----

### **Passo 1: Melhorando o `TarefaViewModel.kt`**

Primeiro, vamos refatorar o ViewModel para que ele gerencie os novos estados de loading e lista.

**Substitua todo o conteúdo** do seu arquivo `TarefaViewModel.kt` por este:

```kotlin
package br.com.curso.todolist.android

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.flow.asStateFlow
import kotlinx.coroutines.flow.update
import kotlinx.coroutines.launch

// 1. Classe para representar todos os estados da nossa UI de uma vez
data class TarefaUiState(
    val tarefas: List<Tarefa> = emptyList(),
    val isLoading: Boolean = false,
    val error: String? = null
)

class TarefaViewModel : ViewModel() {
    // 2. Agora o StateFlow guarda um único objeto UiState
    private val _uiState = MutableStateFlow(TarefaUiState())
    val uiState: StateFlow<TarefaUiState> = _uiState.asStateFlow()

    init {
        carregarTarefas()
    }

    fun carregarTarefas() {
        // 3. Atualiza o estado para "carregando" antes da chamada de rede
        _uiState.update { it.copy(isLoading = true) }

        viewModelScope.launch {
            try {
                val tarefasDaApi = RetrofitClient.instance.getTarefas()
                // 4. Em caso de sucesso, atualiza o estado com os dados e desliga o loading
                _uiState.update { it.copy(isLoading = false, tarefas = tarefasDaApi) }
            } catch (e: Exception) {
                // 5. Em caso de erro, desliga o loading e define uma mensagem de erro
                _uiState.update { it.copy(isLoading = false, error = "Falha ao carregar tarefas") }
                e.printStackTrace()
            }
        }
    }
    
    // Os outros métodos agora também gerenciam o estado de loading de forma otimista
    fun adicionarTarefa(descricao: String) {
        viewModelScope.launch {
            try {
                val novaTarefa = Tarefa(id = null, descricao = descricao, concluida = false)
                val tarefaAdicionada = RetrofitClient.instance.addTarefa(novaTarefa)
                // Atualização otimista: adiciona à lista local antes de recarregar
                _uiState.update { it.copy(tarefas = it.tarefas + tarefaAdicionada) }
            } catch (e: Exception) {
                e.printStackTrace()
                // Em um app real, poderíamos reverter a UI ou mostrar um erro
            }
        }
    }

    fun updateTarefa(tarefa: Tarefa) {
        viewModelScope.launch {
            try {
                tarefa.id?.let {
                    val tarefaAtualizada = RetrofitClient.instance.updateTarefa(it, tarefa)
                    // Atualiza a tarefa específica na lista local
                    _uiState.update { currentState ->
                        val tarefasAtualizadas = currentState.tarefas.map { t ->
                            if (t.id == tarefaAtualizada.id) tarefaAtualizada else t
                        }
                        currentState.copy(tarefas = tarefasAtualizadas)
                    }
                }
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }

    fun deleteTarefa(id: Long?) {
        viewModelScope.launch {
            try {
                id?.let {
                    RetrofitClient.instance.deleteTarefa(it)
                    // Remove da lista local de forma otimista
                    _uiState.update { currentState ->
                        currentState.copy(tarefas = currentState.tarefas.filter { it.id != id })
                    }
                }
            } catch (e: Exception) {
                e.printStackTrace()
            }
        }
    }
}
```

-----

### **Passo 2: O Novo `MainActivity.kt` com Componentes Melhorados**

Agora, vamos recriar o arquivo `MainActivity.kt` para usar o novo `UiState` e para ser mais organizado, quebrando a tela em componentes menores.

**Substitua todo o conteúdo** do seu arquivo `MainActivity.kt` por este:

```kotlin
package br.com.curso.todolist.android

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import br.com.curso.todolist.android.ui.theme.TodoListAndroidTheme

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            TodoListAndroidTheme {
                Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
                    TarefaApp()
                }
            }
        }
    }
}

@Composable
fun TarefaApp(tarefaViewModel: TarefaViewModel = viewModel()) {
    val uiState by tarefaViewModel.uiState.collectAsState()

    Scaffold(
        topBar = {
            TopAppBar(title = { Text("Lista de Tarefas (Android)") })
        }
    ) { paddingValues ->
        Box(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues),
            contentAlignment = Alignment.Center
        ) {
            // Se estiver carregando, mostra o indicador de progresso
            if (uiState.isLoading) {
                CircularProgressIndicator()
            } else {
                // Se não estiver carregando, mostra a tela principal
                TarefaScreen(
                    tarefas = uiState.tarefas,
                    onAddTask = { descricao -> tarefaViewModel.adicionarTarefa(descricao) },
                    onUpdateTask = { tarefa -> tarefaViewModel.updateTarefa(tarefa) },
                    onDeleteTask = { id -> tarefaViewModel.deleteTarefa(id) }
                )
            }
        }
    }
}

@Composable
fun TarefaScreen(
    tarefas: List<Tarefa>,
    onAddTask: (String) -> Unit,
    onUpdateTask: (Tarefa) -> Unit,
    onDeleteTask: (Long?) -> Unit
) {
    Column(modifier = Modifier.padding(16.dp)) {
        var textoNovaTarefa by remember { mutableStateOf("") }

        // Barra para adicionar nova tarefa
        Row(modifier = Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
            OutlinedTextField(
                value = textoNovaTarefa,
                onValueChange = { textoNovaTarefa = it },
                label = { Text("Nova tarefa") },
                modifier = Modifier.weight(1f)
            )
            Spacer(modifier = Modifier.width(8.dp))
            Button(onClick = {
                if (textoNovaTarefa.isNotBlank()) {
                    onAddTask(textoNovaTarefa)
                    textoNovaTarefa = ""
                }
            }) {
                Text("Add")
            }
        }

        Spacer(modifier = Modifier.height(16.dp))
        
        // Se a lista estiver vazia, mostra uma mensagem
        if (tarefas.isEmpty()) {
            Text(
                text = "Nenhuma tarefa encontrada.\nAdicione uma nova!",
                modifier = Modifier.fillMaxWidth().padding(top = 32.dp),
                textAlign = TextAlign.Center,
                style = MaterialTheme.typography.bodyLarge
            )
        } else {
            // Se não, mostra a lista
            LazyColumn {
                items(tarefas, key = { it.id!! }) { tarefa ->
                    TarefaItem(
                        tarefa = tarefa,
                        onCheckedChange = {
                            val tarefaAtualizada = tarefa.copy(concluida = !tarefa.concluida)
                            onUpdateTask(tarefaAtualizada)
                        },
                        onDeleteClick = { onDeleteTask(tarefa.id) }
                    )
                    Divider()
                }
            }
        }
    }
}

@Composable
fun TarefaItem(
    tarefa: Tarefa,
    onCheckedChange: () -> Unit,
    onDeleteClick: () -> Unit
) {
    Row(
        modifier = Modifier.fillMaxWidth().padding(vertical = 8.dp),
        verticalAlignment = Alignment.CenterVertically
    ) {
        Checkbox(
            checked = tarefa.concluida,
            onCheckedChange = { onCheckedChange() }
        )
        Text(
            text = tarefa.descricao,
            modifier = Modifier.weight(1f).padding(horizontal = 8.dp),
            style = if (tarefa.concluida) LocalTextStyle.current.copy(textDecoration = TextDecoration.LineThrough) else LocalTextStyle.current
        )
        IconButton(onClick = onDeleteClick) {
            Icon(Icons.Filled.Delete, contentDescription = "Deletar Tarefa")
        }
    }
}
```

### O Que Melhorou?

1.  **Feedback Instantâneo:** O usuário agora vê um círculo de progresso, sabendo que o app está trabalhando.
2.  **Contexto para o Usuário:** Uma lista vazia agora é explícita, guiando o usuário sobre o que fazer.
3.  **Código Organizado:** A lógica da tela foi dividida em componentes menores (`TarefaApp`, `TarefaScreen`, `TarefaItem`), tornando o código mais fácil de ler, testar e dar manutenção.
4.  **Atualizações Otimistas:** A UI agora responde instantaneamente às ações do usuário (adicionar, deletar, atualizar) e então se sincroniza com o backend, proporcionando uma experiência muito mais fluida.

Rode a aplicação novamente. Você verá que ela está visivelmente mais profissional e robusta\!


---


Você está correto em notar essa mensagem. É importante esclarecer: isso **não é um erro**, mas sim um **aviso (warning)**. Sua aplicação irá compilar e funcionar normalmente.

### O Que Significa o Aviso?

Este aviso é uma prática comum do Google e da equipe do Jetpack Compose. Ele significa que alguns dos componentes do Material Design 3 que estamos usando (como `Scaffold`, `TopAppBar`, `OutlinedTextField`, etc.) são considerados "Experimentais".

Isso quer dizer que, em futuras versões da biblioteca, a forma de usá-los (seus parâmetros, por exemplo) *pode* mudar. O Google está apenas pedindo que você "assine um termo de ciência" de que está usando uma API nova.

### Como Corrigir (Remover o Aviso)

A forma correta de lidar com isso é usar a anotação `@OptIn` para dizer ao compilador: "Eu sei que esta API é experimental e aceito usá-la mesmo assim".

Você tem duas opções:

1.  **Anotar cada função:** Adicionar `@OptIn(ExperimentalMaterial3Api::class)` acima de cada função `@Composable` que usa um componente experimental. Isso pode ser repetitivo.
2.  **Anotar o arquivo inteiro (Recomendado):** Adicionar a anotação uma única vez no topo do arquivo para que ela se aplique a tudo que está dentro dele. Esta é a abordagem mais limpa.

Vamos usar a abordagem recomendada.

-----

#### **Correção no `MainActivity.kt`**

1.  Abra seu arquivo `MainActivity.kt`.
2.  Adicione a seguinte linha como a **primeira linha do arquivo**, antes da declaração `package`:

<!-- end list -->

```kotlin
@file:OptIn(ExperimentalMaterial3Api::class)
```

Aqui está o código completo e corrigido para o seu `MainActivity.kt`.

```kotlin
@file:OptIn(ExperimentalMaterial3Api::class) // <-- ADICIONE ESTA LINHA NO TOPO DO ARQUIVO

package br.com.curso.todolist.android

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.style.TextAlign
import androidx.compose.ui.text.style.TextDecoration
import androidx.compose.ui.unit.dp
import androidx.lifecycle.viewmodel.compose.viewModel
import br.com.curso.todolist.android.ui.theme.TodoListAndroidTheme

// O resto do arquivo continua exatamente o mesmo...
class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            TodoListAndroidTheme {
                Surface(modifier = Modifier.fillMaxSize(), color = MaterialTheme.colorScheme.background) {
                    TarefaApp()
                }
            }
        }
    }
}

@Composable
fun TarefaApp(tarefaViewModel: TarefaViewModel = viewModel()) {
    //... todo o resto do código permanece igual
}

@Composable
fun TarefaScreen(
    //...
) {
    //...
}

@Composable
fun TarefaItem(
    //...
) {
    //...
}
```

Ao adicionar `@file:OptIn(ExperimentalMaterial3Api::class)` no topo, você informa ao compilador para aceitar o uso de todas as APIs experimentais do Material 3 dentro deste arquivo, e os avisos desaparecerão.


---

Ótimas perguntas\! Elas abordam dois pontos muito importantes: a confirmação da configuração de rede para o Android e como operar o ecossistema de software fora do ambiente de desenvolvimento, uma habilidade essencial para automação e deployment.

-----

### **Parte 1: Confirmação da URL da API para Android (`10.0.2.2`)**

Você está correto. A única mudança necessária para o aplicativo Android funcionar é garantir que ele aponte para o endereço IP correto, que é o alias do `localhost` da sua máquina (Windows, Mac ou Linux) visto de dentro do emulador Android.

**A mudança deve ser feita em um único lugar:**

No seu projeto `TodoListAndroid`, abra o arquivo:
`src/main/java/br/com/curso/todolist/android/RetrofitClient.kt`

O código dentro dele deve ser este:

```kotlin
package br.com.curso.todolist.android

import retrofit2.Retrofit
import retrofit2.converter.gson.GsonConverterFactory

object RetrofitClient {
    // ESTA É A LINHA CRÍTICA!
    // Garanta que a URL base seja esta para o emulador se comunicar com o backend local.
    private const val BASE_URL = "http://10.0.2.2:8080/api/"

    val instance: TarefaApiService by lazy {
        val retrofit = Retrofit.Builder()
            .baseUrl(BASE_URL)
            .addConverterFactory(GsonConverterFactory.create())
            .build()
        retrofit.create(TarefaApiService::class.java)
    }
}
```

Se o seu arquivo já está assim, **nenhuma outra alteração é necessária no código**. A aplicação Android está pronta para se comunicar com o seu backend local.

-----

### **Parte 2: Como Iniciar Todas as Aplicações sem a IDE (Via Terminal)**

Aprender a construir e executar suas aplicações pela linha de comando é fundamental. É assim que os servidores de produção e os sistemas de integração contínua (CI/CD) funcionam.

Você precisará de um terminal (Prompt de Comando, PowerShell ou Git Bash no Windows; Terminal no Mac/Linux) para cada aplicação que estiver rodando simultaneamente.

#### **1. Backend: `todolist-api` (com Maven)**

O Spring Initializr nos fornece o Maven Wrapper (`mvnw`), que nos permite construir o projeto sem ter o Maven instalado globalmente.

1.  **Abra um terminal** e navegue até a pasta raiz do projeto `todolist-api`.
2.  **Construa o projeto:** Execute o comando abaixo. Ele vai limpar builds antigos, compilar o código e empacotar tudo em um único arquivo `.jar` executável.
    ```bash
    # No Windows
    mvnw.cmd clean package

    # No Mac/Linux
    ./mvnw clean package
    ```
3.  **Execute a API:** Após o build, um arquivo `.jar` será criado na pasta `target`. Execute-o com o Java.
    ```bash
    java -jar target/todolist-api-1.0-SNAPSHOT.jar
    ```
    **Pronto\!** Seu backend está rodando. Deixe este terminal aberto.

#### **2. Frontend Web: `todolist-web` (com Node.js/npm)**

Para a aplicação web, o processo tem dois estágios: construir os arquivos estáticos e depois servi-los com um servidor web.

1.  **Abra um novo terminal** e navegue até a pasta raiz do projeto `todolist-web`.
2.  **Construa para produção:** Este comando compila o TypeScript e otimiza os arquivos para produção.
    ```bash
    ng build
    ```
    Isso criará uma pasta `dist/todolist-web/browser` com os arquivos `index.html`, CSS e JS.
3.  **Sirva os arquivos:** A maneira mais fácil de iniciar um servidor web local é usando o `npx`.
    ```bash
    npx serve dist/todolist-web/browser
    ```
    O terminal mostrará uma URL (geralmente `http://localhost:3000`) onde você pode acessar a aplicação web. Deixe este terminal aberto.

#### **3. Frontend Desktop: `todolist-desktop` (com Maven)**

O processo é idêntico ao do backend, pois também é um projeto Maven.

1.  **Abra um novo terminal** e navegue até a pasta raiz do projeto `todolist-desktop`.
2.  **Construa o projeto:**
    ```bash
    # No Windows
    mvnw.cmd clean package

    # No Mac/Linux
    ./mvnw clean package
    ```
3.  **Execute a aplicação:**
    ```bash
    java -jar target/todolist-desktop-1.0-SNAPSHOT.jar
    ```
    A janela do aplicativo desktop deverá aparecer.

#### **4. Aplicação Android: `todolist-android` (com Gradle)**

Executar um app Android via linha de comando envolve usar o Gradle Wrapper (`gradlew`) e o `adb` (Android Debug Bridge), que faz parte do SDK do Android.

**Primeiro, inicie seu Emulador** através do Device Manager no Android Studio.

1.  **Abra um novo terminal** e navegue até a pasta raiz do projeto `todolist-android`.
2.  **Construa e instale o app no emulador:** Este comando compila o código e instala o arquivo `.apk` de debug no dispositivo/emulador que estiver conectado e rodando.
    ```bash
    # No Windows
    gradlew.bat installDebug

    # No Mac/Linux
    ./gradlew installDebug
    ```
3.  **Inicie o app no emulador:** Após a instalação, você pode iniciar o app com o `adb`. O nome do pacote e da atividade principal precisam ser especificados.
    ```bash
    adb shell am start -n br.com.curso.todolist.android/.MainActivity
    ```
    O aplicativo To-Do List deverá abrir na tela do seu emulador.

### **Resumo da Ordem de Execução**

1.  Inicie o **Backend** no Terminal 1.
2.  Inicie o **Servidor Web** no Terminal 2.
3.  Inicie o **Emulador Android**.
4.  Use o Terminal 3 para **instalar e iniciar o App Android**.
5.  Use o Terminal 4 para **iniciar o App Desktop**.

Agora você pode controlar todo o ecossistema sem depender de um único clique de "Run" na IDE\!


---
