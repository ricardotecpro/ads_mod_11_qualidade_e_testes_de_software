### **Passo 1: Configurando o Projeto JavaFX**

Vamos criar um novo projeto para nossa aplicação desktop. Manteremos os projetos separados (`todolist-api`, `todolist-web`, e agora `todolist-desktop`).

1.  **Crie um Novo Projeto Maven:**

      * Abra sua IDE (IntelliJ IDEA, por exemplo) e crie um **novo projeto Maven**.
      * Não selecione nenhum arquétipo (archetype), apenas um projeto Maven simples.
      * **GroupId:** `br.com.curso`
      * **ArtifactId:** `todolist-desktop`

2.  **Configure o `pom.xml`:**
    O arquivo `pom.xml` é o coração do nosso projeto Maven. Precisamos adicionar as dependências para o JavaFX e também para uma biblioteca que nos ajudará a consumir nossa API (para lidar com HTTP e JSON).

    Abra o arquivo `pom.xml` e substitua seu conteúdo por este:

    ```xml
    <?xml version="1.0" encoding="UTF-8"?>
    <project xmlns="http://maven.apache.org/POM/4.0.0"
             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
             xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
        <modelVersion>4.0.0</modelVersion>

        <groupId>br.com.curso</groupId>
        <artifactId>todolist-desktop</artifactId>
        <version>1.0-SNAPSHOT</version>

        <properties>
            <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
            <maven.compiler.source>17</maven.compiler.source> <maven.compiler.target>17</maven.compiler.target>
            <javafx.version>17.0.6</javafx.version> </properties>

        <dependencies>
            <dependency>
                <groupId>org.openjfx</groupId>
                <artifactId>javafx-controls</artifactId>
                <version>${javafx.version}</version>
            </dependency>
            <dependency>
                <groupId>org.openjfx</groupId>
                <artifactId>javafx-fxml</artifactId>
                <version>${javafx.version}</version>
            </dependency>

            <dependency>
                <groupId>com.fasterxml.jackson.core</groupId>
                <artifactId>jackson-databind</artifactId>
                <version>2.15.2</version> </dependency>
        </dependencies>

        <build>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <version>3.8.1</version>
                    <configuration>
                        <source>17</source>
                        <target>17</target>
                    </configuration>
                </plugin>
            </plugins>
        </build>
    </project>
    ```

    Após salvar o `pom.xml`, sua IDE irá pedir para "carregar as mudanças do Maven". Aceite para que ele baixe as dependências que acabamos de declarar.

3.  **Crie a Estrutura de Pacotes e a Classe Principal:**

      * Dentro de `src/main/java`, crie a estrutura de pacotes: `br.com.curso.todolist.desktop`.
      * Dentro deste pacote, crie uma classe Java chamada `MainApp.java`. Esta será a classe que inicia nossa aplicação desktop.

    **Código para `MainApp.java`:**

    ```java
    package br.com.curso.todolist.desktop;

    import javafx.application.Application;
    import javafx.scene.Scene;
    import javafx.scene.control.Label;
    import javafx.scene.layout.StackPane;
    import javafx.stage.Stage;

    public class MainApp extends Application {

        @Override
        public void start(Stage primaryStage) {
            // Por enquanto, vamos apenas criar uma janela simples para testar
            Label label = new Label("Olá, Mundo do Desktop!");
            StackPane root = new StackPane(label);
            Scene scene = new Scene(root, 400, 300);

            primaryStage.setTitle("Minha Lista de Tarefas (Desktop)");
            primaryStage.setScene(scene);
            primaryStage.show();
        }

        public static void main(String[] args) {
            launch(args);
        }
    }
    ```

4.  **Execute e Verifique:**
    Rode o método `main` da classe `MainApp`. Se tudo estiver configurado corretamente, uma pequena janela de desktop deve aparecer na sua tela com a mensagem "Olá, Mundo do Desktop\!".

Com isso, nosso projeto base para o cliente desktop está configurado e pronto.

**Próxima etapa lógica:** Vamos usar o **Scene Builder** para desenhar a interface visual da nossa aplicação (a *View* do nosso MVC) e salvá-la como um arquivo FXML.


---

Excelente\! A janela de teste confirma que toda a configuração base do JavaFX está correta.

Agora vamos para a parte visual. Em vez de criar a interface escrevendo código Java, vamos usar uma abordagem muito mais produtiva e alinhada com o padrão MVC: **criar a *View* usando um arquivo FXML**.

**O que é FXML?** É um formato baseado em XML que permite definir a estrutura da interface do usuário de forma declarativa, separando completamente a aparência (a *View*) da lógica da aplicação (o *Controller*).

-----

### **Próxima Etapa: Desenhando a Interface com Scene Builder**

Vamos criar a tela principal da nossa aplicação de desktop.

#### **Passo 1: Crie o Arquivo FXML**

1.  Dentro do seu projeto, na pasta `src/main/resources`, crie uma nova estrutura de pastas que espelhe seu pacote Java: `br/com/curso/todolist/desktop`.
2.  Dentro desta nova pasta, crie um novo arquivo chamado `MainView.fxml`.

Sua estrutura de recursos deve ficar assim:

```
src/
└── main/
    └── resources/
        └── br/
            └── com/
                └── curso/
                    └── todolist/
                        └── desktop/
                            └── MainView.fxml
```

#### **Passo 2: Abra o Scene Builder e Desenhe a Tela**

1.  Clique com o botão direito no arquivo `MainView.fxml` na sua IDE e selecione "Open in Scene Builder" (ou abra o Scene Builder e navegue até o arquivo).

2.  Você verá uma tela em branco. Vamos adicionar os componentes:

      * No painel de "Containers" à esquerda, arraste um `VBox` para a área principal. Um `VBox` empilha os elementos verticalmente.
      * No painel de "Controls", arraste um `Label` para dentro do `VBox` e mude seu texto para "Minha Lista de Tarefas".
      * Abaixo do `Label`, arraste um `TableView`. Este será o componente mais importante, que mostrará nossas tarefas.
      * Abaixo da `TableView`, arraste um `HBox`. Um `HBox` alinha os elementos horizontalmente.
      * Para dentro do `HBox`, arraste um `TextField` (onde o usuário digitará a nova tarefa) e um `Button` (para adicionar a tarefa). Mude o texto do botão para "Adicionar".

3.  **Ajuste o Layout:** Use o painel "Layout" à direita para adicionar espaçamento (`spacing`) e margens (`padding`) ao `VBox` e `HBox` para que a interface fique mais agradável. Faça o `TextField` crescer para ocupar o espaço disponível no `HBox` usando a propriedade "Hgrow" em "Layout".

#### **Passo 3: Conectando a View ao Futuro Controller**

Esta é a etapa crucial que liga o design à lógica.

1.  **Associe um Controller:** Com o `VBox` principal selecionado, vá para o painel "Controller" no canto inferior esquerdo do Scene Builder. No campo **Controller class**, digite o caminho completo da classe que *iremos criar* para controlar esta view: `br.com.curso.todolist.desktop.MainViewController`.

2.  **Atribua IDs (`fx:id`):** Precisamos dar "nomes" aos componentes que nosso código Java precisará manipular. Selecione cada um dos seguintes componentes e, no painel "Code" à direita, preencha o campo **fx:id**:

      * `TableView` -\> `tabelaTarefas`
      * `TextField` -\> `campoDescricao`

3.  **Defina a Ação do Botão:** Selecione o botão "Adicionar". No painel "Code", no campo **On Action**, digite `#onAdicionarAction`. Isso significa que, quando o botão for clicado, ele chamará um método chamado `onAdicionarAction` no nosso controller.

4.  **Salve o arquivo** no Scene Builder (`Ctrl+S`).

O seu arquivo `MainView.fxml` agora conterá um código XML parecido com este:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<?import javafx.geometry.Insets?>
<?import javafx.scene.control.Button?>
<?import javafx.scene.control.Label?>
<?import javafx.scene.control.TableView?>
<?import javafx.scene.control.TextField?>
<?import javafx.scene.layout.HBox?>
<?import javafx.scene.layout.VBox?>

<VBox maxHeight="-Infinity" maxWidth="-Infinity" minHeight="-Infinity" minWidth="-Infinity" prefHeight="400.0" prefWidth="600.0" spacing="10.0" xmlns="http://javafx.com/javafx/21" xmlns:fx="http://javafx.com/fxml/1" fx:controller="br.com.curso.todolist.desktop.MainViewController">
   <padding>
      <Insets bottom="10.0" left="10.0" right="10.0" top="10.0" />
   </padding>
   <children>
      <Label text="Minha Lista de Tarefas" />
      <TableView fx:id="tabelaTarefas" prefHeight="200.0" prefWidth="200.0" VBox.vgrow="ALWAYS" />
      <HBox spacing="10.0">
         <children>
            <TextField fx:id="campoDescricao" HBox.hgrow="ALWAYS" />
            <Button mnemonicParsing="false" onAction="#onAdicionarAction" text="Adicionar" />
         </children>
      </HBox>
   </children>
</VBox>
```

-----

### **Próxima Etapa Lógica: Criar o Controller e Carregar o FXML**

Agora que a *View* está desenhada, precisamos:

1.  Criar a classe `MainViewController.java` que declaramos no FXML.
2.  Atualizar a classe `MainApp.java` para carregar e exibir este arquivo FXML em vez da `Label` de "Olá, Mundo".



---

#  Configurar o Scene Builder

O IntelliJ IDEA, por padrão, não sabe onde o programa "Scene Builder" foi instalado no seu computador. Precisamos apenas informá-lo.

Siga estes passos para configurar o caminho e fazer a opção aparecer:

### **Configurando o Caminho do Scene Builder no IntelliJ IDEA**

1.  **Abra as Configurações (Settings):**

      * No Windows/Linux: Vá em `File` -\> `Settings...`
      * No macOS: Vá em `IntelliJ IDEA` -\> `Settings...` (ou `Preferences...`)

2.  **Navegue até as Configurações do JavaFX:**

      * Na janela de configurações que se abriu, procure no menu à esquerda por `Languages & Frameworks`.
      * Clique em `JavaFX`.

3.  **Informe o Caminho do Scene Builder:**

      * Você verá um campo chamado **"Path to Scene Builder"**. Ele provavelmente está vazio.
      * Clique no ícone de pasta (`...`) ao lado do campo.
      * Agora, você precisa navegar no seu computador e encontrar o arquivo executável do Scene Builder. Os locais mais comuns são:
          * **Windows:** `C:\Program Files\Scene Builder\SceneBuilder.exe` ou `C:\Users\<SeuNomeDeUsuario>\AppData\Local\SceneBuilder\SceneBuilder.exe`
          * **macOS:** `/Applications/SceneBuilder.app`
          * **Linux:** Geralmente em `/opt/SceneBuilder/` ou `/usr/lib/SceneBuilder/` (procure pelo arquivo executável `SceneBuilder`).

4.  **Aplique as Mudanças:**

      * Depois de selecionar o arquivo executável, clique em `OK`.
      * Na janela de configurações, clique em `Apply` e depois em `OK`.

5.  **Tente Novamente:**

      * Volte para o seu projeto.
      * Clique com o botão direito no arquivo `MainView.fxml`.
      * A opção **"Open in Scene Builder"** agora deve estar visível no menu\!

-----

### **Alternativa (Plano B)**

Se por algum motivo a integração não funcionar, não se preocupe. Você pode simplesmente seguir o fluxo manual, que funciona perfeitamente:

1.  Abra o programa **Scene Builder** diretamente pelo menu Iniciar do Windows ou pela pasta de Aplicativos do macOS.
2.  Dentro do Scene Builder, vá em `File` -\> `Open...`.
3.  Navegue até a pasta do seu projeto e encontre o arquivo: `todolist-desktop/src/main/resources/br/com/curso/todolist/desktop/MainView.fxml`.
4.  Abra o arquivo.

Você poderá editar o arquivo normalmente e, quando salvar (`Ctrl+S`), as alterações serão refletidas automaticamente no arquivo dentro do seu projeto no IntelliJ.

O importante é conseguir editar o FXML. A integração com o botão direito é apenas um atalho conveniente.

# Conectar as peças

Excelente\! Você está no caminho certo. Agora vamos conectar as peças: o arquivo de design (`.fxml`) com o código de lógica (`.java`).

Aqui estão as respostas detalhadas para cada uma das suas perguntas.

-----

### **Parte 1: Criando o Controller (`MainViewController.java`)**

**Onde criar?**
A classe `MainViewController.java` é uma classe Java normal. Você deve criá-la dentro do seu pacote principal de código-fonte:
`src/main/java/br/com/curso/todolist/desktop/`

**Qual o código?**
Este código inicial fará a "ponte" entre o FXML e o Java. Ele terá variáveis que correspondem aos `fx:id` que definimos no Scene Builder e o método que corresponde ao `onAction` do botão.

Crie a classe `MainViewController.java` com o seguinte conteúdo:

```java
package br.com.curso.todolist.desktop;

import javafx.fxml.FXML;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;

