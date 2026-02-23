# Aula 07 - Arquitetura MVVM 🏗️

<!-- .slide: data-transition="zoom" -->

---

## 🦸 O Problema da God Activity

Sua Activity faz tudo?
* Chama a internet. <!-- .element: class="fragment" -->
* Valida campos. <!-- .element: class="fragment" -->
* Salva no banco. <!-- .element: class="fragment" -->
* Desenha a tela. <!-- .element: class="fragment" -->

> Isso é um pesadelo de manutenção! 😱

---

## 📐 O Padrão MVVM

Recomendado pelo Google (Android Jetpack).

* **Model**: Dados e Lógica de Negócio. <!-- .element: class="fragment" -->
* **View**: UI (Activity/XML). Burra e Visual. <!-- .element: class="fragment" -->
* **ViewModel**: O cérebro. Faz a ponte entre os dois. <!-- .element: class="fragment" -->

---

### O Fluxo de Dados

```mermaid
graph LR
    V[View] -->|Ações| VM[ViewModel]
    VM -->|Observa| V
    VM <-->|Dados| M[Model/Repo]
```

---

## 🧠 O ViewModel

Seu maior superpoder: **Sobrevivência**.

* Quando você gira a tela, a Activity morre e renasce. <!-- .element: class="fragment" -->
* O ViewModel **permanece** vivo na memória. <!-- .element: class="fragment" -->
* Os dados não são perdidos! 💎 <!-- .element: class="fragment" -->

<!-- .slide: data-background-color="#1e1e24" -->

---

## 📡 LiveData

O mensageiro que respeita a vida.

* É um container de dados observável. <!-- .element: class="fragment" -->
* A View diz: "Me avise quando o dado mudar". <!-- .element: class="fragment" -->
* Se a View estiver em background, o LiveData espera ela voltar para avisar. <!-- .element: class="fragment" -->

---

### Exemplo de LiveData

```kotlin
// No ViewModel
val nome = MutableLiveData<String>()

fun carregar() {
    nome.value = "Ricardo"
}
```

```kotlin
// Na Activity
viewModel.nome.observe(this) { novoNome ->
    binding.txtNome.text = novoNome
}
```

---

## 🏗️ Camada Model & Repository

Não deixe o ViewModel saber de ONDE vêm os dados.

* O **Repository** decide: "Vou buscar na Internet ou no Banco local?" <!-- .element: class="fragment" -->
* O ViewModel apenas pede: "Me dê a lista de usuários". <!-- .element: class="fragment" -->

---

## 🆚 MVVM vs Outros

| Padrão | Característica |
| :--- | :--- |
| **MVC** | Controller fica sobrecarregado. |
| **MVP** | Presenter e View muito acoplados. |
| **MVVM** | View observa o ViewModel (Desacoplado). |

---

## 🧪 Benefícios para Testes

Testar UI é lento e caro.
Testar lógica no ViewModel é **fast & cheap**. ⚡

> Com MVVM, você testa a lógica sem precisar abrir o emulador.

---

## 🧬 Data Binding (Avançado)

Imagine ligar o dado do ViewModel direto no XML.

```xml
<TextView
    android:text="@{viewModel.userName}" />
```

* Menos `binding.textView.text = ...` na Activity. <!-- .element: class="fragment" -->
* Código mais limpo. <!-- .element: class="fragment" -->

<!-- .slide: data-transition="convex" -->

---

## 🛠️ Prática da Aula: Contador MVVM

1. Crie uma Activity com um botão e um texto. <!-- .element: class="fragment" -->
2. Crie um `MainViewModel` com um `counter: MutableLiveData<Int>`. <!-- .element: class="fragment" -->
3. No clique, chame `counter.value = (counter.value ?: 0) + 1`. <!-- .element: class="fragment" -->
4. Observe o contador na Activity. <!-- .element: class="fragment" -->

---

### O Segredo da Rotação 🔄

Teste seu app:
1. Clique 5 vezes (Contador = 5).
2. Gire o celular.
3. Se o contador continuar em 5, você implementou MVVM corretamente! ✅

---

## 🆚 MVVM no iOS

No iOS moderno usamos **@StateObject** e **@Published**.

```swift
class UserViewModel: ObservableObject {
    @Published var name = "Ricardo"
}
```

> O conceito de "Reatividade" é o mesmo!

---

## 📊 Vantagens Reais

* **Manutenibilidade**: Código organizado por pastas. <!-- .element: class="fragment" -->
* **Escalabilidade**: Fácil adicionar novas telas. <!-- .element: class="fragment" -->
* **Performance**: UI Thread fica livre para animações. <!-- .element: class="fragment" -->

---

## 🏁 Conclusão

* Não seja um refém da `MainActivity`. <!-- .element: class="fragment" -->
* Use o ViewModel para guardar o estado. <!-- .element: class="fragment" -->
* Deixe o LiveData atualizar sua tela. <!-- .element: class="fragment" -->

---

## ❓ Dúvidas?

---

### Próxima Aula: Persistência de Dados (Room)! 💾👋
