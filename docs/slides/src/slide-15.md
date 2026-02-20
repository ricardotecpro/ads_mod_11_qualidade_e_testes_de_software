# Aula 15 - Publicação na Google Play 🚀

<!-- .slide: data-transition="convex" -->

---

## 🏁 A Reta Final

Seu app está pronto e testado. Agora, como o mundo vai baixá-lo?

* Google Play (Android). { .fragment }
* App Store (iOS). { .fragment }
* Distribuição Direta (APK/Enterprise). { .fragment }

---

## 📦 APK vs AAB

O passado e o futuro dos pacotes.

* **APK**: Um arquivo gigante para todos os celulares. { .fragment }
* **AAB (App Bundle)**: O Google gera o APK sob medida para cada usuário. { .fragment }
* **Resultado**: Downloads até 50% menores! 💎 { .fragment }

---

## 🔑 A Chave da Vida (Keystore)

Todo app de produção deve ser assinado.

* O arquivo `.jks` é o seu RG. { .fragment }
* **AVISO CRÍTICO**: Se perder a senha ou o arquivo, você nunca mais poderá atualizar o app. Guarde na nuvem, no HD e no papel! 💾 { .fragment }

---

## 🎮 Google Play Console

O portal dos campeões.

* **Taxa**: $25 (Única e vitalícia). { .fragment }
* **Análise**: O Google revisa seu app (1 a 7 dias). { .fragment }
* **Políticas**: Cuidado com direitos autorais e privacidade. { .fragment }

---

## 🛡️ Ofuscação (R8 / ProGuard)

Proteja seu código original.

* Transforma `MinhaClasseDeLogin` em `a.b.c`. { .fragment }
* Remove código morto. { .fragment }
* Dificulta a pirataria e engenharia reversa. { .fragment }

---

## 📈 Versão e Build

No `build.gradle`:

* **versionCode**: 1, 2, 3... (Sempre sobe). { .fragment }
* **versionName**: "1.0.0", "1.1.2" (O que o usuário vê). { .fragment }

<!-- .slide: data-background-color="#344e41" -->

---

## 🎨 Marketing na Loja (ASO)

Não basta ser bom, tem que parecer bom.

* **Ícone**: A cara do seu app (512px). { .fragment }
* **Feature Graphic**: O banner de impacto. { .fragment }
* **Screenshots**: Mostre as melhores telas! { .fragment }

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

1. **Teste Interno**: Amigos e equipe. { .fragment }
2. **Teste Fechado (Beta)**: Grupo seleto. { .fragment }
3. **Produção**: O mundo todo! { .fragment }

---

## 🏆 Checklist de Lançamento

- [ ] Removi todos os `Log.d`? { .fragment }
- [ ] O nome do app está correto? { .fragment }
- [ ] O ícone é o de produção (não o padrão)? { .fragment }
- [ ] Tenho os links de Política de Privacidade? { .fragment }

---

## 🏁 Conclusão

* Publicar é um processo burocrático mas gratificante. { .fragment }
* A segurança da Keystore é sua prioridade #1. { .fragment }
* Marketing (ASO) é o que traz downloads. { .fragment }

---

## ❓ Perguntas sobre Lançamento?

---

### Próxima Aula: Projeto Final e Portfólio! 🎓👋
