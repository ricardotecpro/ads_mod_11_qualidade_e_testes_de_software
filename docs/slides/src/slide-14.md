# Aula 14 - Testes e Qualidade 🐞
## Desenvolvendo com confiança

---

## Agenda 📅

1. Logcat e Debugging { .fragment }
2. Breakpoints 🛑 { .fragment }
3. Pirâmide de Testes { .fragment }
4. Testes Unitários { .fragment }
5. Testes de UI (Espresso) { .fragment }

---

## 1. Logcat 📝

- Pare de usar `println`. { .fragment }
- Use `Log.d`, `Log.e`, `Log.i`. { .fragment }
- Filtros por TAG facilitam o trabalho. { .fragment }

---

## 2. O Poder do Debugger 🛠️

- **Breakpoint**: Congela o app no tempo. { .fragment }
- Inspecione variáveis sem precisar de logs. { .fragment }
- "Step over" e "Step into". { .fragment }

---

## 3. Tipos de Testes 🧪

```mermaid
graph TD
    A[Testes Unitários - JVM] --> B[Testes de Integração]
    B --> C[Testes de UI - Espresso]
```

- **Unitários**: Rápidos e isolados. { .fragment }
- **UI**: Lentos, mas testam a experiência real. { .fragment }

---

## 4. Testes Unitários ⚙️

- Testam sua lógica (ViewModel/Business Rules). { .fragment }
- Rode direto no Mac/PC (sem emulador). { .fragment }

---

## 5. Expresso ☕

- Ele "clica" por você. { .fragment }
- Automatiza fluxos chatos (ex: teste de login). { .fragment }

```kotlin
onView(withId(R.id.btn)).perform(click())
```

---

## 6. Erros Comuns no Android ⚠️

- **NullPointerException**: O clássico. { .fragment }
- **ActivityNotFound**: Esqueceu de por no Manifest? { .fragment }
- **CalledFromWrongThread**: Mexeu na UI fora da Main Thread. { .fragment }

---

## 7. Boas Práticas 🏆

- Use `try/catch` para zonas de perigo (IO/Rede). { .fragment }
- Mostre mensagens amigáveis para o usuário. { .fragment }

---

## Desafio de Debug ⚡

Qual comando você usa para ver mensagens apenas de ERRO no Logcat?

---

## Resumo ✅

- Logcat é o seu diário. { .fragment }
- Debugger é sua lupa. { .fragment }
- Testes Automáticos são sua proteção. { .fragment }

---

## Próxima Aula: Publicação 🚀

- Hora de ganhar o mundo na Play Store. { .fragment }

---

## Dúvidas? 🐞