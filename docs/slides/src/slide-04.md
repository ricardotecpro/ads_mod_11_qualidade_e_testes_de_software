# Aula 04 - Estrutura de um App 🏗️

<!-- .slide: data-transition="zoom" -->

---

## 🧐 O que tem "debaixo do capô"?

Ao abrir um projeto no Android Studio, vemos muitas pastas.
Não se desespere! Vamos entender cada uma.

---

## 📂 Visão Geral do Projeto

Existem dois modos de visão: **Project** e **Android**.
Nós usaremos o modo **Android** (mais organizado).

---

## 1. O Manifesto 📜

`app/src/main/AndroidManifest.xml`

É o contrato do seu app com o sistema operacional.

* Nome e Ícone do App. { .fragment }
* Declaração de todas as **Activities**. { .fragment }
* Solicitação de **Permissões** (Câmera, GPS). { .fragment }

---

## 2. A Pasta `java` (ou `kotlin`) ⌨️

Onde a "mágica" acontece.

* Ficam as classes de lógica. { .fragment }
* Ficam as classes das telas (MainActivity). { .fragment }
* Organizado em **pacotes** (ex: `com.meuapp.telas`). { .fragment }

---

## 3. A Pasta `res` (Resources) 🎨

Tudo o que o usuário **vê** ou **ouve**, mas que não é lógica.

* **drawable**: Imagens e ícones. { .fragment }
* **layout**: A interface visual (XML). { .fragment }
* **mipmap**: Ícones que aparecem no menu do celular. { .fragment }
* **values**: Strings, Cores e Temas. { .fragment }

---

### 🎨 Por que centralizar os `values`?

Evite escrever texto direto no código!

```xml
<!-- res/values/strings.xml -->
<string name="boas_vinda">Bem-vindo ao App!</string>
```

> Facilita a tradução para outros idiomas (Internacionalização). 🌍

---

## 4. Gradle: O Gerente de Fábrica ⚙️

Não é código do seu app, é a configuração da "fábrica" que constrói ele.

* `build.gradle (Project)`: Configurações globais. { .fragment }
* `build.gradle (Module)`: Configurações específicas do App. { .fragment }

---

### 📦 O que tem no Gradle?

* **versionCode**: Número interno (1, 2, 3...). { .fragment }
* **versionName**: Nome para o usuário (1.0.1...). { .fragment }
* **Dependencies**: Bibliotecas externas (Retrofit, Room). { .fragment }

---

## 🏗️ O Ciclo de Build

```mermaid
graph LR
    A[Código Kotlin/Java] --> B[Compilador]
    E[Recursos XML/Img] --> B
    B --> C[Arquivo DEX]
    C --> D[APK / AAB]
```

---

## 🆚 Estrutura: Android vs iOS

| Android | iOS | Papel |
| :---: | :---: | :--- |
| `AndroidManifest` | `Info.plist` | Metadados |
| `res/layout` | `Storyboard/XIB` | UI Visual |
| `gradle` | `CocoaPods/SwiftPM` | Dependências |
| `res/values` | `Localizable.strings` | Textos |

---

## 🔌 ViewBinding: O Link Seguro

Antigamente usava-se o `findViewById` (lento e perigoso).
Hoje usamos o **ViewBinding**.

```kotlin
// No código Kotlin
binding.txtTitulo.text = "Novo Título"
```

> Garante que você não tente acessar um ID que não existe na tela! 🛡️

---

## 🛠️ Prática: Explorando o Studio

1. Abra o arquivo `Activity_main.xml`. { .fragment }
2. Veja as abas **Code**, **Split** e **Design**. { .fragment }
3. Mantenha no **Split** para aprender rápido! { .fragment }

<!-- .slide: data-background-color="#2d6a4f" -->

---

## ⚠️ Cuidado com a pasta `build`

Ela é gerada automaticamente.
**Nunca** altere nada dentro dela manualmente. Se der erro, use o comando:
`Build -> Clean Project`.

---

## 🧩 Resumo

* **Manifesto**: Declarativo e essencial. { .fragment }
* **Res**: Visual e Multimídia. { .fragment }
* **Gradle**: Configuração e Bibliotecas. { .fragment }
* **Java/Kotlin**: Comportamento. { .fragment }

---

## 🚀 Desafio da Aula

1. Adicione uma nova cor em `colors.xml`. { .fragment }
2. Crie uma nova String em `strings.xml`. { .fragment }
3. Use essa cor e essa string em um componente na tela inicial. { .fragment }

---

## 🏁 Conclusão

Entender a estrutura é o primeiro passo para não se perder em projetos grandes.

---

### Próxima Aula: Interface Gráfica (Layouts)! 🎨👋