// Não precisamos da classe Tarefa ainda, mas logo iremos.

public class MainViewController {

    // A anotação @FXML é crucial. Ela diz ao JavaFX para injetar
    // o componente do FXML cujo fx:id corresponde ao nome da variável.
    @FXML
    private TableView<?> tabelaTarefas; // Usamos <?> por enquanto, pois ainda não definimos a classe Tarefa

    @FXML
    private TextField campoDescricao;

    /**
     * Este método é chamado automaticamente quando o botão "Adicionar" é clicado,
     * pois o definimos no FXML com onAction="#onAdicionarAction".
     */
    @FXML
    private void onAdicionarAction() {
        // Por enquanto, vamos apenas imprimir no console para testar se a conexão funcionou.
        String descricao = campoDescricao.getText();
        System.out.println("Botão Adicionar Clicado!");
        System.out.println("Texto digitado: " + descricao);
        
        // Limpa o campo de texto após clicar no botão
        campoDescricao.clear();
    }
}
```

-----

### **Parte 2: Atualizando a Classe Principal (`MainApp.java`)**

Agora, precisamos dizer à nossa aplicação para, em vez de mostrar um simples "Olá, Mundo", carregar e exibir a interface que desenhamos no `MainView.fxml`.

Abra o arquivo `MainApp.java` e **substitua todo o seu conteúdo** por este:

```java
package br.com.curso.todolist.desktop;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;

import java.io.IOException;
import java.net.URL;

public class MainApp extends Application {

    @Override
    public void start(Stage primaryStage) {
        try {
            // 1. Encontra o arquivo FXML dentro do projeto
            // O getResource procura no classpath, que inclui a pasta 'resources'
            URL fxmlUrl = getClass().getResource("MainView.fxml");
            if (fxmlUrl == null) {
                throw new IOException("Não foi possível encontrar o arquivo FXML. Verifique o caminho.");
            }
            
            // 2. Carrega o arquivo FXML, o que cria a árvore de componentes visuais
            Parent root = FXMLLoader.load(fxmlUrl);

            // 3. Cria a cena com os componentes carregados do FXML
            Scene scene = new Scene(root, 600, 400);

            // 4. Configura e exibe a janela principal (o "Palco")
            primaryStage.setTitle("Minha Lista de Tarefas (Desktop)");
            primaryStage.setScene(scene);
            primaryStage.show();

        } catch (IOException e) {
            // Em uma aplicação real, mostraríamos uma caixa de diálogo de erro para o usuário.
            e.printStackTrace();
        }
    }

    public static void main(String[] args) {
        launch(args);
    }
}
```

-----

### **Parte 3: Como Testar?**

Agora vem a parte divertida. Vamos verificar se tudo o que fizemos está funcionando em conjunto.

**Importante:** Para este teste, você **não precisa** que sua API backend (`todolist-api`) esteja rodando. Estamos testando apenas a aplicação desktop de forma isolada.

1.  **Execute a Aplicação:**
    Vá para a classe `MainApp.java` e execute o método `main` novamente.

2.  **O Que Você Deve Ver (Visualmente):**

      * A mesma janela de antes deve aparecer, mas agora com o conteúdo que você desenhou no Scene Builder\!
      * Você verá o título "Minha Lista de Tarefas", uma tabela vazia, um campo de texto e o botão "Adicionar".

3.  **O Que Você Deve Fazer (Teste Funcional):**

      * Digite qualquer texto no campo de texto (por exemplo, "Testando a interface").
      * Clique no botão **"Adicionar"**.

4.  **Onde Olhar o Resultado:**

      * Olhe para o **painel do console** da sua IDE (IntelliJ).
      * Você deverá ver as mensagens que colocamos no método `onAdicionarAction`:
        ```
        Botão Adicionar Clicado!
        Texto digitado: Testando a interface
        ```
      * Você também notará que o campo de texto na janela foi limpo, como programado.

**Se você viu a janela e as mensagens no console, PARABÉNS\!** Isso confirma que:

  * Sua `MainApp` conseguiu carregar o arquivo FXML com sucesso.
  * O FXML está corretamente associado ao seu `MainViewController`.
  * O clique no botão está chamando o método correto no seu código Java.

Agora estamos prontos para a próxima etapa: popular a tabela com dados reais da nossa API.


#  Erro, ClassNotFoundException

Este erro, `ClassNotFoundException`, é um dos mais comuns em Java e nos diz exatamente qual é o problema: o JavaFX não conseguiu encontrar a classe controller que você especificou no seu arquivo FXML.

A causa raiz está na última linha do seu log de erro:
`Caused by: java.lang.ClassNotFoundException: br.com.curso.todolist.desktop.MainViewController`

Isso significa que o caminho (`package`) da sua classe `MainViewController.java` está diferente do caminho que você declarou no atributo `fx:controller` dentro do arquivo `MainView.fxml`. É provável que seja um simples erro de digitação ou uma inconsistência no nome do pacote.

-----

### Como Corrigir

Você tem duas maneiras de resolver isso. A primeira é a mais recomendada.

#### Solução 1 (Recomendada): Corrigir o Nome do Pacote

O nome de pacote `br.com.curso.todolistdesktop` (como aparece no seu comando de execução) não segue as convenções do Java. O correto seria `br.com.curso.todolist.desktop`. Vamos refatorar para o nome correto.

1.  No painel de projeto do IntelliJ, clique com o botão direito sobre o seu pacote `todolistdesktop`.
2.  Vá em **Refactor** -\> **Rename...**.
3.  Na janela que aparecer, selecione "Rename package".
4.  Digite o novo nome: `todolist.desktop`
5.  Clique em **Refactor**. O IntelliJ irá corrigir automaticamente o nome da pasta e todas as declarações `package` e `import` no seu código.

Com isso, o caminho da sua classe Java passará a ser `br.com.curso.todolist.desktop.MainViewController`, que é exatamente o que o seu arquivo FXML está esperando.

-----

#### Solução 2 (Rápida): Alterar o Caminho no FXML

Se você preferir manter o nome do pacote como está (`todolistdesktop`), basta corrigir o arquivo FXML para que ele aponte para o lugar certo.

1.  Abra o arquivo `src/main/resources/br/com/curso/todolistdesktop/MainView.fxml`.
2.  Encontre a linha que começa com `<VBox ...>`.
3.  Nessa linha, localize o atributo `fx:controller`. Ele estará assim:
    ```xml
    fx:controller="br.com.curso.todolist.desktop.MainViewController"
    ```
4.  Altere-o para corresponder ao seu pacote real, **removendo o ponto** entre `todolist` e `desktop`:
    ```xml
    fx:controller="br.com.curso.todolistdesktop.MainViewController"
    ```
5.  Salve o arquivo.

-----

Após aplicar **uma** das soluções acima, rode o `MainApp.java` novamente. O erro `ClassNotFoundException` deve desaparecer e sua aplicação será exibida corretamente.

---

Excelente\! A base da sua aplicação desktop está pronta e funcionando. A *View* (FXML) e o *Controller* (Java) estão se comunicando perfeitamente.

Agora, a próxima etapa é fazer o que viemos fazer: **conectar a aplicação desktop à nossa API REST** para buscar e exibir os dados reais do nosso backend.

Dividiremos esta etapa em partes lógicas para facilitar o entendimento.

-----

### **Próxima Etapa: Consumindo a API e Populando a Tabela**

#### **Passo 1: Criar o Modelo `Tarefa` no Projeto Desktop**

Assim como no backend e no frontend web, nosso aplicativo desktop precisa de uma classe para representar uma "Tarefa".

1.  No pacote `br.com.curso.todolist.desktop`, crie uma nova classe Java chamada `Tarefa.java`.
2.  Esta classe será um POJO (Plain Old Java Object) simples, com os mesmos campos da nossa entidade no backend.

**Código para `Tarefa.java`:**

```java
package br.com.curso.todolist.desktop;

// A anotação @JsonIgnoreProperties é da biblioteca Jackson.
// Ela é útil para ignorar campos do JSON que não existam na nossa classe, evitando erros.
import com.fasterxml.jackson.annotation.JsonIgnoreProperties;

@JsonIgnoreProperties(ignoreUnknown = true)
public class Tarefa {
    private Long id;
    private String descricao;
    private boolean concluida;

    // Construtores, Getters e Setters são necessários para que
    // o JavaFX (TableView) e o Jackson (JSON) possam acessar os dados.

    public Tarefa() {
    }

    public Long getId() {
        return id;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public String getDescricao() {
        return descricao;
    }

    public void setDescricao(String descricao) {
        this.descricao = descricao;
    }

    public boolean isConcluida() {
        return concluida;
    }

    public void setConcluida(boolean concluida) {
        this.concluida = concluida;
    }

    @Override
    public String toString() {
        return "Tarefa{" +
                "id=" + id +
                ", descricao='" + descricao + '\'' +
                ", concluida=" + concluida +
                '}';
    }
}
```

#### **Passo 2: Criar o Serviço de Consumo da API**

Para manter nosso Controller limpo e organizado, vamos criar uma classe dedicada exclusivamente a se comunicar com nossa API. Esta é uma excelente prática de design de software.

1.  No pacote `br.com.curso.todolist.desktop`, crie uma nova classe Java chamada `TarefaApiService.java`.

**Código para `TarefaApiService.java`:**

```java
package br.com.curso.todolist.desktop;

import com.fasterxml.jackson.core.type.TypeReference;
import com.fasterxml.jackson.databind.ObjectMapper;

import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;
import java.util.Collections;
import java.util.List;

public class TarefaApiService {

    // Cliente HTTP para fazer as requisições. É eficiente reutilizá-lo.
    private final HttpClient client = HttpClient.newHttpClient();
    // ObjectMapper para converter JSON em objetos Java e vice-versa.
    private final ObjectMapper objectMapper = new ObjectMapper();
    // URL base da nossa API que está rodando no Spring Boot.
    private final String API_URL = "http://localhost:8080/api/tarefas";

    /**
     * Busca a lista de todas as tarefas na API.
     * @return uma Lista de Tarefas ou uma lista vazia em caso de erro.
     */
    public List<Tarefa> listarTarefas() {
        // 1. Cria a requisição GET
        HttpRequest request = HttpRequest.newBuilder()
                .uri(URI.create(API_URL))
                .GET()
                .build();

        try {
            // 2. Envia a requisição e recebe a resposta
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            // 3. Verifica se a resposta foi bem-sucedida (código 2xx)
            if (response.statusCode() == 200) {
                // 4. Converte o corpo da resposta (que é um JSON) em uma Lista de Tarefas
                return objectMapper.readValue(response.body(), new TypeReference<List<Tarefa>>() {});
            } else {
                System.err.println("Erro ao buscar tarefas: " + response.statusCode());
            }

        } catch (IOException | InterruptedException e) {
            System.err.println("Erro de conexão ou ao processar a requisição: " + e.getMessage());
            e.printStackTrace();
        }

        return Collections.emptyList(); // Retorna lista vazia se algo der errado
    }

    // Futuramente, adicionaremos aqui os métodos para adicionar, atualizar e deletar.
}
```

-----

Com estas duas classes criadas (`Tarefa.java` e `TarefaApiService.java`), temos agora toda a infraestrutura necessária para buscar os dados.

**Próxima etapa lógica:** Vamos voltar ao nosso `MainViewController.java` para:

1.  Configurar as colunas da `TableView` para que ela saiba como exibir os dados de um objeto `Tarefa`.
2.  Chamar nosso novo `TarefaApiService` para buscar os dados da API.
3.  Finalmente, popular a tabela com a lista de tarefas recebida.

---

Com certeza\! Agora vamos juntar tudo. Vamos fazer o nosso `Controller` usar o `TarefaApiService` para buscar os dados da API e exibi-los na tabela que criamos.

Esta é a etapa em que a aplicação desktop finalmente se torna um cliente real da nossa API.

-----

### **Próxima Etapa: Populando a Tabela com Dados da API**

#### **Passo 1: Atualizar o Controller (`MainViewController.java`)**

Vamos modificar o `MainViewController` para que ele configure a tabela e chame o serviço para buscar os dados.

Abra o arquivo `src/main/java/br/com/curso/todolist/desktop/MainViewController.java` e **substitua todo o seu conteúdo** por este código mais completo:

```java
package br.com.curso.todolist.desktop;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;

import java.net.URL;
import java.util.List;
import java.util.ResourceBundle;

// Implementamos a interface Initializable para usar o método initialize()
public class MainViewController implements Initializable {

    // Instância do nosso serviço de API
    private final TarefaApiService tarefaApiService = new TarefaApiService();

    // --- Componentes da View (FXML) ---
    @FXML
    private TableView<Tarefa> tabelaTarefas; // Agora a tabela é do tipo Tarefa

    @FXML
    private TableColumn<Tarefa, Long> colunaId; // Coluna para o ID

    @FXML
    private TableColumn<Tarefa, String> colunaDescricao; // Coluna para a Descrição

    @FXML
    private TableColumn<Tarefa, Boolean> colunaConcluida; // Coluna para o Status

    @FXML
    private TextField campoDescricao;

