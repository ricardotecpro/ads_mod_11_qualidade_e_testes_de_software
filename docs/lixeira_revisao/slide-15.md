# Aula 15 - Publicação na Google Play 🚀

<!-- .slide: data-transition="convex" -->

---

## 🏁 A Reta Final

Seu app está pronto e testado. Agora, como o mundo vai baixá-lo?

* Google Play (Android). <!-- .element: class="fragment" -->
* App Store (iOS). <!-- .element: class="fragment" -->
* Distribuição Direta (APK/Enterprise). <!-- .element: class="fragment" -->

---

## 📦 APK vs AAB

O passado e o futuro dos pacotes.

* **APK**: Um arquivo gigante para todos os celulares. <!-- .element: class="fragment" -->
* **AAB (App Bundle)**: O Google gera o APK sob medida para cada usuário. <!-- .element: class="fragment" -->
* **Resultado**: Downloads até 50% menores! 💎 <!-- .element: class="fragment" -->

---

## 🔑 A Chave da Vida (Keystore)

Todo app de produção deve ser assinado.

* O arquivo `.jks` é o seu RG. <!-- .element: class="fragment" -->
* **AVISO CRÍTICO**: Se perder a senha ou o arquivo, você nunca mais poderá atualizar o app. Guarde na nuvem, no HD e no papel! 💾 <!-- .element: class="fragment" -->

---

## 🎮 Google Play Console

O portal dos campeões.

* **Taxa**: $25 (Única e vitalícia). <!-- .element: class="fragment" -->
* **Análise**: O Google revisa seu app (1 a 7 dias). <!-- .element: class="fragment" -->
* **Políticas**: Cuidado com direitos autorais e privacidade. <!-- .element: class="fragment" -->

---

## 🛡️ Ofuscação (R8 / ProGuard)

Proteja seu código original.

* Transforma `MinhaClasseDeLogin` em `a.b.c`. <!-- .element: class="fragment" -->
* Remove código morto. <!-- .element: class="fragment" -->
* Dificulta a pirataria e engenharia reversa. <!-- .element: class="fragment" -->

---

## 📈 Versão e Build

No `build.gradle`:

* **versionCode**: 1, 2, 3... (Sempre sobe). <!-- .element: class="fragment" -->
* **versionName**: "1.0.0", "1.1.2" (O que o usuário vê). <!-- .element: class="fragment" -->

<!-- .slide: data-background-color="#344e41" -->

---

## 🎨 Marketing na Loja (ASO)

Não basta ser bom, tem que parecer bom.

* **Ícone**: A cara do seu app (512px). <!-- .element: class="fragment" -->
* **Feature Graphic**: O banner de impacto. <!-- .element: class="fragment" -->
* **Screenshots**: Mostre as melhores telas! <!-- .element: class="fragment" -->

---

## 🆚 Android vs iOS (Loja)

| Característica | Google Play | App Store |
| :--- | :--- | :--- |
| **Custo** | $25 (Única) | $99 (Anual) |
| **Revisão** | Média de 2 dias | Média de 24h a 48h |
| **Rigidez** | Moderada | Alta / Rigorosa |
| **Formato** | AAB / APK | IPA |

---

## 🧪 Canais de Teste

Teste com pessoas reais antes do lançamento.

1. **Teste Interno**: Amigos e equipe. <!-- .element: class="fragment" -->
2. **Teste Fechado (Beta)**: Grupo seleto. <!-- .element: class="fragment" -->
3. **Produção**: O mundo todo! <!-- .element: class="fragment" -->

---

## 🏆 Checklist de Lançamento

- [ ] Removi todos os `Log.d`? <!-- .element: class="fragment" -->
- [ ] O nome do app está correto? <!-- .element: class="fragment" -->
- [ ] O ícone é o de produção (não o padrão)? <!-- .element: class="fragment" -->
- [ ] Tenho os links de Política de Privacidade? <!-- .element: class="fragment" -->

---

## 🏁 Conclusão

* Publicar é um processo burocrático mas gratificante. <!-- .element: class="fragment" -->
* A segurança da Keystore é sua prioridade #1. <!-- .element: class="fragment" -->
* Marketing (ASO) é o que traz downloads. <!-- .element: class="fragment" -->

---

## ❓ Perguntas sobre Lançamento?

---

### Próxima Aula: Projeto Final e Portfólio! 🎓👋
