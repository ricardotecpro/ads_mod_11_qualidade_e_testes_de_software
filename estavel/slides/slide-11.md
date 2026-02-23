# Aula 11 - Threads e Assincronismo 🧵
## Coroutines e Performance

---

## Agenda 📅

1. Main Thread vs Background <!-- .element: class="fragment" -->
2. O erro ANR 🛑 <!-- .element: class="fragment" -->
3. Kotlin Coroutines ⚡ <!-- .element: class="fragment" -->
4. Suspend Functions <!-- .element: class="fragment" -->
5. Dispatchers (Main vs IO) <!-- .element: class="fragment" -->

---

## 1. O Problema do Gargalo 🛑

- O Android desenha a tela 60 vezes por segundo. <!-- .element: class="fragment" -->
- Se você "segurar" a Main Thread, o app congela. <!-- .element: class="fragment" -->

---

## 2. Kotlin Coroutines ⚡

- Sequencial na leitura, assíncrono na execução. <!-- .element: class="fragment" -->

```kotlin
viewModelScope.launch {
    val dados = api.buscar() // Suspende aqui
    binding.txt.text = dados // Volta aqui
}
```

---

## 3. Suspend Fun 𝑓

- Uma função que pode ser "pausada". <!-- .element: class="fragment" -->
- Não bloqueia a thread original. <!-- .element: class="fragment" -->

---

## 4. Dispatchers (Os Entregadores) 📦

- **Main**: Só para interface visual. <!-- .element: class="fragment" -->
- **IO**: Para internet, banco e arquivos. <!-- .element: class="fragment" -->
- **Default**: Para cálculos pesados. <!-- .element: class="fragment" -->

---

## 5. Coroutines vs Threads puras 🆚

- Threads são pesadas e caras. <!-- .element: class="fragment" -->
- Coroutines são leves (miles podem rodar ao mesmo tempo). <!-- .element: class="fragment" -->

---

## 6. Cancelamento 🚫

- Se o usuário fechar a tela, a Coroutine deve parar. <!-- .element: class="fragment" -->
- `viewModelScope` faz isso sozinho para você! <!-- .element: class="fragment" -->

---

## Desafio de Performance ⚡

O comando `Thread.sleep(2000)` trava a tela do celular? E o `delay(2000)`?

---

## Resumo ✅

- Main Thread = UI apenas. <!-- .element: class="fragment" -->
- Coroutines simplificam o async. <!-- .element: class="fragment" -->
- Dispatchers definem onde o código roda. <!-- .element: class="fragment" -->

---

## Próxima Aula: UX e Material 🎨

- Deixando o app bonito e moderno. <!-- .element: class="fragment" -->

---

## Dúvidas? 🧵