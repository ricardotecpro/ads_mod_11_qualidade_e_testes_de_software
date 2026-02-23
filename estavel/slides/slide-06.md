# Aula 06 - Navegação entre Telas 🗺️
## Intents e o Fluxo do Usuário

---

## Agenda 📅

1. O que é uma Intent? <!-- .element: class="fragment" -->
2. Intent Explícita vs Implícita <!-- .element: class="fragment" -->
3. Passagem de Parâmetros (Extras) <!-- .element: class="fragment" -->
4. Pilha de Navegação (Back Stack) <!-- .element: class="fragment" -->
5. Android vs iOS (Navigation) <!-- .element: class="fragment" -->

---

## 1. A Intenção (Intent) 📨

- É o "envelope" de mensagem do Android. <!-- .element: class="fragment" -->
- Serve para abrir Activities, Serviços ou Broadcasts. <!-- .element: class="fragment" -->

---

## 2. Intent Explícita 🎯

- Quando você sabe o nome da classe destino. <!-- .element: class="fragment" -->

```kotlin
val intent = Intent(this, ProfileActivity::class.java)
startActivity(intent)
```

---

## 3. Passagem de Dados (Extras) 📦

```kotlin
// Enviando
intent.putExtra("NOME", "Lucas")

// Recebendo
val nome = intent.getStringExtra("NOME")
```

- Chave-Valor. <!-- .element: class="fragment" -->

---

## 4. Intent Implícita 🌍

- "Alguém aí sabe abrir um site?" <!-- .element: class="fragment" -->
- "Alguém pode ligar para este número?" <!-- .element: class="fragment" -->

```kotlin
val i = Intent(Intent.ACTION_VIEW, Uri.parse("https://..."))
startActivity(i)
```

---

## 5. A Pilha (Back Stack) 📚

- LIFO (Last In, First Out). <!-- .element: class="fragment" -->
- O botão **Voltar** desempilha a Activity do topo. <!-- .element: class="fragment" -->

---

## Limpando a Pilha

- `finish()`: Mata a tela atual. <!-- .element: class="fragment" -->
- Flags: Reconfiguram a pilha (ex: Logout). <!-- .element: class="fragment" -->

---

## 6. Comparativo: Android vs iOS 🆚

| Android 🤖 | iOS 🍎 |
| :--- | :--- |
| Intent | Segue / UIIntent |
| `startActivity` | `pushViewController` |
| `finish()` | `popViewController` |

---

## 7. Melhores Práticas 🏆

- Não passe objetos gigantes via Intent (use IDs). <!-- .element: class="fragment" -->
- Verifique se o dado existe antes de usar. <!-- .element: class="fragment" -->
- Finalize telas de login após o sucesso. <!-- .element: class="fragment" -->

---

## Desafio de Navegação ⚡

Se eu chamar `finish()` na tela de Splash, o usuário consegue voltar para ela apertando o botão de voltar?

---

## Resumo ✅

- Intents conectam os componentes. <!-- .element: class="fragment" -->
- PutExtra envia, GetExtra recebe. <!-- .element: class="fragment" -->
- Back Stack gerencia a vida e morte das telas. <!-- .element: class="fragment" -->

---

## Próxima Aula: MVVM 🏗️

- Organizando o código em camadas. <!-- .element: class="fragment" -->
- ViewModel e LiveData. <!-- .element: class="fragment" -->

---

## Dúvidas? 🗺️