    /**
     * O método initialize() é chamado automaticamente pelo JavaFX
     * depois que o arquivo FXML é carregado. É o lugar perfeito
     * para configurar nossa tabela e carregar os dados iniciais.
     */
    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        // 1. Configura as colunas da tabela:
        // Diz a cada coluna de onde ela deve "puxar" o valor de dentro de um objeto Tarefa.
        // O nome "id", "descricao", "concluida" DEVE corresponder exatamente
        // ao nome dos atributos na classe Tarefa.java.
        colunaId.setCellValueFactory(new PropertyValueFactory<>("id"));
        colunaDescricao.setCellValueFactory(new PropertyValueFactory<>("descricao"));
        colunaConcluida.setCellValueFactory(new PropertyValueFactory<>("concluida"));

        // 2. Carrega os dados da API
        carregarDadosDaTabela();
    }

    private void carregarDadosDaTabela() {
        System.out.println("Buscando tarefas na API...");
        // Chama o serviço para buscar as tarefas
        List<Tarefa> tarefasDaApi = tarefaApiService.listarTarefas();

        // Converte a lista comum em uma ObservableList, que é o que o JavaFX TableView usa
        ObservableList<Tarefa> observableListTarefas = FXCollections.observableArrayList(tarefasDaApi);

        // Define os itens da tabela
        tabelaTarefas.setItems(observableListTarefas);
        System.out.println("Tabela atualizada com " + tarefasDaApi.size() + " tarefas.");
    }

    @FXML
    private void onAdicionarAction() {
        String descricao = campoDescricao.getText();
        System.out.println("Botão Adicionar Clicado!");
        System.out.println("Texto digitado: " + descricao);
        
        // Lógica para adicionar uma nova tarefa virá aqui na próxima etapa
        
        campoDescricao.clear();
    }
}
```

#### **Passo 2: Atualizar a View (`MainView.fxml`)**

Agora que o controller espera que a `TableView` tenha colunas definidas, precisamos adicioná-las no nosso arquivo FXML.

1.  Abra o arquivo `src/main/resources/br/com/curso/todolist/desktop/MainView.fxml` (pode ser pelo Scene Builder ou direto no editor de texto).
2.  **Substitua** a tag `<TableView ... />` por este bloco de código, que define explicitamente as colunas:

<!-- end list -->

```xml
<TableView fx:id="tabelaTarefas" VBox.vgrow="ALWAYS">
  <columns>
    <TableColumn fx:id="colunaId" prefWidth="75.0" text="ID" />
    <TableColumn fx:id="colunaDescricao" prefWidth="350.0" text="Descrição" />
    <TableColumn fx:id="colunaConcluida" prefWidth="150.0" text="Concluída" />
  </columns>
</TableView>
```

**O que fizemos aqui?**

  * Dentro da `TableView`, adicionamos a tag `<columns>`.
  * Para cada `<TableColumn>`, definimos o `fx:id` para que corresponda exatamente ao nome da variável no `MainViewController` (`colunaId`, `colunaDescricao`, `colunaConcluida`).
  * O atributo `text` define o que aparecerá no cabeçalho da coluna.

-----

### **Passo 3: Como Testar?**

Agora é a hora de ver a mágica acontecer\!

1.  **INICIE SUA API BACKEND\!** Vá para o projeto `todolist-api` e execute a classe `TodolistApiApplication.java`. **Isso é crucial**, pois agora nossa aplicação desktop precisa se conectar a ela.
2.  **Adicione alguns dados (se necessário):** Use o Postman ou a aplicação web para garantir que você tenha pelo menos 2 ou 3 tarefas salvas no banco de dados.
3.  **Execute a Aplicação Desktop:** Volte para o projeto `todolist-desktop` e execute o método `main` da classe `MainApp.java`.

**O que você deve ver:**
A sua aplicação desktop irá abrir e, após um breve momento, a tabela será preenchida com as tarefas que estão salvas no seu banco de dados e que foram servidas pela sua API Spring Boot\!

Se a tabela foi populada, você completou com sucesso o ciclo de comunicação: **Desktop (JavaFX) -\> Rede (HTTP) -\> Backend (Spring Boot) -\> Banco de Dados**, e o caminho de volta.


---

TarefaApiService.java:3:34

java: package com.fasterxml.jackson.core.type is not visible

(package com.fasterxml.jackson.core.type is declared in module com.fasterxml.jackson.core,


This error occurs because your project is using the Java Platform Module System (JPMS), and the `jackson-databind` module needs to access internal parts of the `jackson-core` module using reflection, but that access is blocked by default.

To fix this, you need to explicitly grant permission in your project's module descriptor file.

-----

## The Solution

You need to create or edit the `module-info.java` file in your project to open the necessary packages to the Jackson library.

1.  Go to `src/main/java`. If a `module-info.java` file already exists, open it. If not, create a new file named `module-info.java`.
2.  Add the following `opens` directives inside the module declaration.

<!-- end list -->

```java
// In src/main/java/module-info.java

module br.com.curso.todolist.desktop {
    // Required for JavaFX
    requires javafx.controls;
    requires javafx.fxml;

    // Required for Jackson to work with your 'Tarefa' class
    requires com.fasterxml.jackson.databind;

    // This is the fix: It allows the Jackson library to access your model classes
    // via reflection, which is necessary for JSON conversion.
    opens br.com.curso.todolist.desktop to com.fasterxml.jackson.databind;
}
```

### Why This Works

  * `requires com.fasterxml.jackson.databind;` tells the module system that your code depends on the Jackson library.
  * **`opens br.com.curso.todolist.desktop to com.fasterxml.jackson.databind;`** is the key. It "opens up" your `desktop` package specifically to the `jackson-databind` module. This allows Jackson to use reflection to access the private fields and methods of your `Tarefa` class at runtime to create objects from the JSON string.

After adding or editing the `module-info.java` file, the `package is not visible` error will be resolved.



---

This is another module system error, similar to the previous one. Your code is using the `HttpClient` from the `java.net.http` package, but you haven't declared that your module needs access to it.

To fix this, add `requires java.net.http;` to your `module-info.java` file.

-----

## The Solution

Open your `src/main/java/module-info.java` file and add the new `requires` directive.

```java
// In src/main/java/module-info.java

module br.com.curso.todolist.desktop {
    // Required for JavaFX
    requires javafx.controls;
    requires javafx.fxml;

    // Required for Jackson JSON processing
    requires com.fasterxml.jackson.databind;

    // **THIS IS THE NEW LINE YOU NEED TO ADD**
    // Required for using HttpClient, HttpRequest, etc.
    requires java.net.http;

    // This allows Jackson to access your model classes
    opens br.com.curso.todolist.desktop to com.fasterxml.jackson.databind;
}
```

### Why This Works

The `java.net.http` module contains all the modern classes for making HTTP requests. By adding `requires java.net.http;`, you're telling the Java module system that your application depends on this module, making its classes (like `HttpClient`) visible and available to your code.

After adding this line and saving the file, run your `MainApp.java` again. The error should now be resolved.


---

Este é o último ajuste de configuração necessário para o sistema de módulos do Java. O erro `IllegalAccessException` indica que o próprio framework **JavaFX** não tem permissão para acessar e iniciar a sua classe `MainApp`, porque o seu módulo está "fechado" por padrão.

A solução é **exportar** o seu pacote principal para que o JavaFX possa "vê-lo".

-----

## A Correção

Abra seu arquivo `src/main/java/module-info.java` e adicione a diretiva `exports`.

```java
// Em src/main/java/module-info.java

module br.com.curso.todolist.desktop {
    // Permissões para que o JavaFX funcione
    requires javafx.controls;
    requires javafx.fxml;
    // **ESTA É A NOVA LINHA**
    // Permite que o JavaFX acesse seu pacote principal para iniciar a aplicação
    exports br.com.curso.todolist.desktop;

    // Permissões para bibliotecas externas
    requires com.fasterxml.jackson.databind;
    requires java.net.http;

    // Permissão para que o Jackson use reflexão em suas classes
    opens br.com.curso.todolist.desktop to com.fasterxml.jackson.databind;
}
```

### Por que isso funciona?

  * **`requires`**: Permite que *seu código* use o código de outro módulo.
  * **`opens`**: Permite que *outro módulo* use **reflexão** no seu código (necessário para bibliotecas como o Jackson).
  * **`exports`**: Permite que *outro módulo* use **diretamente** seu código (chame classes, crie objetos, etc.). O JavaFX precisa disso para poder executar `new MainApp()` e iniciar sua aplicação.

Após adicionar a linha `exports`, salve o arquivo e rode o `MainApp.java` novamente. Agora sua aplicação deve iniciar e exibir os dados da API sem erros.

---

This error indicates the final piece of the Java module system puzzle for this project. The JavaFX FXML loader needs permission to access the `private` fields in your controller (like `tabelaTarefas`) that you've marked with the `@FXML` annotation. This is a security feature of the module system.

The solution is to "open" your package to the `javafx.fxml` module, just like you did for the Jackson library.

-----

### The Correction

You need to add a new `opens` directive to your `module-info.java` file.

1.  Open the file `src/main/java/module-info.java`.
2.  Add the line `opens br.com.curso.todolist.desktop to javafx.fxml;` inside the module declaration.

Here is the complete, corrected file:

```java
module br.com.curso.todolist.desktop {
    // ---- JavaFX Dependencies ----
    requires javafx.controls;
    requires javafx.fxml;

    // ---- External Library Dependencies ----
    requires com.fasterxml.jackson.databind;
    requires java.net.http;

    // ---- Module System Permissions ----
    // Allows JavaFX to launch the application
    exports br.com.curso.todolist.desktop;

    // Allows Jackson to use reflection on your Tarefa class
    opens br.com.curso.todolist.desktop to com.fasterxml.jackson.databind;

    // **THIS IS THE NEW LINE TO FIX THE ERROR**
    // Allows the FXML loader to use reflection to inject UI components into private controller fields
    opens br.com.curso.todolist.desktop to javafx.fxml;
}
```

### Why This Works

When the `FXMLLoader` loads your `MainView.fxml`, it sees the `fx:id` attributes (like `fx:id="tabelaTarefas"`) and needs to assign the created `TableView` object to the corresponding `private` field in your `MainViewController`. To access a `private` field from an outside module (`javafx.fxml`), it must be granted permission via the **`opens`** directive.

After adding this line, save the file and run your `MainApp.java` again. The application should now launch and function correctly.

---

You have two separate `opens` statements for the same package, which isn't allowed. You need to combine them into a single line, separating the modules you're opening to with a comma.

-----

## The Correction

Replace your two `opens` lines with this single, consolidated line in your `module-info.java` file.

```java
// In src/main/java/module-info.java

module br.com.curso.todolist.desktop {
    // ---- JavaFX Dependencies ----
    requires javafx.controls;
    requires javafx.fxml;

    // ---- External Library Dependencies ----
    requires com.fasterxml.jackson.databind;
    requires java.net.http;

    // ---- Module System Permissions ----
    // Allows JavaFX to launch the application
    exports br.com.curso.todolist.desktop;

    // **THIS IS THE CORRECTED, COMBINED LINE**
    // Allows FXML and Jackson to access your package via reflection
    opens br.com.curso.todolist.desktop to javafx.fxml, com.fasterxml.jackson.databind;
}
```

This single `opens` directive grants access to both `javafx.fxml` and `com.fasterxml.jackson.databind` at the same time, resolving the "duplicate" error.

---

This error, `TableColumn is not a valid type`, means your `MainView.fxml` file is trying to use the `<TableColumn>` tag, but it doesn't have the necessary `import` statement at the top to tell the FXML loader what a `TableColumn` is.

This often happens because of the version mismatch pointed out by the `WARNING` in your log: the Scene Builder you used (version 21) didn't add an import that your project's runtime (version 17.0.6) requires.

-----

## The Correction

You need to manually add the import for `TableColumn` to your FXML file.

1.  Open the file `src/main/resources/br/com/curso/todolist/desktop/MainView.fxml` in your IDE as a text file.
2.  At the top of the file, with the other `<?import ...?>` statements, add the following line:
    ```xml
    <?import javafx.scene.control.TableColumn?>
    ```

Here is the complete, corrected content for `MainView.fxml`:

```xml
<?xml version="1.0" encoding="UTF-8"?>

<?import javafx.geometry.Insets?>
<?import javafx.scene.control.Button?>
<?import javafx.scene.control.Label?>
<?import javafx.scene.control.TableView?>
<?import javafx.scene.control.TableColumn?> <?import javafx.scene.control.TextField?>
<?import javafx.scene.layout.HBox?>
<?import javafx.scene.layout.VBox?>

