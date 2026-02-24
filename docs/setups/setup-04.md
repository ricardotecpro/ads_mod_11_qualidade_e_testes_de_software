# Setup 04: Java & Maven para QA ☕

O ecossistema Java é muito forte em empresas enterprise para automação com Selenium e RestAssured.

## 1. JDK (Java Development Kit)
1.  Baixe o **JDK 17 ou 21 (LTS)** no site da Oracle ou Adoptium.
2.  Configure a variável `JAVA_HOME`.

## 2. Apache Maven
O Maven é o gestor de dependências padrão para projetos Java.
1.  Baixe em [maven.apache.org](https://maven.apache.org/download.cgi).
2.  Adicione a pasta `bin` ao seu PATH.
3.  Teste: `mvn -version`.

## 3. IntelliJ IDEA (Comunidade)
Excelente suporte para refatoração e execução de testes JUnit/TestNG.
1.  Baixe a versão **Community** em [jetbrains.com/idea](https://www.jetbrains.com/idea/).

## 4. Dependências de QA comuns (pom.xml)
No seu projeto Maven, você geralmente incluirá:
- `selenium-java`
- `junit-jupiter`
- `rest-assured`

## 5. Solução de Problemas Comuns ⚠️
*   **Erro de Compilação**: Verifique se a versão do JDK no IntelliJ está alinhada com a do seu sistema.
*   **Maven não baixa pacotes**: Pode ser problema de Proxy da empresa ou rede. Verifique seu arquivo `settings.xml`.