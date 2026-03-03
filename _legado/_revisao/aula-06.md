# Aula 06 - Navegação entre Telas 🗺️

!!! tip "Objetivo"
    **Objetivo**: Aprender a navegar entre Activities usando Intents, passar dados entre telas e entender a pilha de navegação (Back Stack).

---

## 1. O que é uma Intent? 📨

Uma `Intent` (Intenção) é uma mensagem que o Android usa para pedir uma ação.
*   "Quero abrir a tela de Login".
*   "Quero abrir a Câmera".
*   "Quero compartilhar esse texto".

### Tipos de Intent
1.  **Explícita**: Você diz exatamente qual classe abrir. (Navegação interna).
    *   *Ex: Ir da Home para Detalhes.*
2.  **Implícita**: Você diz o que quer fazer, e o Android procura quem resolva.
    *   *Ex: Abrir um site (Navegador), Tirar foto (App de Câmera).*

---

## 2. Navegando para outra Activity 🚀

```kotlin
val intent = Intent(this, DetalhesActivity::class.java)
startActivity(intent)
```

### 🆚 Comparação: Segues e NavigationController (iOS)
No iOS, usamos `performSegue` ou `navigationController?.pushViewController(...)`.
A `Intent` do Android funciona como o "empurrão" para a próxima tela.

---

## 3. Passando Dados (Extras) 📦

Como enviar o nome do usuário para a próxima tela?

**Activity A (Origem):**
```kotlin
val intent = Intent(this, HomeActivity::class.java)
intent.putExtra("NOME_USUARIO", "Ricardo")
intent.putExtra("ID_USUARIO", 123)
startActivity(intent)
```

**Activity B (Destino):**
```kotlin
val nome = intent.getStringExtra("NOME_USUARIO")
val id = intent.getIntExtra("ID_USUARIO", -1) // -1 é valor padrão
```

### 🆚 Comparação: Prepare for Segue (iOS)
No iOS, interceptamos a navegação no método `prepare(for:sender:)` para configurar as propriedades da próxima ViewController. No Android, os dados vão "empacotados" na Intent.

---

## 4. A Pilha de Voltar (Back Stack) 📚

O Android gerencia as telas como uma pilha de cartas.
1.  Abre A. (Pilha: [A])
2.  A chama B. (Pilha: [A, B])
3.  B chama C. (Pilha: [A, B, C])
4.  Usuário aperta **Voltar** (Back).
    *   C é destruída (`onDestroy`).
    *   Voltamos para B (`onResume`). (Pilha: [A, B])

### Finalizando uma Activity
Se você chamar `finish()` na Activity A, ela sai da pilha.
*   Útil para tela de Login (após logar, não queremos voltar para o login).

```kotlin
// Login ok
startActivity(Intent(this, HomeActivity::class.java))
finish() // Mata a LoginActivity
```

---

## 5. Navigation Component (Moderno) 🧭

Existe uma forma mais moderna de navegar usando **Fragments** e um gráfico visual (Navigation Graph).
*   Single Activity Architecture: Uma única Activity hospeda vários Fragments (telas).
*   XML de Navegação: Define visualmente as setas de uma tela pra outra.

> Neste curso focaremos em **Intents** pois é a base fundamental. O Navigation Component abstrai as Intents por baixo.

---

## 6. Intents Implícitas (Abrindo outros apps) 🌍

Quer abrir um site?

```kotlin
val siteIntent = Intent(Intent.ACTION_VIEW, Uri.parse("https://google.com"))
startActivity(siteIntent)
```

Discar um número?

```kotlin
val discarIntent = Intent(Intent.ACTION_DIAL, Uri.parse("tel:123456789"))
startActivity(discarIntent)
```

---

## 7. Desafio: O Fluxo de Login 🔐

Desenhe o fluxo (no papel ou Mermaid) e implemente o código:
1.  **Tela Splash**: Exibe logo por 2 segundos e vai pra Login. (Usa `Handler` ou Coroutines para esperar, depois `finish()`).
2.  **Tela Login**: Digita dados -> Botão Entrar -> Vai pra Home e mata Login.
3.  **Tela Home**: Tem botão "Perfil" -> Vai pra Perfil (sem matar Home).
4.  **Tela Perfil**: Botão "Sair" -> Limpa tudo e volta pra Login.

> **Dica**: Para "limpar tudo" no Logout, use flags na Intent:
> `intent.flags = Intent.FLAG_ACTIVITY_NEW_TASK or Intent.FLAG_ACTIVITY_CLEAR_TASK`

---

**Próxima Aula**: Chega de jogar código na Activity! Vamos organizar a casa com [Arquitetura MVVM](./aula-07.md) 🏗️