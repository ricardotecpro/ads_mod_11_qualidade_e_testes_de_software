# Aula 02 - Java para Android ☕

<!-- .slide: data-transition="convex" -->

---

## 🎯 Por que aprender Java em 2026?

"O Kotlin não matou o Java?"

* **Base Sólida**: O Android é feito de Java. <!-- .element: class="fragment" -->
* **Legado**: Bilhões de linhas de código em produção. <!-- .element: class="fragment" -->
* **Mercado**: Muitas empresas pedem os dois. <!-- .element: class="fragment" -->

---

## 🧱 A Base da Sintaxe

Java é uma linguagem de tipagem estática e explícita.

```java
public class Ola {
    public static void main(String[] args) {
        System.out.println("Olá, Java!");
    }
}
```

---

## 📦 Variáveis e Tipos

Onde guardamos os dados na memória.

* **int**: Números inteiros. <!-- .element: class="fragment" -->
* **double**: Números decimais. <!-- .element: class="fragment" -->
* **boolean**: true ou false. <!-- .element: class="fragment" -->
* **String**: Texto (É uma classe!). <!-- .element: class="fragment" -->

---

### Cuidado com o Null! 👻

Em Java, objetos podem ser `null`.
Isso causa o famoso **NullPointerException**.

```java
String nome = null;
int tamanho = nome.length(); // BOOM! 💥
```

---

## 🔀 Estruturas de Decisão

```java
int idade = 20;

if (idade >= 18) {
    System.out.println("Pode dirigir");
} else {
    System.out.println("Aguarde mais um pouco");
}
```

---

## 🔁 Estruturas de Repetição

```java
// Contar até 5
for (int i = 1; i <= 5; i++) {
    System.out.println("Número: " + i);
}
```

---

## 🏛️ Orientação a Objetos (POO)

O coração do desenvolvimento nativo.

* **Classe**: O molde (Planta da casa). <!-- .element: class="fragment" -->
* **Objeto**: A instância (A casa construída). <!-- .element: class="fragment" -->

---

### Exemplo: Classe Carro 🚗

```java
public class Carro {
    String modelo;
    int ano;

    void buzinar() {
        System.out.println("Beep Beep!");
    }
}
```

---

## 🧬 Herança: O `extends`

No Android, usamos herança o tempo todo.

```java
public class MainActivity extends Activity {
    // Agora minha classe faz tudo que uma Activity faz!
}
```

---

## 🔒 Encapsulamento

Proteja seus dados!

* **public**: Todos veem. <!-- .element: class="fragment" -->
* **private**: Só a classe vê. <!-- .element: class="fragment" -->

> Use **getters** e **setters** para acessar dados privados.

---

## 🗺️ Android Studio: Onde o Java vive

Ao criar um App, o código Java fica na pasta:
`app/src/main/java/`

---

### Ciclo de Vida: O `onCreate`

O primeiro contato com o Android.

```java
@Override
protected void onCreate(Bundle savedInstanceState) {
    super.onCreate(savedInstanceState);
    setContentView(R.layout.activity_main);
}
```

---

## 🔬 Comparação: Java vs Swift

No iOS (Swift), os conceitos são os mesmos, muda a "roupa".

* Java: `public class`
* Swift: `class` (mais simples)

---

## 🛠️ Ferramentas da Aula

1. **JDK instalado**. <!-- .element: class="fragment" -->
2. **IntelliJ** ou **Android Studio**. <!-- .element: class="fragment" -->
3. Treinar lógica básica no console. <!-- .element: class="fragment" -->

<!-- .slide: data-background-color="#5d2a42" -->

---

## 🧩 Exercício Rápido

Crie uma classe `Usuario` com:
* Nome (String)
* Idade (int)
* Método `verificarIdade()` que diz se é maior de idade.

---

## ⚡ De Java para Kotlin

Na aula de hoje vimos Java.
Nas próximas, veremos como o Kotlin simplifica **TUDO** isso.

> Mas sem entender o Java, você será apenas um "copiador de código".

---

## 🏁 Resumo

* Java é a fundação. <!-- .element: class="fragment" -->
* POO é essencial para Android. <!-- .element: class="fragment" -->
* Classes, Atributos e Métodos são seus novos amigos. <!-- .element: class="fragment" -->

---

## ❓ Pergunta do Dia

"Posso criar um app Android sem saber nadinha de Java?"

> Pode, mas na primeira biblioteca antiga que você baixar, vai travar!

---

### Próxima Aula: Kotlin Moderno ⚡

---

### Valeu, pessoal! 👋