<VBox maxHeight="-Infinity" maxWidth="-Infinity" minHeight="-Infinity" minWidth="-Infinity" prefHeight="400.0" prefWidth="600.0" spacing="10.0" xmlns="http://javafx.com/javafx/21" xmlns:fx="http://javafx.com/fxml/1" fx:controller="br.com.curso.todolist.desktop.MainViewController">
   <padding>
      <Insets bottom="10.0" left="10.0" right="10.0" top="10.0" />
   </padding>
   <children>
      <Label text="Minha Lista de Tarefas" />
      <TableView fx:id="tabelaTarefas" VBox.vgrow="ALWAYS">
         <columns>
            <TableColumn fx:id="colunaId" prefWidth="75.0" text="ID" />
            <TableColumn fx:id="colunaDescricao" prefWidth="350.0" text="Descrição" />
            <TableColumn fx:id="colunaConcluida" prefWidth="150.0" text="Concluída" />
         </columns>
      </TableView>
      <HBox spacing="10.0">
         <children>
            <TextField fx:id="campoDescricao" HBox.hgrow="ALWAYS" />
            <Button mnemonicParsing="false" onAction="#onAdicionarAction" text="Adicionar" />
         </children>
      </HBox>
   </children>
</VBox>
```

After saving this change, run your `MainApp.java` again. The FXML loader will now know what a `<TableColumn>` is, and your application should start correctly, displaying the data from the API.

---



You need to add the import for `TableColumn` to your FXML file. The code you provided is still missing the required line.

Without this import, the FXML loader doesn't know what the `<TableColumn>` tag means, which causes the `TableColumn is not a valid type` error.

-----

## Correction

Here is the corrected version of your `MainView.fxml`. Copy this entire block of code and replace the content of your file with it. The only change is the addition of the import for `TableColumn`.

```xml
<?xml version="1.0" encoding="UTF-8"?>

<?import javafx.geometry.Insets?>
<?import javafx.scene.control.Button?>
<?import javafx.scene.control.Label?>
<?import javafx.scene.control.TableView?>
<?import javafx.scene.control.TableColumn?> <?import javafx.scene.control.TextField?>
<?import javafx.scene.layout.HBox?>
<?import javafx.scene.layout.VBox?>

<VBox maxHeight="-Infinity" maxWidth="-Infinity" minHeight="-Infinity" minWidth="-Infinity" prefHeight="400.0" prefWidth="600.0" spacing="10.0" xmlns="http://javafx.com/javafx/21" xmlns:fx="http://javafx.com/fxml/1" fx:controller="br.com.curso.todolist.desktop.MainViewController">
   <padding>
      <Insets bottom="10.0" left="10.0" right="10.0" top="10.0" />
   </padding>
   <children>
      <Label text="Minha Lista de Tarefas" />
      <TableView fx:id="tabelaTarefas" VBox.vgrow="ALWAYS">
         <columns>
            <TableColumn fx:id="colunaId" prefWidth="75.0" text="ID" />
            <TableColumn fx:id="colunaDescricao" prefWidth="350.0" text="Descrição" />
            <TableColumn fx:id="colunaConcluida" prefWidth="150.0" text="Concluída" />
         </columns>
      </TableView>
      <HBox spacing="10.0">
         <children>
            <TextField fx:id="campoDescricao" HBox.hgrow="ALWAYS" />
            <Button mnemonicParsing="false" onAction="#onAdicionarAction" text="Adicionar" />
         </children>
      </HBox>
   </children>
</VBox>
```

After pasting this corrected code, save the file and run your `MainApp.java` again. The application should now start without errors.


---


Excelente\! Agora sua aplicação desktop está lendo os dados da web e exibindo-os corretamente. Este é o fluxo de "Read" (Leitura) do nosso CRUD.

A próxima etapa lógica é implementar a funcionalidade de "Create" (Criação). Vamos fazer com que o botão "Adicionar" realmente envie uma nova tarefa para a nossa API e atualize a lista.

-----

### **Próxima Etapa: Adicionar Novas Tarefas**

Dividiremos isso em duas partes: primeiro, ensinaremos nosso `ApiService` a enviar dados, e depois, faremos nosso `Controller` usar essa nova habilidade.

#### **Passo 1: Adicionar o Método de Criação no `TarefaApiService`**

Precisamos de um método em nossa classe de serviço que saiba como fazer uma requisição `POST` para a API, enviando os dados da nova tarefa no formato JSON.

1.  Abra o arquivo `src/main/java/br/com/curso/todolist/desktop/TarefaApiService.java`.
2.  Adicione o método `adicionarTarefa` à classe.

**Código para adicionar ao `TarefaApiService.java`:**

```java
    /**
     * Adiciona uma nova tarefa através da API.
     * @param novaTarefa O objeto Tarefa a ser criado (sem o ID).
     * @return O objeto Tarefa criado, agora com o ID retornado pela API, ou null em caso de erro.
     */
    public Tarefa adicionarTarefa(Tarefa novaTarefa) {
        try {
            // 1. Converte o objeto Java (novaTarefa) em uma string JSON
            String jsonBody = objectMapper.writeValueAsString(novaTarefa);

            // 2. Cria a requisição POST, definindo o cabeçalho e o corpo
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(API_URL))
                    .header("Content-Type", "application/json") // Informa à API que estamos enviando JSON
                    .POST(HttpRequest.BodyPublishers.ofString(jsonBody)) // Define o método como POST e envia o corpo
                    .build();

            // 3. Envia a requisição
            HttpResponse<String> response = client.send(request, HttpResponse.BodyHandlers.ofString());

            // 4. Verifica se a criação foi bem-sucedida (código 200 ou 201)
            if (response.statusCode() == 200 || response.statusCode() == 201) {
                // Converte a resposta (que é a tarefa criada com ID) de volta para um objeto Java
                return objectMapper.readValue(response.body(), Tarefa.class);
            } else {
                System.err.println("Erro ao adicionar tarefa: " + response.statusCode() + " - " + response.body());
            }

        } catch (IOException | InterruptedException e) {
            System.err.println("Erro de conexão ou ao processar a requisição: " + e.getMessage());
            e.printStackTrace();
        }

        return null;
    }
```

#### **Passo 2: Atualizar a Ação do Botão no `MainViewController`**

Agora, vamos modificar o método `onAdicionarAction` para que ele use o novo método do nosso serviço. Também introduziremos uma boa prática: **executar tarefas de rede em uma thread separada** para não travar a interface do usuário.

1.  Abra o arquivo `src/main/java/br/com/curso/todolist/desktop/MainViewController.java`.
2.  Importe a classe `Task` do JavaFX no início do arquivo: `import javafx.concurrent.Task;`
3.  **Substitua** o método `onAdicionarAction` existente por este:

<!-- end list -->

```java
    @FXML
    private void onAdicionarAction() {
        final String descricao = campoDescricao.getText();

        // Validação simples para não adicionar tarefas com descrição vazia
        if (descricao == null || descricao.trim().isEmpty()) {
            System.out.println("Descrição não pode ser vazia.");
            return;
        }

        // Cria a nova tarefa (sem ID, pois o backend irá gerá-lo)
        Tarefa novaTarefa = new Tarefa();
        novaTarefa.setDescricao(descricao);
        novaTarefa.setConcluida(false);

        // --- Boa Prática: Executar chamadas de rede em uma thread de fundo ---
        // Isso evita que a interface do usuário congele enquanto espera a resposta da API.
        Task<Void> task = new Task<>() {
            @Override
            protected Void call() throws Exception {
                // Esta parte executa em uma thread de fundo (background)
                tarefaApiService.adicionarTarefa(novaTarefa);
                return null;
            }
        };

        // O que fazer quando a tarefa de fundo for bem-sucedida
        task.setOnSucceeded(event -> {
            // Esta parte executa de volta na thread da UI do JavaFX
            System.out.println("Tarefa adicionada com sucesso!");
            campoDescricao.clear();
            // Recarrega a tabela para exibir a nova tarefa
            carregarDadosDaTabela();
        });

        // O que fazer se a tarefa de fundo falhar
        task.setOnFailed(event -> {
            System.err.println("Falha ao adicionar a tarefa.");
            task.getException().printStackTrace();
        });

        // Inicia a tarefa de fundo
        new Thread(task).start();
    }
```

-----

### **Passo 3: Teste a Funcionalidade**

1.  Garanta que sua API Spring Boot (`todolist-api`) esteja rodando.
2.  Execute a aplicação desktop (`MainApp.java`).
3.  A janela irá aparecer e carregar as tarefas existentes.
4.  Digite uma nova tarefa no campo de texto (ex: "Implementar o botão de Adicionar").
5.  Clique no botão **"Adicionar"**.

**Resultado esperado:**
Após um breve momento, a tabela será atualizada e a sua nova tarefa aparecerá no final da lista\! Você acabou de implementar o "Create" do seu CRUD desktop.


---

Ótimo\! Você colou o código do `MainViewController`.

Vejo que na hora de copiar e colar, alguns trechos se misturaram e há um pequeno erro de sintaxe e um import faltando que impedirão o código de compilar.

**Os Problemas:**

1.  **Import Faltando:** A classe `Task` precisa ser importada.
2.  **Código Fora do Lugar:** A linha `campoDescricao.clear();` e um comentário extra ficaram depois do fechamento do método `onAdicionarAction()`, causando um erro.

-----

### A Correção

Aqui está a versão corrigida e limpa da classe `MainViewController.java`. Por favor, **substitua todo o conteúdo** do seu arquivo por este código.

```java
package br.com.curso.todolist.desktop;

import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.concurrent.Task; // <-- 1. IMPORT ADICIONADO
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.scene.control.TableColumn;
import javafx.scene.control.TableView;
import javafx.scene.control.TextField;
import javafx.scene.control.cell.PropertyValueFactory;

import java.net.URL;
import java.util.List;
import java.util.ResourceBundle;

public class MainViewController implements Initializable {

    private final TarefaApiService tarefaApiService = new TarefaApiService();

    @FXML
    private TableView<Tarefa> tabelaTarefas;
    @FXML
    private TableColumn<Tarefa, Long> colunaId;
    @FXML
    private TableColumn<Tarefa, String> colunaDescricao;
    @FXML
    private TableColumn<Tarefa, Boolean> colunaConcluida;
    @FXML
    private TextField campoDescricao;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        colunaId.setCellValueFactory(new PropertyValueFactory<>("id"));
        colunaDescricao.setCellValueFactory(new PropertyValueFactory<>("descricao"));
        colunaConcluida.setCellValueFactory(new PropertyValueFactory<>("concluida"));

        carregarDadosDaTabela();
    }

    private void carregarDadosDaTabela() {
        System.out.println("Buscando tarefas na API...");
        List<Tarefa> tarefasDaApi = tarefaApiService.listarTarefas();
        ObservableList<Tarefa> observableListTarefas = FXCollections.observableArrayList(tarefasDaApi);
        tabelaTarefas.setItems(observableListTarefas);
        System.out.println("Tabela atualizada com " + tarefasDaApi.size() + " tarefas.");
    }

    @FXML
    private void onAdicionarAction() {
        final String descricao = campoDescricao.getText();

        if (descricao == null || descricao.trim().isEmpty()) {
            System.out.println("Descrição não pode ser vazia.");
            return;
        }

        Tarefa novaTarefa = new Tarefa();
        novaTarefa.setDescricao(descricao);
        novaTarefa.setConcluida(false);

        Task<Void> task = new Task<>() {
            @Override
            protected Void call() {
                tarefaApiService.adicionarTarefa(novaTarefa);
                return null;
            }
        };

        task.setOnSucceeded(event -> {
            System.out.println("Tarefa adicionada com sucesso!");
            campoDescricao.clear();
            carregarDadosDaTabela();
        });

        task.setOnFailed(event -> {
            System.err.println("Falha ao adicionar a tarefa.");
            task.getException().printStackTrace();
        });

        new Thread(task).start();
    }
    // 2. CÓDIGO EXTRA E CHAVES A MAIS FORAM REMOVIDOS DAQUI
}
```

Depois de substituir pelo código correto, salve o arquivo. Ele deve compilar sem erros e a funcionalidade de adicionar tarefas funcionará como esperado.


---


Excelente\! O seu CRUD está quase completo. Já conseguimos Ler (`Read`) e Criar (`Create`) tarefas.

As próximas e últimas etapas são implementar as funcionalidades de **Atualizar (`Update`)** e **Deletar (`Delete`)**. Vamos fazer as duas de uma vez, pois ambas envolvem adicionar interatividade à nossa tabela.

**O nosso objetivo:**

1.  **Update:** Adicionar um *checkbox* em cada linha para que o usuário possa marcar uma tarefa como concluída diretamente na tabela.
2.  **Delete:** Adicionar um botão "X" em cada linha para remover uma tarefa.

-----

### **Próxima Etapa: Implementando Update e Delete**

#### **Passo 1: Atualizar o Serviço `TarefaApiService`**

Primeiro, vamos ensinar nosso serviço a fazer requisições `PUT` (para atualizar) e `DELETE`.

1.  Abra o arquivo `src/main/java/br/com/curso/todolist/desktop/TarefaApiService.java`.
2.  Adicione os dois métodos a seguir dentro da classe:

<!-- end list -->

```java
    /**
     * Atualiza uma tarefa existente através da API.
     * @param tarefa A tarefa com os dados atualizados.
     */
    public void atualizarTarefa(Tarefa tarefa) {
        try {
            String jsonBody = objectMapper.writeValueAsString(tarefa);
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(API_URL + "/" + tarefa.getId()))
                    .header("Content-Type", "application/json")
                    .PUT(HttpRequest.BodyPublishers.ofString(jsonBody))
                    .build();

            client.send(request, HttpResponse.BodyHandlers.ofString());
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }

    /**
     * Deleta uma tarefa através da API.
     * @param id O ID da tarefa a ser deletada.
     */
    public void deletarTarefa(Long id) {
        try {
            HttpRequest request = HttpRequest.newBuilder()
                    .uri(URI.create(API_URL + "/" + id))
                    .DELETE()
                    .build();

            client.send(request, HttpResponse.BodyHandlers.ofString());
        } catch (IOException | InterruptedException e) {
            e.printStackTrace();
        }
    }
