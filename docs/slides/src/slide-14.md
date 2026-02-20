# Aula 14 - Testes e Qualidade 🐞

<!-- .slide: data-transition="slide" -->

---

## 🔍 Por que testar?

Erros custam caro.

* Perda de usuários. { .fragment }
* Má fama na loja (1 estrela). { .fragment }
* Prejuízo financeiro. { .fragment }

> "Testar é o ato de provar que seu código faz o que você diz que ele faz."

---

## 📝 O Logcat Profissional

Pare de usar `println`. Use etiquetas!

* **Log.d**: Debug (lógica). { .fragment }
* **Log.i**: Informação (eventos). { .fragment }
* **Log.w**: Aviso (algo estranho). { .fragment }
* **Log.e**: Erro grave. { .fragment }

---

## 🛠️ O Modo Debug (Besouro)

Seu superpoder de investigação.

* **Breakpoint**: "Congele" o tempo naquela linha. { .fragment }
* **Variables Panel**: Veja o que tem dentro de cada objeto. { .fragment }
* **Evaluate Expression**: Execute código no meio da pausa! 🎩 { .fragment }

---

## 🏔️ A Pirâmide de Testes

Não teste tudo da mesma forma.

1. **Unitários (70%)**: Lógica pura, rápidos. { .fragment }
2. **Integração (20%)**: Peças conversando. { .fragment }
3. **UI / Espresso (10%)**: O robô clica na tela. { .fragment }

---

### Teste Unitário (JUnit) 🧪

```kotlin
@Test
fun login_comSenhaVazia_deveRetornarErro() {
    val result = validador.verificar("", "123")
    assertFalse(result)
}
```

* Roda no seu PC (JVM). { .fragment }
* Leva milissegundos. { .fragment }

---

### Teste de UI (Espresso) ☕

O robô que simula o usuário.

```kotlin
onView(withId(R.id.btnEnter)).perform(click())
onView(withId(R.id.txtWelcome)).check(matches(isDisplayed()))
```

* Roda no Emulador/Celular. { .fragment }
* Lento, mas testa a experiência real. { .fragment }

---

## 🛡️ Tratamento de Exceções

Previna o "O App parou".

```kotlin
try {
    fazerAlgoPerigoso()
} catch (e: Exception) {
    Log.e("BUM", "Deu ruim", e)
    showErrorDialog()
}
```

---

## 🆚 Android vs iOS (Qualidade)

| Ferramenta | Android | iOS |
| :--- | :--- | :--- |
| **Unit Testing** | JUnit / Mockito | XCTest |
| **UI Testing** | Espresso / Barista | XCUITest |
| **Logs** | Logcat | Console (os_log) |
| **Profiler** | Android Profiler | Xcode Instruments |

---

## 🏃 CI/CD: Automação

Nunca envie código quebrado para o GitHub.

* **GitHub Actions**: Roda seus testes a cada "Push". { .fragment }
* **Lint**: Analisa se o seu código está limpo e segue padrões. { .fragment }

<!-- .slide: data-background-color="#5e503f" -->

---

## 🛠️ Prática: Meu Primeiro Teste

1. Vá na pasta `src/test/java`. { .fragment }
2. Crie uma função que soma dois números. { .fragment }
3. Escreva um `@Test` que use `assertEquals`. { .fragment }
4. Clique no "Play" verde ao lado da função. { .fragment }

---

## 🏁 Conclusão

* Programador bom é o que testa. { .fragment }
* Use logs com sabedoria. { .fragment }
* Aprenda a ler o **Stack Trace** (o relatório de erros). { .fragment }

---

## ❓ Perguntas sobre Qualidade?

---

### Próxima Aula: Publicação na Google Play! 🚀👋
