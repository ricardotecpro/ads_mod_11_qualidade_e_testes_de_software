# Aula 11 - Threads e Assincronismo 🧵
## Coroutines e Performance

---

## Agenda 📅

1. Main Thread vs Background { .fragment }
2. O erro ANR 🛑 { .fragment }
3. Kotlin Coroutines ⚡ { .fragment }
4. Suspend Functions { .fragment }
5. Dispatchers (Main vs IO) { .fragment }

---

## 1. O Problema do Gargalo 🛑

- O Android desenha a tela 60 vezes por segundo. { .fragment }
- Se você "segurar" a Main Thread, o app congela. { .fragment }

---

## 2. Kotlin Coroutines ⚡

- Sequencial na leitura, assíncrono na execução. { .fragment }

```kotlin
viewModelScope.launch {
    val dados = api.buscar() // Suspende aqui
    binding.txt.text = dados // Volta aqui
}
```

---

## 3. Suspend Fun 𝑓

- Uma função que pode ser "pausada". { .fragment }
- Não bloqueia a thread original. { .fragment }

---

## 4. Dispatchers (Os Entregadores) 📦

- **Main**: Só para interface visual. { .fragment }
- **IO**: Para internet, banco e arquivos. { .fragment }
- **Default**: Para cálculos pesados. { .fragment }

---

## 5. Coroutines vs Threads puras 🆚

- Threads são pesadas e caras. { .fragment }
- Coroutines são leves (miles podem rodar ao mesmo tempo). { .fragment }

---

## 6. Cancelamento 🚫

- Se o usuário fechar a tela, a Coroutine deve parar. { .fragment }
- `viewModelScope` faz isso sozinho para você! { .fragment }

---

## Desafio de Performance ⚡

O comando `Thread.sleep(2000)` trava a tela do celular? E o `delay(2000)`?

---

## Resumo ✅

- Main Thread = UI apenas. { .fragment }
- Coroutines simplificam o async. { .fragment }
- Dispatchers definem onde o código roda. { .fragment }

---

## Próxima Aula: UX e Material 🎨

- Deixando o app bonito e moderno. { .fragment }

---

## Dúvidas? 🧵