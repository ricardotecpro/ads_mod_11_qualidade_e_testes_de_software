# Aula 06 - Navegação entre Telas 🗺️
## Intents e o Fluxo do Usuário

---

## Agenda 📅

1. O que é uma Intent? { .fragment }
2. Intent Explícita vs Implícita { .fragment }
3. Passagem de Parâmetros (Extras) { .fragment }
4. Pilha de Navegação (Back Stack) { .fragment }
5. Android vs iOS (Navigation) { .fragment }

---

## 1. A Intenção (Intent) 📨

- É o "envelope" de mensagem do Android. { .fragment }
- Serve para abrir Activities, Serviços ou Broadcasts. { .fragment }

---

## 2. Intent Explícita 🎯

- Quando você sabe o nome da classe destino. { .fragment }

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

- Chave-Valor. { .fragment }

---

## 4. Intent Implícita 🌍

- "Alguém aí sabe abrir um site?" { .fragment }
- "Alguém pode ligar para este número?" { .fragment }

```kotlin
val i = Intent(Intent.ACTION_VIEW, Uri.parse("https://..."))
startActivity(i)
```

---

## 5. A Pilha (Back Stack) 📚

- LIFO (Last In, First Out). { .fragment }
- O botão **Voltar** desempilha a Activity do topo. { .fragment }

---

## Limpando a Pilha

- `finish()`: Mata a tela atual. { .fragment }
- Flags: Reconfiguram a pilha (ex: Logout). { .fragment }

---

## 6. Comparativo: Android vs iOS 🆚

| Android 🤖 | iOS 🍎 |
| :--- | :--- |
| Intent | Segue / UIIntent |
| `startActivity` | `pushViewController` |
| `finish()` | `popViewController` |

---

## 7. Melhores Práticas 🏆

- Não passe objetos gigantes via Intent (use IDs). { .fragment }
- Verifique se o dado existe antes de usar. { .fragment }
- Finalize telas de login após o sucesso. { .fragment }

---

## Desafio de Navegação ⚡

Se eu chamar `finish()` na tela de Splash, o usuário consegue voltar para ela apertando o botão de voltar?

---

## Resumo ✅

- Intents conectam os componentes. { .fragment }
- PutExtra envia, GetExtra recebe. { .fragment }
- Back Stack gerencia a vida e morte das telas. { .fragment }

---

## Próxima Aula: MVVM 🏗️

- Organizando o código em camadas. { .fragment }
- ViewModel e LiveData. { .fragment }

---

## Dúvidas? 🗺️