# Aula 04 - Estrutura de um App Android 🏗️
## Manifest, Lifecycle e Layouts

---

## Agenda 📅

1. O Manifesto (Cérebro) <!-- .element: class="fragment" -->
2. Activities e ViewControllers <!-- .element: class="fragment" -->
3. O Ciclo de Vida (Nascer e Morrer) <!-- .element: class="fragment" -->
4. Layouts XML e Recursos (res/) <!-- .element: class="fragment" -->
5. ViewBinding vs findViewById <!-- .element: class="fragment" -->

---

## 1. AndroidManifest.xml 📜

- Identidade do App. <!-- .element: class="fragment" -->
- Permissões (Internet, GPS). <!-- .element: class="fragment" -->
- Lista de Telas (Activities). <!-- .element: class="fragment" -->

---

## 2. Activities: O Cérebro da Tela 🧠

- Herda de `AppCompatActivity`. <!-- .element: class="fragment" -->
- Controla a lógica de uma tela específica. <!-- .element: class="fragment" -->

---

## 3. Ciclo de Vida (Lifecycle) 🔄

Crucial para performance e bateria!

```mermaid
graph LR
    A[Created] --> B[Started]
    B --> C[Resumed]
    C --> D[Paused]
    D --> E[Stopped]
    E --> F[Destroyed]
```

---

## Estados Principais

- **onCreate**: Configuração inicial. <!-- .element: class="fragment" -->
- **onResume**: App visível e pronto para toque. <!-- .element: class="fragment" -->
- **onStop**: App saiu da frente do usuário. <!-- .element: class="fragment" -->

---

## Activity vs UIViewController

- Mesma lógica de gerenciar estados e visual. <!-- .element: class="fragment" -->

| Android 🤖 | iOS 🍎 |
| :--- | :--- |
| `onCreate` | `viewDidLoad` |
| `onStart` | `viewWillAppear` |
| `onStop` | `viewDidDisappear` |

---

## 4. Layouts XML 🎨

- O visual é separado da lógica. <!-- .element: class="fragment" -->
- Arquivos em `res/layout`. <!-- .element: class="fragment" -->

```xml
<TextView
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Olá Mundo" />
```

---

## 5. Recursos (res/) 📦

- **drawable**: Imagens. <!-- .element: class="fragment" -->
- **values/strings**: Textos traduzíveis. <!-- .element: class="fragment" -->
- **values/colors**: Paleta de cores. <!-- .element: class="fragment" -->

---

## 6. ViewBinding 🔗

- A forma moderna e segura de acessar a UI. <!-- .element: class="fragment" -->

```kotlin
// Antes (Perigoso)
val btn = findViewById<Button>(R.id.btn)

// Depois (Seguro)
binding.btnClick.setOnClickListener { ... }
```

---

## Desafio: O App sumiu! 😱

Se o usuário aperta o botão HOME, qual método do ciclo de vida é o último a ser chamado com certeza?

---

## Resumo ✅

- Manifest é a configuração. <!-- .element: class="fragment" -->
- Activity gerencia a tela. <!-- .element: class="fragment" -->
- Ciclo de vida evita travamentos e gasto de bateria. <!-- .element: class="fragment" -->
- XML desenha, Kotlin controla. <!-- .element: class="fragment" -->

---

## Próxima Aula: Interfaces (UI) 🎨

- ConstraintLayout. <!-- .element: class="fragment" -->
- Componentes Modernos. <!-- .element: class="fragment" -->
- Eventos de Clique. <!-- .element: class="fragment" -->

---

## Dúvidas? 🏗️