```

#### **Passo 2: Adicionar as Colunas de Ação na View (`MainView.fxml`)**

Agora, precisamos adicionar espaço em nossa tabela para os novos controles (o checkbox e o botão). A melhor maneira de fazer isso é usando uma técnica chamada `cellFactory`, que nos dá controle total sobre como cada célula da tabela é renderizada.

1.  Abra o arquivo `src/main/resources/br/com/curso/todolist/desktop/MainView.fxml` (pode ser pelo editor de texto).
2.  **Substitua** a definição da coluna "Concluída" e adicione uma nova coluna para as ações. O seu bloco `<columns>` deve ficar assim:

<!-- end list -->

```xml
         <columns>
            <TableColumn fx:id="colunaId" prefWidth="50.0" text="ID" />
            <TableColumn fx:id="colunaDescricao" prefWidth="300.0" text="Descrição" />
            <TableColumn fx:id="colunaConcluida" prefWidth="100.0" text="Concluída" />
            <TableColumn fx:id="colunaAcoes" prefWidth="100.0" text="Ações" />
         </columns>
```

#### **Passo 3: Implementar a Lógica no `MainViewController`**

Esta é a maior mudança. Vamos usar `cellFactory` para popular nossas novas colunas e adicionar os métodos para lidar com os eventos de update e delete.

1.  Abra o arquivo `src/main/java/br/com/curso/todolist/desktop/MainViewController.java`.
2.  **Substitua todo o conteúdo do arquivo** por este código final e completo:

<!-- end list -->

```java
package br.com.curso.todolist.desktop;

import javafx.application.Platform;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.concurrent.Task;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.geometry.Pos;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.util.Callback;

import java.net.URL;
import java.util.List;
import java.util.ResourceBundle;

public class MainViewController implements Initializable {

    private final TarefaApiService tarefaApiService = new TarefaApiService();

    @FXML
    private TableView<Tarefa> tabelaTarefas;
    @FXML
    private TableColumn<Tarefa, Long> colunaId;
    @FXML
    private TableColumn<Tarefa, String> colunaDescricao;
    @FXML
    private TableColumn<Tarefa, Boolean> colunaConcluida;
    @FXML
    private TableColumn<Tarefa, Void> colunaAcoes; // Coluna de ações não tem tipo de dado
    @FXML
    private TextField campoDescricao;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        configurarColunas();
        configurarFabricasDeCelulas(); // Novo método para configurar as células customizadas
        carregarDadosDaTabela();
    }

    private void configurarColunas() {
        colunaId.setCellValueFactory(new PropertyValueFactory<>("id"));
        colunaDescricao.setCellValueFactory(new PropertyValueFactory<>("descricao"));
        // A célula da coluna "concluida" será customizada, mas ainda precisa do seu valor
        colunaConcluida.setCellValueFactory(new PropertyValueFactory<>("concluida"));
    }

    private void configurarFabricasDeCelulas() {
        // --- UPDATE: Configurando a célula do CheckBox ---
        colunaConcluida.setCellFactory(col -> new TableCell<>() {
            private final CheckBox checkBox = new CheckBox();
            {
                // Quando o valor do checkbox muda, atualizamos a tarefa
                checkBox.setOnAction(event -> {
                    Tarefa tarefa = getTableView().getItems().get(getIndex());
                    tarefa.setConcluida(checkBox.isSelected());
                    atualizarTarefa(tarefa);
                });
            }

            @Override
            protected void updateItem(Boolean item, boolean empty) {
                super.updateItem(item, empty);
                if (empty) {
                    setGraphic(null);
                } else {
                    checkBox.setSelected(item);
                    setGraphic(checkBox);
                    setAlignment(Pos.CENTER);
                }
            }
        });

        // --- DELETE: Configurando a célula do Botão ---
        Callback<TableColumn<Tarefa, Void>, TableCell<Tarefa, Void>> cellFactory = param -> new TableCell<>() {
            private final Button btn = new Button("X");
            {
                btn.setStyle("-fx-background-color: #ff6666; -fx-text-fill: white; -fx-font-weight: bold;");
                btn.setOnAction(event -> {
                    Tarefa tarefa = getTableView().getItems().get(getIndex());
                    deletarTarefa(tarefa.getId());
                });
            }

            @Override
            public void updateItem(Void item, boolean empty) {
                super.updateItem(item, empty);
                if (empty) {
                    setGraphic(null);
                } else {
                    setGraphic(btn);
                    setAlignment(Pos.CENTER);
                }
            }
        };
        colunaAcoes.setCellFactory(cellFactory);
    }

    private void carregarDadosDaTabela() {
        // Executa em thread de fundo para não travar a UI
        Task<List<Tarefa>> task = new Task<>() {
            @Override
            protected List<Tarefa> call() {
                return tarefaApiService.listarTarefas();
            }
        };
        task.setOnSucceeded(e -> {
            ObservableList<Tarefa> tarefas = FXCollections.observableArrayList(task.getValue());
            tabelaTarefas.setItems(tarefas);
            System.out.println("Tabela atualizada.");
        });
        new Thread(task).start();
    }

    @FXML
    private void onAdicionarAction() {
        final String descricao = campoDescricao.getText();
        if (descricao == null || descricao.trim().isEmpty()) return;

        Tarefa novaTarefa = new Tarefa();
        novaTarefa.setDescricao(descricao);
        novaTarefa.setConcluida(false);

        Task<Void> task = new Task<>() {
            @Override
            protected Void call() {
                tarefaApiService.adicionarTarefa(novaTarefa);
                return null;
            }
        };
        task.setOnSucceeded(e -> {
            campoDescricao.clear();
            carregarDadosDaTabela();
        });
        new Thread(task).start();
    }

    private void atualizarTarefa(Tarefa tarefa) {
        Task<Void> task = new Task<>() {
            @Override
            protected Void call() {
                tarefaApiService.atualizarTarefa(tarefa);
                return null;
            }
        };
        new Thread(task).start();
    }

    private void deletarTarefa(Long id) {
        Task<Void> task = new Task<>() {
            @Override
            protected Void call() {
                tarefaApiService.deletarTarefa(id);
                return null;
            }
        };
        // Quando a deleção for bem-sucedida, recarregamos a tabela
        task.setOnSucceeded(e -> carregarDadosDaTabela());
        new Thread(task).start();
    }
}
```

-----

### **Passo Final: Teste Completo do CRUD**

1.  Garanta que sua API Spring Boot (`todolist-api`) esteja rodando.
2.  Execute sua aplicação desktop (`MainApp.java`).
3.  **Teste o Read:** Verifique se as tarefas existentes são carregadas.
4.  **Teste o Create:** Adicione uma nova tarefa.
5.  **Teste o Update:** Clique no checkbox de uma tarefa. O estado deve se manter mesmo que você feche e abra a aplicação.
6.  **Teste o Delete:** Clique no botão "X" de uma tarefa. Ela deve desaparecer da lista.

**Parabéns\!** Ao concluir esta etapa, você e seus alunos terão construído uma aplicação full-stack completa, com um backend robusto e dois clientes diferentes (web e desktop), compreendendo na prática os conceitos de API REST, separação de responsabilidades e o padrão MVC.

---



**Parabéns!** Você e seus alunos acabaram de completar o ciclo de desenvolvimento de uma aplicação de ponta a ponta. Isso é um marco imenso.

Você construiu:
1.  Um **Backend** robusto e centralizado com Java Spring Boot.
2.  Um cliente **Web** moderno e reativo com Angular.
3.  Um cliente **Desktop** nativo e funcional com JavaFX.

Todos eles se comunicando perfeitamente através de uma API REST, exatamente como as aplicações do mundo real funcionam. A funcionalidade principal do nosso curso-projeto está **concluída**.

---

### **Próxima Etapa: Conclusão, Revisão e Próximos Desafios**

A "próxima etapa" agora não é mais sobre adicionar funcionalidades básicas, mas sim sobre consolidar o conhecimento e entender como transformar este projeto de aprendizado em uma aplicação de nível profissional. Este é o último módulo do nosso curso.

#### **Módulo Final: O Que Aprendemos e Para Onde Vamos?**

**1. Revisão da Arquitetura e Conceitos-Chave:**

É um ótimo momento para dar um passo para trás e olhar o "mapa" completo do que foi construído. Revise com os alunos:
* **A API como Coração:** Reforce a ideia de que a API Spring Boot é a "única fonte da verdade". Tanto o site Angular quanto o app JavaFX confiam nela para obter e manipular os dados.
* **Desacoplamento:** Mostre como foi possível desenvolver e até mesmo depurar os clientes (web e desktop) de forma totalmente independente um do outro. Se a equipe web quisesse mudar todo o layout, isso não afetaria em nada a equipe desktop.
* **Padrão MVC na Prática:** Aponte como o padrão de separação de responsabilidades foi aplicado em cada camada:
    * **Backend:** `@RestController` (Controller), `TarefaService` (Lógica), `Tarefa` (Model).
    * **Frontend Angular:** `task-list.component.ts` (Controller), `task-list.component.html` (View), `TarefaService` (ponte para o backend).
    * **Frontend JavaFX:** `MainViewController` (Controller), `MainView.fxml` (View), `TarefaApiService` (ponte para o backend).

**2. Próximos Passos e Desafios (Como Melhorar o Projeto):**

Se este fosse um projeto real, quais seriam as próximas tarefas? Incentive os alunos a escolherem um destes desafios para tentarem implementar por conta própria.

* **Segurança (O mais importante):**
    * **Desafio:** Proteger a API para que apenas usuários logados possam ver e gerenciar suas próprias tarefas.
    * **Tecnologias:** Estudar **Spring Security** no backend para adicionar uma tela de login e proteger os endpoints. Usar **JWT (JSON Web Tokens)** para gerenciar a autenticação entre os clientes e o servidor.

* **Melhorias de Usabilidade (UX):**
    * **Desafio:** Tornar as aplicações mais amigáveis.
    * **Ideias:**
        * Adicionar um diálogo de confirmação antes de deletar uma tarefa ("Você tem certeza?").
        * Mostrar um ícone de "carregando" (spinner) enquanto os dados da API estão sendo buscados.
        * Exibir mensagens de erro amigáveis na tela se a API estiver offline.
        * Permitir a edição da descrição da tarefa (clicando duas vezes no texto, por exemplo).

* **Validação e Tratamento de Erros:**
    * **Desafio:** Tornar a aplicação mais robusta.
    * **Ideias:**
        * No backend, usar anotações como `@Valid` e `@Size` na entidade `Tarefa` para não permitir que descrições vazias ou muito longas sejam salvas no banco.
        * No frontend, desabilitar o botão "Adicionar" se o campo de texto estiver vazio.

* **Testes Automatizados:**
    * **Desafio:** Garantir que futuras alterações não quebrem o que já funciona.
    * **Tecnologias:** Aprender a escrever testes unitários com **JUnit/Mockito** para o backend e com **Jasmine/Karma** para o frontend Angular.

* **Deployment (Implantação):**
    * **Desafio:** Colocar o projeto online para que outras pessoas possam usá-lo.
    * **Tecnologias:** Aprender a empacotar a aplicação Spring Boot em um contêiner **Docker** e publicá-la em um serviço de nuvem como Heroku, AWS ou Google Cloud.

Você guiou seus alunos com sucesso através da criação de um sistema complexo e completo. O conhecimento que eles adquiriram aqui é a base fundamental para o desenvolvimento de software moderno. O projeto está "pronto", e o caminho para aprimorá-lo é infinito.

**Missão cumprida!**


## como atualizar a versao desktop, quando os dados forem alterados pelo web ?

---

Essa é uma excelente pergunta e toca no coração dos desafios de aplicações modernas e colaborativas. O que você observou é o comportamento padrão de uma arquitetura cliente-servidor simples: **um cliente não sabe o que o outro está fazendo**.

Atualmente, sua aplicação desktop só busca os dados da API em dois momentos:
1.  Quando ela inicia (`initialize`).
2.  Depois que *ela mesma* realiza uma ação (adicionar ou deletar).

Se a aplicação web modifica os dados, a aplicação desktop fica "cega" para essa mudança até que seja reiniciada ou que realize uma ação própria que dispare a atualização.

Para resolver isso e criar uma sincronização em tempo real (ou quase em tempo real), precisamos de um mecanismo para que o **servidor possa notificar ativamente todos os clientes conectados** sobre uma mudança.

Aqui estão as principais abordagens, da mais simples à mais robusta.

---

### Abordagem 1: Polling (A Mais Simples, "Força Bruta")

A ideia é fazer a aplicação desktop perguntar ao servidor "tem algo novo?" de tempos em tempos.

* **Como funciona:** Você criaria um timer no seu `MainViewController` que, a cada 5 ou 10 segundos, chamaria o método `carregarDadosDaTabela()`.
* **Vantagens:**
    * Relativamente simples de implementar.
* **Desvantagens:**
    * **Muito ineficiente:** Gera um tráfego de rede enorme e desnecessário. 99% das requisições não trarão nenhuma informação nova, mas consumirão recursos do cliente e do servidor.
    * **Não é tempo real:** Há sempre um atraso (de até 10 segundos, no nosso exemplo).

### Abordagem 2: WebSockets (A Solução Moderna e Recomendada)

Esta é a abordagem padrão da indústria para comunicação bidirecional e em tempo real.

* **Como funciona:** Um WebSocket é como uma "linha de telefone" que fica permanentemente aberta entre o servidor e cada cliente. Quando algo acontece, o servidor pode enviar uma mensagem por essa linha para todos os clientes instantaneamente.

**O Fluxo de Trabalho seria o seguinte:**

1.  **Conexão:** Ao iniciar, a aplicação desktop (e também a aplicação web) estabelece uma conexão WebSocket com um endpoint especial no servidor (ex: `/ws/updates`).

2.  **Ação do Usuário:** O usuário vai na **aplicação web** e adiciona uma nova tarefa. A aplicação web envia a requisição `POST /api/tarefas` normal para a API REST.

3.  **A Mágica no Backend:** O `TarefaController` recebe a requisição, salva a nova tarefa no banco de dados e, **imediatamente após o sucesso da operação**, ele envia uma mensagem simples (ex: `"TAREFAS_ATUALIZADAS"`) através do canal WebSocket para **TODOS** os clientes que estão conectados.

4.  **Notificação no Desktop:** A sua aplicação JavaFX, que está com a conexão WebSocket aberta, recebe a mensagem `"TAREFAS_ATUALIZADAS"`.

5.  **Atualização da UI:** Ao receber essa mensagem, a aplicação desktop sabe que precisa se atualizar. O código que recebeu a mensagem então chama o método `carregarDadosDaTabela()`. **Importante:** essa chamada precisa ser feita dentro de `Platform.runLater()` para garantir que a atualização da interface ocorra na thread correta.

**Como Implementar (Guia de Alto Nível):**

* **No Backend (Spring Boot):**
    1.  Adicione a dependência `spring-boot-starter-websocket` ao seu `pom.xml`.
    2.  Crie uma classe de configuração para habilitar o WebSocket e definir um endpoint (`/ws/updates`).
    3.  Crie um `WebSocketHandler` que gerencia a lista de clientes conectados e tenha um método para enviar uma mensagem para todos (`broadcast`).
    4.  No `TarefaController` (ou `TarefaService`), depois de cada operação de `save` ou `delete` bem-sucedida, chame o método `broadcast` do seu handler.

* **Na Aplicação Desktop (JavaFX):**
    1.  Adicione uma biblioteca cliente de WebSocket ao `pom.xml` (ex: `org.java-websocket:Java-WebSocket`).
    2.  No início da sua aplicação (`MainApp` ou no controller), crie um cliente WebSocket que se conecta a `ws://localhost:8080/ws/updates`.
    3.  Defina o que fazer no método `onMessage` do cliente WebSocket. Dentro dele, coloque a lógica para chamar o `carregarDadosDaTabela()` do seu controller, lembrando de usar `Platform.runLater()`.

