# Aula 01 - Introdução ao Mobile 📱

<!-- .slide: data-transition="zoom" -->

---

## Bem-vindo ao Mundo Mobile! 🌍

O mundo hoje é _mobile-first_.

* Mais acesso via smartphone que PC. <!-- .element: class="fragment" -->
* Bilhões de dispositivos ativos. <!-- .element: class="fragment" -->
* Ecossistema dinâmico e lucrativo. <!-- .element: class="fragment" -->

---

## 🎯 Nossa Agenda de Hoje

1. Panorama do Mercado <!-- .element: class="fragment" -->
2. Nativo vs Híbrido vs Web <!-- .element: class="fragment" -->
3. Android vs iOS <!-- .element: class="fragment" -->
4. Android Studio & Ferramentas <!-- .element: class="fragment" -->
5. Por onde começar? <!-- .element: class="fragment" -->

---

## 📱 1. Os Três Caminhos

Existem três formas principais de criar um App.

<!-- .slide: data-transition="slide-in fade-out" -->

---

### 🚀 Nativo

Desenvolvido na linguagem "mãe" da plataforma.

* **Android**: Kotlin / Java 🤖 <!-- .element: class="fragment" -->
* **iOS**: Swift / Objective-C 🍎 <!-- .element: class="fragment" -->
* **Vantagem**: Performance máxima e acesso total ao hardware. <!-- .element: class="fragment" -->

---

### 🌐 Web (PWA)

Basicamente um site que se comporta como App.

* **Tecnologias**: HTML, CSS, JS.
* **Vantagem**: Custo baixo, funciona em tudo.
* **Desvantagem**: Performance limitada e pouco acesso ao hardware. <!-- .element: class="fragment" -->

---

### 🧩 Híbrido / Cross-Platform

Usa um framework para gerar ambas as plataformas.

* **Exemplos**: Flutter, React Native.
* **Vantagem**: Uma base de código para dois apps.
* **Desvantagem**: Dependência de terceiros e overhead de performance. <!-- .element: class="fragment" -->

---

## 🤖 2. O Gigante Verde: Android

O sistema operacional mais usado do planeta.

* Criado pelo Google. <!-- .element: class="fragment" -->
* Baseado em **Linux**. <!-- .element: class="fragment" -->
* Aberto e flexível. <!-- .element: class="fragment" -->

---

### Arquitetura Android

```mermaid
graph TD
    A[Apps] --> B[Java/Kotlin Framework]
    B --> C[ART Runtime]
    C --> D[Hardware Abstraction - HAL]
    D --> E[Linux Kernel]
```

---

## 🍎 3. O Pomar da Apple: iOS

Foco em luxo, fluidez e segurança.

* Criado pela Apple. <!-- .element: class="fragment" -->
* Sistema Fechado (Darwin/Unix). <!-- .element: class="fragment" -->
* Consumidores com alto poder aquisitivo. <!-- .element: class="fragment" -->

---

### Android vs iOS 🆚

| Recurso | Android | iOS |
| :--- | :--- | :--- |
| **Linguagem** | Kotlin | Swift |
| **IDE** | Android Studio | Xcode |
| **Loja** | Google Play | App Store |
| **Taxa** | $25 (Única) | $99 (Anual) |

---

## 🛠️ 4. Sua Oficina: Android Studio

A ferramenta oficial para criar apps Android.

* Baseada no IntelliJ IDEA. <!-- .element: class="fragment" -->
* Emulador integrado. <!-- .element: class="fragment" -->
* Layout Editor visual. <!-- .element: class="fragment" -->

<!-- .slide: data-background-color="#073b4c" -->

---

### ⚠️ Requisitos de Hardware

Para não passar raiva:

* **RAM**: 8GB (Mínimo) / 16GB (Sonho). <!-- .element: class="fragment" -->
* **Disco**: SSD é OBRIGATÓRIO. <!-- .element: class="fragment" -->
* **Processador**: i5 ou superior. <!-- .element: class="fragment" -->

---

## 📂 5. Anatomia de um Projeto

O que tem dentro das pastas?

```termynal
$ ls -R app/src/main
AndroidManifest.xml
java/ # Código Fonte
res/  # Recursos (Imagens/Layouts)
```

---

### O Manifesto 📜

O arquivo `AndroidManifest.xml` é o "RG" do seu App.

* Nome do App. <!-- .element: class="fragment" -->
* Quais telas existem (Activities). <!-- .element: class="fragment" -->
* Quais permissões ele precisa (Internet, Câmera). <!-- .element: class="fragment" -->

---

## 🧠 6. Por que Nativo?

Frameworks vêm e vão, mas o **Nativo** permanece.

> "Quem entende a base, não teme a mudança."

<!-- .slide: data-transition="convex" -->

---

## 🆚 Kotlin vs Swift

São linguagens "irmãs" na sintaxe!

```kotlin
// Kotlin
val nome = "Ricardo"
println("Olá $nome")
```

```swift
// Swift
let nome = "Ricardo"
print("Olá \(nome)")
```

---

## 🚀 Desafio de Hoje

1. Instalar o **Android Studio**. <!-- .element: class="fragment" -->
2. Criar seu primeiro projeto "Empty Activity". <!-- .element: class="fragment" -->
3. Mudar o texto do "Hello World" para seu nome. <!-- .element: class="fragment" -->

---

## 🏁 Conclusão

* Mobile é o presente e o futuro. <!-- .element: class="fragment" -->
* Escolher o caminho Nativo te dá superpoderes. <!-- .element: class="fragment" -->
* Próxima aula: **Java para Android**. <!-- .element: class="fragment" -->

---

## ❓ Dúvidas?

Siga para o canal oficial da disciplina no Teams!

---

### Fim da Aula 01 👋
