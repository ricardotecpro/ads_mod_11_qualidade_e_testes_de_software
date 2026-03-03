# Aula 14 - Testes e Qualidade 🐞

<!-- .slide: data-transition="slide" -->

---

## 🔍 Por que testar?

Erros custam caro.

* Perda de usuários. <!-- .element: class="fragment" -->
* Má fama na loja (1 estrela). <!-- .element: class="fragment" -->
* Prejuízo financeiro. <!-- .element: class="fragment" -->

> "Testar é o ato de provar que seu código faz o que você diz que ele faz."

---

## 📝 O Logcat Profissional

Pare de usar `println`. Use etiquetas!

* **Log.d**: Debug (lógica). <!-- .element: class="fragment" -->
* **Log.i**: Informação (eventos). <!-- .element: class="fragment" -->
* **Log.w**: Aviso (algo estranho). <!-- .element: class="fragment" -->
* **Log.e**: Erro grave. <!-- .element: class="fragment" -->

---

## 🛠️ O Modo Debug (Besouro)

Seu superpoder de investigação.

* **Breakpoint**: "Congele" o tempo naquela linha. <!-- .element: class="fragment" -->
* **Variables Panel**: Veja o que tem dentro de cada objeto. <!-- .element: class="fragment" -->
* **Evaluate Expression**: Execute código no meio da pausa! 🎩 <!-- .element: class="fragment" -->

---

## 🏔️ A Pirâmide de Testes

Não teste tudo da mesma forma.

1. **Unitários (70%)**: Lógica pura, rápidos. <!-- .element: class="fragment" -->
2. **Integração (20%)**: Peças conversando. <!-- .element: class="fragment" -->
3. **UI / Espresso (10%)**: O robô clica na tela. <!-- .element: class="fragment" -->

---

### Teste Unitário (JUnit) 🧪

```kotlin
@Test
fun login_comSenhaVazia_deveRetornarErro() {
    val result = validador.verificar("", "123")
    assertFalse(result)
}
```

* Roda no seu PC (JVM). <!-- .element: class="fragment" -->
* Leva milissegundos. <!-- .element: class="fragment" -->

---

### Teste de UI (Espresso) ☕

O robô que simula o usuário.

```kotlin
onView(withId(R.id.btnEnter)).perform(click())
onView(withId(R.id.txtWelcome)).check(matches(isDisplayed()))
```

* Roda no Emulador/Celular. <!-- .element: class="fragment" -->
* Lento, mas testa a experiência real. <!-- .element: class="fragment" -->

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

* **GitHub Actions**: Roda seus testes a cada "Push". <!-- .element: class="fragment" -->
* **Lint**: Analisa se o seu código está limpo e segue padrões. <!-- .element: class="fragment" -->

<!-- .slide: data-background-color="#5e503f" -->

---

## 🛠️ Prática: Meu Primeiro Teste

1. Vá na pasta `src/test/java`. <!-- .element: class="fragment" -->
2. Crie uma função que soma dois números. <!-- .element: class="fragment" -->
3. Escreva um `@Test` que use `assertEquals`. <!-- .element: class="fragment" -->
4. Clique no "Play" verde ao lado da função. <!-- .element: class="fragment" -->

---

## 🏁 Conclusão

* Programador bom é o que testa. <!-- .element: class="fragment" -->
* Use logs com sabedoria. <!-- .element: class="fragment" -->
* Aprenda a ler o **Stack Trace** (o relatório de erros). <!-- .element: class="fragment" -->

---

## ❓ Perguntas sobre Qualidade?

---

### Próxima Aula: Publicação na Google Play! 🚀👋