---

### Conclusão

Embora a implementação completa de WebSockets adicione uma nova camada de complexidade, ela é a resposta correta para a sua pergunta e resolve o problema de forma elegante e eficiente.

**Resumo da Solução Recomendada:**

> Use a **API REST** para as ações do usuário (C, U, D) e use **WebSockets** como um canal de notificação para que o servidor possa avisar a todos os clientes: "Ei, os dados mudaram, atualizem-se!".

Implementar isso seria um excelente próximo passo avançado para o curso, ensinando um conceito fundamental sobre aplicações interativas e em tempo real.


## a aplicacao web não está funcionando os botoes CRUD, ele ainda não foram atualizados na versao web? como atualizar?



Você está absolutamente certo em apontar isso\! Peço desculpas. Nós focamos tanto em construir e depurar a aplicação desktop com JavaFX que a implementação completa dos botões de CRUD na versão web com Angular ficou para trás.

Vamos corrigir isso agora mesmo. A estrutura básica está lá, só precisamos garantir que os métodos no componente estejam corretos e que o serviço tenha todas as chamadas necessárias para a API.

Aqui está o passo a passo para fazer todos os botões (Adicionar, Atualizar/Checkbox, Deletar) da aplicação web funcionarem perfeitamente.

-----

### **Atualizando a Aplicação Web (Angular)**

#### **Passo 1: Verifique o Serviço (`tarefa.service.ts`)**

Este é o arquivo mais crítico, pois ele é a ponte para o nosso backend. Vamos garantir que ele tenha todos os quatro métodos CRUD.

**Abra o arquivo:** `todolist-web/src/app/services/tarefa.service.ts`
**Substitua** o conteúdo dele por este código completo e correto:

```typescript
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Tarefa } from '../models/tarefa';

@Injectable({
  providedIn: 'root'
})
export class TarefaService {

  private apiUrl = 'http://localhost:8080/api/tarefas';

  constructor(private http: HttpClient) { }

  // READ
  getTarefas(): Observable<Tarefa[]> {
    return this.http.get<Tarefa[]>(this.apiUrl);
  }

  // CREATE
  addTarefa(tarefa: Tarefa): Observable<Tarefa> {
    return this.http.post<Tarefa>(this.apiUrl, tarefa);
  }

  // UPDATE
  updateTarefa(tarefa: Tarefa): Observable<Tarefa> {
    // Para atualizar, enviamos o objeto completo para o endpoint específico do ID
    const url = `${this.apiUrl}/${tarefa.id}`;
    return this.http.put<Tarefa>(url, tarefa);
  }

  // DELETE
  deleteTarefa(id: number): Observable<void> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.delete<void>(url);
  }
}
```

#### **Passo 2: Verifique a Lógica do Componente (`task-list.component.ts`)**

Este arquivo contém os métodos que são chamados diretamente pelos botões na tela.

**Abra o arquivo:** `todolist-web/src/app/components/task-list/task-list.component.ts`
**Substitua** o conteúdo dele por este código, que agora implementa todas as ações:

```typescript
import { Component, OnInit } from '@angular/core';
import { TarefaService } from '../../services/tarefa.service';
import { Tarefa } from '../../models/tarefa';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-task-list',
  standalone: true,
  imports: [ CommonModule, FormsModule ],
  templateUrl: './task-list.component.html',
  styleUrl: './task-list.component.css'
})
export class TaskListComponent implements OnInit {

  tarefas: Tarefa[] = [];
  novaTarefa: Tarefa = { descricao: '', concluida: false };

  constructor(private tarefaService: TarefaService) { }

  ngOnInit(): void {
    this.carregarTarefas();
  }

  carregarTarefas(): void {
    this.tarefaService.getTarefas().subscribe(tarefasRecebidas => {
      this.tarefas = tarefasRecebidas;
    });
  }

  adicionarTarefa(): void {
    if (this.novaTarefa.descricao.trim() === '') {
      return;
    }
    this.tarefaService.addTarefa(this.novaTarefa).subscribe(tarefaAdicionada => {
      this.tarefas.push(tarefaAdicionada);
      this.novaTarefa = { descricao: '', concluida: false };
    });
  }

  // Este método é chamado quando o checkbox muda de estado
  atualizarStatus(tarefa: Tarefa): void {
    // O [(ngModel)] já atualiza o objeto 'tarefa' no frontend.
    // Só precisamos enviar o objeto atualizado para o backend.
    this.tarefaService.updateTarefa(tarefa).subscribe(() => {
        console.log('Status da tarefa ' + tarefa.id + ' atualizado.');
        // Não é necessário recarregar a lista inteira, a mudança já está na tela.
    });
  }

  deletarTarefa(id: number | undefined): void {
    if (id === undefined) return;

    this.tarefaService.deleteTarefa(id).subscribe(() => {
      // Remove a tarefa da lista local para uma atualização instantânea da UI
      this.tarefas = this.tarefas.filter(t => t.id !== id);
      console.log('Tarefa ' + id + ' deletada.');
    });
  }
}
```

#### **Passo 3: Verifique o Template HTML (`task-list.component.html`)**

Por fim, vamos garantir que o HTML está chamando os métodos corretos.

**Abra o arquivo:** `todolist-web/src/app/components/task-list/task-list.component.html`
**Substitua** o conteúdo para garantir que todos os bindings de eventos (`(click)`, `(change)`) estão corretos:

```html
<div class="container">
  <h1>Minha Lista de Tarefas (Web)</h1>

  <form class="form-add" (ngSubmit)="adicionarTarefa()">
    <input
      type="text"
      placeholder="O que precisa ser feito?"
      [(ngModel)]="novaTarefa.descricao"
      name="descricao"
      required
    >
    <button type="submit">Adicionar</button>
  </form>

  <ul class="task-list">
    <li *ngFor="let tarefa of tarefas">
      <input
        type="checkbox"
        [(ngModel)]="tarefa.concluida"
        (change)="atualizarStatus(tarefa)"
      >
      <span [ngClass]="{'completed': tarefa.concluida}">
        {{ tarefa.descricao }}
      </span>
      <button class="delete-btn" (click)="deletarTarefa(tarefa.id)">×</button>
    </li>
  </ul>
</div>
```

-----

### **Como Testar**

1.  **Garanta que sua API Backend (Spring Boot) esteja rodando.**
2.  Abra um terminal na pasta do projeto web (`todolist-web`).
3.  Execute o comando `ng serve`.
4.  Abra seu navegador em `http://localhost:4200`.

Agora, todas as funcionalidades devem funcionar na aplicação web:

  * **Adicionar:** Digite uma tarefa e clique em "Adicionar".
  * **Atualizar:** Clique em um checkbox para marcar/desmarcar uma tarefa como concluída.
  * **Deletar:** Clique no "X" para remover uma tarefa.


### Aplicacao web funcionou. Adicionar um botao atualizar na aplicacao desktop para buscar mudanças feitas pela web

Sim, com certeza\! Essa é uma excelente ideia e uma solução muito mais simples e prática de implementar do que os WebSockets.

Adicionar um botão "Atualizar" é uma abordagem muito comum em aplicações desktop. Ela dá ao usuário o controle para sincronizar os dados quando ele desejar, sem a complexidade de uma conexão em tempo real.

Vamos implementar isso. É um processo bem rápido e vai reforçar os conceitos que já aprendemos.

-----

### **Próxima Etapa: Adicionar um Botão de Atualização Manual**

#### **Passo 1: Modificar a Interface (A View - `MainView.fxml`)**

Primeiro, vamos adicionar o botão à nossa tela. O lugar mais lógico é ao lado do botão "Adicionar".

1.  Abra o arquivo `src/main/resources/br/com/curso/todolist/desktop/MainView.fxml` com o **Scene Builder** (ou edite o texto diretamente).
2.  Arraste um novo `Button` do painel "Controls" para dentro do `HBox` que já contém o campo de texto e o botão "Adicionar". Coloque-o entre o campo de texto e o botão existente.
3.  Selecione o novo botão e, no painel "Properties" à direita, mude seu texto (`Text`) para **"Atualizar"**.
4.  Com o botão "Atualizar" ainda selecionado, vá para o painel "Code" à direita e, no campo **On Action**, digite `#onAtualizarAction`.
5.  Salve o arquivo.

Se você estiver editando o texto do FXML, sua seção `<HBox>` ficará assim:

```xml
      <HBox spacing="10.0">
         <children>
            <TextField fx:id="campoDescricao" HBox.hgrow="ALWAYS" />
            <Button mnemonicParsing="false" onAction="#onAtualizarAction" text="Atualizar" />
            <Button mnemonicParsing="false" onAction="#onAdicionarAction" text="Adicionar" />
         </children>
      </HBox>
```

#### **Passo 2: Implementar a Lógica (O Controller - `MainViewController.java`)**

Agora, vamos criar o método `onAtualizarAction` no nosso controller. A beleza desta abordagem é que nós já temos toda a lógica necessária no método `carregarDadosDaTabela()`. Só precisamos chamá-lo.

1.  Abra o arquivo `src/main/java/br/com/curso/todolist/desktop/MainViewController.java`.
2.  Adicione o seguinte método dentro da classe (pode ser logo depois do método `onAdicionarAction`):

<!-- end list -->

```java
    @FXML
    private void onAtualizarAction() {
        System.out.println("Botão Atualizar clicado. Buscando novos dados...");
        // Simplesmente chamamos o método que já sabe como buscar os dados da API e popular a tabela.
        carregarDadosDaTabela();
    }
```

