# Setup 04: Java e JDK ☕

## 1. JDK (Java Development Kit)
O kit essencial para compilar Java.
1.  Baixe o **JDK 17 LTS (ou 21 LTS)** no site da Oracle ou Adoptium.
2.  Instale e configure a variável de ambiente `JAVA_HOME`.
3.  Teste: `java -version`.

## 2. IntelliJ IDEA (Recomendado)
A melhor IDE para Java/Kotlin.
1.  Baixe a versão **Community** (Gratuita) em [jetbrains.com/idea](https://www.jetbrains.com/idea/).
2.  Instale.

## 3. VS Code
Se preferir o VS Code:
1.  Instale o "Extension Pack for Java" da Microsoft.

## 4. Solução de Problemas Comuns ⚠️

*   **'javac' não reconhecido**: A variável de ambiente `JAVA_HOME` ou o `Path` estão errados. Verifique se apontam para a pasta `bin` do JDK.
*   **Erro: "Class names are only accepted..."**: O nome do arquivo DEVE ser igual ao nome da classe (ex: `Ola.java` tem que ter `public class Ola`).
*   **Versão antiga do Java**: Digite `java -version` para conferir se está usando a versão que acabou de instalar.