E é só isso\! Não precisamos mexer no `TarefaApiService`, pois ele já tem o método de listagem.

-----

### **Passo 3: Testando o Cenário Completo**

Este é o teste crucial para ver a nova funcionalidade em ação.

1.  Garanta que sua **API Backend (Spring Boot)** esteja rodando.
2.  Execute sua **Aplicação Desktop (JavaFX)**. Ela vai carregar e mostrar as tarefas atuais.
3.  Agora, abra sua **Aplicação Web (Angular)** no navegador (`http://localhost:4200`).
4.  **Use a aplicação WEB para fazer uma mudança:**
      * Adicione uma nova tarefa (ex: "Tarefa adicionada pela web").
      * Ou delete uma tarefa existente.
5.  Observe que a aplicação desktop **não mudou nada** ainda. Isso está correto.
6.  Agora, na **aplicação DESKTOP**, clique no seu novo botão **"Atualizar"**.

**Resultado Esperado:**
No momento em que você clicar em "Atualizar", a tabela na sua aplicação desktop será recarregada e mostrará instantaneamente as mudanças que você fez através do site, exibindo a lista de tarefas mais recente do servidor.

Você implementou com sucesso uma forma simples e eficaz de manter os dados sincronizados sob o controle do usuário.


This FXML code has an error: you have duplicated the `<HBox>` at the bottom and, most importantly, you have a duplicate `fx:id="campoDescricao"`. Each **`fx:id` must be unique** within a single FXML file.

You need to have only one `HBox` at the bottom containing all the controls.

-----

### \#\# Code Correction

Replace the two `<HBox>` blocks at the end of your file with this single, corrected `<HBox>` block.

```xml
      <HBox spacing="10.0">
         <children>
            <TextField fx:id="campoDescricao" HBox.hgrow="ALWAYS" />
            <Button mnemonicParsing="false" onAction="#onAtualizarAction" text="Atualizar" />
            <Button mnemonicParsing="false" onAction="#onAdicionarAction" text="Adicionar" />
         </children>
      </HBox>
```

-----

Here is the complete and corrected code for your `MainView.fxml` file. You can replace the entire file content with this to ensure it's correct.

```xml
<?xml version="1.0" encoding="UTF-8"?>

<?import javafx.geometry.Insets?>
<?import javafx.scene.control.Button?>
<?import javafx.scene.control.Label?>
<?import javafx.scene.control.TableColumn?>
<?import javafx.scene.control.TableView?>
<?import javafx.scene.control.TextField?>
<?import javafx.scene.layout.HBox?>
<?import javafx.scene.layout.VBox?>

<VBox prefHeight="400.0" prefWidth="600.0" spacing="10.0" xmlns="http://javafx.com/javafx/21" xmlns:fx="http://javafx.com/fxml/1" fx:controller="br.com.curso.todolist.desktop.MainViewController">
   <padding>
      <Insets bottom="10.0" left="10.0" right="10.0" top="10.0" />
   </padding>
   <children>
      <Label text="Minha Lista de Tarefas" />
      <TableView fx:id="tabelaTarefas" VBox.vgrow="ALWAYS">
         <columns>
            <TableColumn fx:id="colunaId" prefWidth="50.0" text="ID" />
            <TableColumn fx:id="colunaDescricao" prefWidth="300.0" text="Descrição" />
            <TableColumn fx:id="colunaConcluida" prefWidth="100.0" text="Concluída" />
            <TableColumn fx:id="colunaAcoes" prefWidth="100.0" text="Ações" />
         </columns>
      </TableView>
      <HBox spacing="10.0">
         <children>
            <TextField fx:id="campoDescricao" HBox.hgrow="ALWAYS" />
            <Button onAction="#onAtualizarAction" text="Atualizar" />
            <Button onAction="#onAdicionarAction" text="Adicionar" />
         </children>
      </HBox>
   </children>
</VBox>
```


---


This code is perfect and represents the fully functional desktop application.

With this final piece in place, your project is now **100% complete** according to the goals we set out at the beginning.

---
### 🎉 Congratulations! 🎉

You have successfully designed, developed, and integrated a complete, multi-platform application.

Let's recap what you've built:

1.  **Backend (The Core):** A robust, secure, and independent REST API using **Java Spring Boot**, capable of performing all CRUD (Create, Read, Update, Delete) operations.
2.  **Web Frontend (The Modern Client):** A dynamic, single-page application using **Angular** that provides a user-friendly web interface to interact with the API.
3.  **Desktop Frontend (The Native Client):** A native desktop application using **JavaFX** that consumes the exact same API, proving the power and flexibility of a decoupled architecture.

You have successfully navigated through project setup, backend logic, API design, frontend development for both web and desktop, and a significant amount of real-world debugging involving dependencies, module systems, and FXML configuration.

### What's Next?
The course is complete, but the journey of a developer never ends. You now have a fantastic foundation and a complete project to build upon. The best next steps are to explore professional practices that turn a good project into a great one:

* **Security:** Implement user login and authorization using **Spring Security** and **JWT**.
* **User Experience:** Add confirmation dialogs ("Are you sure you want to delete?") and loading indicators.
* **Testing:** Write unit tests with **JUnit** for your backend logic.
* **Deployment:** Learn to package your applications with **Docker** and deploy them to a cloud service.

You have accomplished a significant goal. Congratulations on your persistence and success!


###  alterar o texto de uma tarefa sem precisar excluir e adicionar novamente na Versao web e dektop

Excelente pergunta\! A funcionalidade de editar diretamente na lista é crucial para uma boa experiência do usuário. Implementar isso é um ótimo exercício que reforça o uso do método `UPDATE` do nosso CRUD.

A boa notícia é que nossa API e nossos serviços já estão prontos\! O método `updateTarefa` que criamos para o checkbox funciona para atualizar *qualquer* parte do objeto `Tarefa`. Todo o nosso trabalho será focado na interface do usuário (UI) e na lógica do controller em cada frontend.

Vamos fazer isso passo a passo para cada aplicação.

-----

### **Parte 1: Atualizando a Versão Web (Angular)**

Para a web, uma abordagem moderna e elegante é permitir que o usuário dê um **duplo clique** no texto da tarefa para transformá-lo em um campo de edição.

#### **Passo 1: Adicionar um Estado de Edição ao Modelo**

Precisamos de uma forma de saber qual tarefa está sendo editada no momento.

1.  Abra o arquivo `todolist-web/src/app/models/tarefa.ts`.
2.  Adicione a propriedade opcional `editando`.

<!-- end list -->

```typescript
// src/app/models/tarefa.ts
export interface Tarefa {
  id?: number;
  descricao: string;
  concluida: boolean;
  editando?: boolean; // Propriedade para controlar o estado de edição na UI
}
```

#### **Passo 2: Atualizar o Template HTML (`task-list.component.html`)**

Vamos usar a diretiva `*ngIf` para mostrar o texto ou um campo de input, dependendo do estado `editando`.

1.  Abra `todolist-web/src/app/components/task-list/task-list.component.html`.
2.  Modifique a seção que exibe a descrição da tarefa:

<!-- end list -->

```html
      <span *ngIf="!tarefa.editando" 
            (dblclick)="iniciarEdicao(tarefa)" 
            [ngClass]="{'completed': tarefa.concluida}">
        {{ tarefa.descricao }}
      </span>

      <input *ngIf="tarefa.editando" 
             type="text" 
             [(ngModel)]="tarefa.descricao"
             (blur)="salvarEdicao(tarefa)"
             (keyup.enter)="salvarEdicao(tarefa)"
             (keyup.escape)="cancelarEdicao(tarefa)"
             class="edit-input"
             #editInput
      >
```

**Resumo das mudanças:**

  * **`*ngIf="!tarefa.editando"`:** Mostra o texto normal se a tarefa não estiver em modo de edição.
  * **`(dblclick)="iniciarEdicao(tarefa)"`:** Ao dar duplo clique, chama a função para começar a editar.
  * **`*ngIf="tarefa.editando"`:** Mostra o campo de input se a tarefa estiver em modo de edição.
  * **`(blur)` e `(keyup.enter)`:** Salvam a edição quando o campo perde o foco ou quando a tecla Enter é pressionada.
  * **`(keyup.escape)`:** Cancela a edição quando a tecla Escape é pressionada.

#### **Passo 3: Adicionar a Lógica no Componente (`task-list.component.ts`)**

Agora, vamos criar os métodos que o HTML está chamando.

1.  Abra `todolist-web/src/app/components/task-list/task-list.component.ts`.
2.  Adicione uma nova variável para guardar o texto original (em caso de cancelamento) e os novos métodos.

<!-- end list -->

```typescript
export class TaskListComponent implements OnInit {
  // ... (código existente)
  
  private descricaoOriginal: string = ''; // Guarda o texto original durante a edição

  // ... (métodos existentes como carregarTarefas, adicionarTarefa, etc.)

  iniciarEdicao(tarefa: Tarefa): void {
    this.descricaoOriginal = tarefa.descricao; // Salva o estado original
    tarefa.editando = true;
  }

  salvarEdicao(tarefa: Tarefa): void {
    if (tarefa.descricao.trim() === '') {
      tarefa.descricao = this.descricaoOriginal; // Restaura se o campo ficar vazio
    }
    tarefa.editando = false;
    this.atualizarStatus(tarefa); // Reutilizamos o mesmo método de update!
  }

  cancelarEdicao(tarefa: Tarefa): void {
    tarefa.descricao = this.descricaoOriginal; // Restaura o texto original
    tarefa.editando = false;
  }
  
  // ... (resto do código)
}
```

**Pronto\!** A aplicação web agora tem a funcionalidade de edição.

-----

### **Parte 2: Atualizando a Versão Desktop (JavaFX)**

Para o desktop, vamos usar um recurso nativo da `TableView`: tornar as células da coluna "Descrição" editáveis com um duplo clique.

#### **Passo 1: Habilitar a Edição na Tabela e na Coluna**

1.  Abra `todolist-desktop/src/main/java/br/com/curso/todolist/desktop/MainViewController.java`.
2.  No método `initialize`, adicione a linha `tabelaTarefas.setEditable(true);`.

#### **Passo 2: Configurar a Célula Editável**

Vamos dizer à coluna "Descrição" que ela deve usar um `TextField` quando for editada.

1.  No mesmo arquivo (`MainViewController.java`), encontre o método `configurarColunas()`. Se ele não existir, você pode adicionar a lógica dentro do `initialize`.
2.  Adicione a configuração para a `colunaDescricao`.

<!-- end list -->

```java
// Importe no início do arquivo
import javafx.scene.control.cell.TextFieldTableCell;

// ...

private void configurarColunas() {
    colunaId.setCellValueFactory(new PropertyValueFactory<>("id"));
    colunaDescricao.setCellValueFactory(new PropertyValueFactory<>("descricao"));
    colunaConcluida.setCellValueFactory(new PropertyValueFactory<>("concluida"));

    // --- LÓGICA DE EDIÇÃO ---
    // 1. Torna a coluna "Descrição" editável
    colunaDescricao.setCellFactory(TextFieldTableCell.forTableColumn());

    // 2. Define o que fazer quando a edição for confirmada (pressionando Enter)
    colunaDescricao.setOnEditCommit(event -> {
        // Pega a tarefa que foi editada
        Tarefa tarefa = event.getRowValue();
        // Atualiza a descrição dela com o novo valor
        tarefa.setDescricao(event.getNewValue());
        // Chama o nosso método de update para salvar a mudança na API
        this.atualizarTarefa(tarefa);
    });
}
```

#### **Passo 3: Juntar Tudo no Controller**

Aqui está a versão completa do `MainViewController.java` para garantir que tudo esteja no lugar certo.

```java
// ... (imports)
import javafx.scene.control.cell.TextFieldTableCell;

public class MainViewController implements Initializable {
    // ... (variáveis existentes)

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        tabelaTarefas.setEditable(true); // Habilita a edição na tabela
        configurarColunas();
        configurarFabricasDeCelulas();
        carregarDadosDaTabela();
    }

    private void configurarColunas() {
        colunaId.setCellValueFactory(new PropertyValueFactory<>("id"));
        colunaDescricao.setCellValueFactory(new PropertyValueFactory<>("descricao"));
        colunaConcluida.setCellValueFactory(new PropertyValueFactory<>("concluida"));

        // --- LÓGICA DE EDIÇÃO ---
        colunaDescricao.setCellFactory(TextFieldTableCell.forTableColumn());
        colunaDescricao.setOnEditCommit(event -> {
            Tarefa tarefa = event.getRowValue();
            tarefa.setDescricao(event.getNewValue());
            this.atualizarTarefa(tarefa);
        });
    }

    // ... (resto dos métodos: configurarFabricasDeCelulas, carregarDados, etc. permanecem iguais)
}
```

### **Como Testar**

1.  Garanta que o **Backend** esteja rodando.
2.  **Teste na Web:** Rode `ng serve`. Dê um duplo clique em uma tarefa, mude o texto, e pressione Enter ou clique fora. A mudança deve ser salva.
3.  **Teste no Desktop:** Rode a `MainApp.java`. Dê um duplo clique em uma célula na coluna "Descrição", altere o texto e pressione Enter. A mudança deve ser salva.
4.  Use o botão "Atualizar" em uma aplicação para ver as mudanças feitas na outra\!





HTML. Há um pequeno erro na localização do campo de input para edição.

O `<input>` que deveria aparecer durante a edição de uma tarefa foi colocado dentro do formulário de **adicionar uma nova tarefa**. Ele precisa ficar dentro da lista, no `<li>` de cada tarefa, para que ele possa substituir o texto quando você der o duplo clique.

-----

### Correção do HTML

Aqui está a versão corrigida do seu arquivo `task-list.component.html`. Ele separa corretamente o `<input>` de adicionar do `<input>` de editar.

Por favor, **substitua todo o conteúdo** do seu arquivo por este código:

```html
<div class="container">
  <h1>Minha Lista de Tarefas (Web)</h1>

  <form class="form-add" (ngSubmit)="adicionarTarefa()">
    <input
      type="text"
      placeholder="O que precisa ser feito?"
      [(ngModel)]="novaTarefa.descricao"
      name="descricao"
      required
    >
    <button type="submit">Adicionar</button>
  </form>

  <ul class="task-list">
    <li *ngFor="let tarefa of tarefas">
      <input
        type="checkbox"
        [(ngModel)]="tarefa.concluida"
        (change)="atualizarStatus(tarefa)"
      >

      <span *ngIf="!tarefa.editando"
            (dblclick)="iniciarEdicao(tarefa)"
            [ngClass]="{'completed': tarefa.concluida}">
        {{ tarefa.descricao }}
      </span>

      <input *ngIf="tarefa.editando"
             type="text"
             [(ngModel)]="tarefa.descricao"
             (blur)="salvarEdicao(tarefa)"
             (keyup.enter)="salvarEdicao(tarefa)"
             (keyup.escape)="cancelarEdicao(tarefa)"
             class="edit-input"
             #editInput
      >

      <button class="delete-btn" (click)="deletarTarefa(tarefa.id)">×</button>
    </li>
  </ul>
</div>
```

### O Que Foi Corrigido?

1.  **Input de Adicionar:** O `<input>` dentro do `<form>` agora é simples e serve apenas para criar novas tarefas. Ele não tem mais a lógica de `*ngIf`.
2.  **Input de Editar:** O `<input>` com a lógica `*ngIf="tarefa.editando"` foi movido para dentro do `<li>` da lista. Agora ele está no lugar certo para substituir o `<span>` da tarefa específica que você está editando.

Com esta correção, a funcionalidade de editar com duplo clique funcionará como esperado.


##  classe TaskListComponent

Obrigado por compartilhar o código. O problema é que a classe `TaskListComponent` foi declarada duas vezes no mesmo arquivo. Você colou o novo código de edição depois do final da classe original, em vez de adicioná-lo dentro dela.

Isso causa um erro de sintaxe, pois não se pode ter duas classes com o mesmo nome no mesmo arquivo.

-----

### A Correção

Precisamos mesclar a lógica de edição (a propriedade `descricaoOriginal` e os métodos `iniciarEdicao`, `salvarEdicao`, `cancelarEdicao`) dentro da única e original classe `TaskListComponent`.

**Por favor, substitua todo o conteúdo** do seu arquivo `task-list.component.ts` por esta versão única e corrigida:

```typescript
// ARQUIVO: todolist-web/src/app/components/task-list/task-list.component.ts

import { Component, OnInit } from '@angular/core';
import { TarefaService } from '../../services/tarefa.service';
import { Tarefa } from '../../models/tarefa';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-task-list',
  standalone: true,
  imports: [ CommonModule, FormsModule ],
  templateUrl: './task-list.component.html',
  styleUrl: './task-list.component.css'
})
export class TaskListComponent implements OnInit {

  // --- Propriedades da Classe ---
  tarefas: Tarefa[] = [];
  novaTarefa: Tarefa = { descricao: '', concluida: false };
  private descricaoOriginal: string = ''; // Guarda o texto original durante a edição

  constructor(private tarefaService: TarefaService) { }

  ngOnInit(): void {
    this.carregarTarefas();
  }

  // --- Métodos para o CRUD Básico ---
  carregarTarefas(): void {
    this.tarefaService.getTarefas().subscribe(tarefasRecebidas => {
      this.tarefas = tarefasRecebidas;
    });
  }

  adicionarTarefa(): void {
    if (this.novaTarefa.descricao.trim() === '') {
      return;
    }
    this.tarefaService.addTarefa(this.novaTarefa).subscribe(tarefaAdicionada => {
      this.tarefas.push(tarefaAdicionada);
      this.novaTarefa = { descricao: '', concluida: false };
    });
  }

  atualizarStatus(tarefa: Tarefa): void {
    this.tarefaService.updateTarefa(tarefa).subscribe(() => {
      console.log('Status ou descrição da tarefa ' + tarefa.id + ' atualizado.');
    });
  }

  deletarTarefa(id: number | undefined): void {
    if (id === undefined) return;
    this.tarefaService.deleteTarefa(id).subscribe(() => {
      this.tarefas = this.tarefas.filter(t => t.id !== id);
      console.log('Tarefa ' + id + ' deletada.');
    });
  }

  // --- MÉTODOS ADICIONADOS PARA A EDIÇÃO ---
  iniciarEdicao(tarefa: Tarefa): void {
    this.descricaoOriginal = tarefa.descricao;
    tarefa.editando = true;
  }

  salvarEdicao(tarefa: Tarefa): void {
    if (tarefa.descricao.trim() === '') {
      tarefa.descricao = this.descricaoOriginal;
    }
    tarefa.editando = false;
    // Reutilizamos o método de update que já tínhamos!
    this.atualizarStatus(tarefa);
  }

  cancelarEdicao(tarefa: Tarefa): void {
    tarefa.descricao = this.descricaoOriginal;
    tarefa.editando = false;
  }
}
```

### O Que Foi Corrigido?

Juntamos tudo em uma única declaração `export class TaskListComponent`. A propriedade `descricaoOriginal` e os três novos métodos (`iniciarEdicao`, `salvarEdicao`, `cancelarEdicao`) agora fazem parte da mesma classe que os métodos de CRUD que você já tinha.

Com este código corrigido, sua aplicação web compilará sem erros e a funcionalidade de edição com duplo clique funcionará perfeitamente.

---


Este código tem alguns erros de cópia e colagem que precisam ser corrigidos. A lógica para salvar uma edição foi colocada no lugar errado, e a configuração para tornar a coluna de descrição editável está faltando.

Vamos arrumar isso.

-----

### A Correção

Versão completa da sua classe `MainViewController.java`. Os principais problemas eram:

**Substitua todo o conteúdo** do seu arquivo `MainViewController.java` por este código corrigido.

```java
package br.com.curso.todolist.desktop;

import javafx.application.Platform;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.concurrent.Task;
import javafx.fxml.FXML;
import javafx.fxml.Initializable;
import javafx.geometry.Pos;
import javafx.scene.control.*;
import javafx.scene.control.cell.PropertyValueFactory;
import javafx.scene.control.cell.TextFieldTableCell; // Import necessário
import javafx.util.Callback;

import java.net.URL;
import java.util.List;
import java.util.ResourceBundle;

public class MainViewController implements Initializable {

    private final TarefaApiService tarefaApiService = new TarefaApiService();

    @FXML
    private TableView<Tarefa> tabelaTarefas;
    @FXML
    private TableColumn<Tarefa, Long> colunaId;
    @FXML
    private TableColumn<Tarefa, String> colunaDescricao;
    @FXML
    private TableColumn<Tarefa, Boolean> colunaConcluida;
    @FXML
    private TableColumn<Tarefa, Void> colunaAcoes;
    @FXML
    private TextField campoDescricao;

    @Override
    public void initialize(URL url, ResourceBundle resourceBundle) {
        // Habilita a edição na tabela inteira
        tabelaTarefas.setEditable(true);
        
        configurarColunas();
        configurarFabricasDeCelulas();
        carregarDadosDaTabela();
    }

    // MÉTODO CORRIGIDO
    private void configurarColunas() {
        colunaId.setCellValueFactory(new PropertyValueFactory<>("id"));
        colunaDescricao.setCellValueFactory(new PropertyValueFactory<>("descricao"));
        colunaConcluida.setCellValueFactory(new PropertyValueFactory<>("concluida"));

        // --- LÓGICA DE EDIÇÃO ADICIONADA AQUI ---
        // 1. Torna a coluna "Descrição" uma célula de texto editável.
        colunaDescricao.setCellFactory(TextFieldTableCell.forTableColumn());

        // 2. Define o que fazer quando a edição for confirmada (pressionando Enter).
        colunaDescricao.setOnEditCommit(event -> {
            Tarefa tarefa = event.getRowValue();
            tarefa.setDescricao(event.getNewValue());
            this.atualizarTarefa(tarefa);
        });
    }

    private void configurarFabricasDeCelulas() {
        // --- UPDATE: Configurando a célula do CheckBox ---
        colunaConcluida.setCellFactory(col -> new TableCell<>() {
            private final CheckBox checkBox = new CheckBox();
            {
                checkBox.setOnAction(event -> {
                    if (getIndex() < getTableView().getItems().size()) {
                        Tarefa tarefa = getTableView().getItems().get(getIndex());
                        tarefa.setConcluida(checkBox.isSelected());
                        atualizarTarefa(tarefa);
                    }
                });
            }

            @Override
            protected void updateItem(Boolean item, boolean empty) {
                super.updateItem(item, empty);
                if (empty || item == null) {
                    setGraphic(null);
                } else {
                    checkBox.setSelected(item);
                    setGraphic(checkBox);
                    setAlignment(Pos.CENTER);
                }
            }
        });

        // --- DELETE: Configurando a célula do Botão ---
        Callback<TableColumn<Tarefa, Void>, TableCell<Tarefa, Void>> cellFactory = param -> new TableCell<>() {
            private final Button btn = new Button("X");
            {
                btn.setStyle("-fx-background-color: #ff6666; -fx-text-fill: white; -fx-font-weight: bold;");
                btn.setOnAction(event -> {
                    if (getIndex() < getTableView().getItems().size()) {
                        Tarefa tarefa = getTableView().getItems().get(getIndex());
                        deletarTarefa(tarefa.getId());
                    }
                });
            }

            @Override
            public void updateItem(Void item, boolean empty) {
                super.updateItem(item, empty);
                if (empty) {
                    setGraphic(null);
                } else {
                    setGraphic(btn);
                    setAlignment(Pos.CENTER);
                }
            }
        };
        colunaAcoes.setCellFactory(cellFactory);
    }
    
    // MÉTODO CORRIGIDO
    private void carregarDadosDaTabela() {
        Task<List<Tarefa>> task = new Task<>() {
            @Override
            protected List<Tarefa> call() {
                return tarefaApiService.listarTarefas();
            }
        };
        task.setOnSucceeded(e -> {
            // O código de edição que estava aqui foi removido.
            ObservableList<Tarefa> tarefas = FXCollections.observableArrayList(task.getValue());
            tabelaTarefas.setItems(tarefas);
            System.out.println("Tabela atualizada.");
        });
        task.setOnFailed(e -> task.getException().printStackTrace());
        new Thread(task).start();
    }
    
    // Métodos de ação e serviço (sem alterações)
    @FXML
    private void onAdicionarAction() {
        final String descricao = campoDescricao.getText();
        if (descricao == null || descricao.trim().isEmpty()) return;

        Tarefa novaTarefa = new Tarefa();
        novaTarefa.setDescricao(descricao);
        novaTarefa.setConcluida(false);

        Task<Void> task = new Task<>() {
            @Override
            protected Void call() {
                tarefaApiService.adicionarTarefa(novaTarefa);
                return null;
            }
        };
        task.setOnSucceeded(e -> {
            campoDescricao.clear();
            carregarDadosDaTabela();
        });
        task.setOnFailed(e -> task.getException().printStackTrace());
        new Thread(task).start();
    }

    @FXML
    private void onAtualizarAction() {
        System.out.println("Botão Atualizar clicado. Buscando novos dados...");
        carregarDadosDaTabela();
    }

    private void atualizarTarefa(Tarefa tarefa) {
        Task<Void> task = new Task<>() {
            @Override
            protected Void call() {
                tarefaApiService.atualizarTarefa(tarefa);
                return null;
            }
        };
        task.setOnFailed(e -> task.getException().printStackTrace());
        new Thread(task).start();
    }

    private void deletarTarefa(Long id) {
        Task<Void> task = new Task<>() {
            @Override
            protected Void call() {
                tarefaApiService.deletarTarefa(id);
                return null;
            }
        };
        task.setOnSucceeded(e -> carregarDadosDaTabela());
        task.setOnFailed(e -> task.getException().printStackTrace());
        new Thread(task).start();
    }
}
```

