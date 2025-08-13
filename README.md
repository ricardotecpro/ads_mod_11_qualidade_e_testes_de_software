### **Guia Prático: Construindo e Testando a API do To-Do List**

**Objetivo:** Criar, passo a passo, o backend completo da nossa aplicação, e aprender a testar cada funcionalidade de forma isolada usando uma ferramenta de cliente HTTP.

-----

### **Etapa 0: Configuração Inicial do Projeto**

Vamos usar o **Spring Initializr** para criar a estrutura base do nosso projeto de forma rápida e segura.

1.  Acesse o site: [https://start.spring.io](https://start.spring.io)

2.  Preencha os campos da seguinte forma:

    * **Project:** Maven
    * **Language:** Java
    * **Spring Boot:** A versão estável mais recente (ex: 3.x.x).
    * **Project Metadata:**
        * **Group:** `br.com.curso`
        * **Artifact:** `todolist-api`
        * **Name:** `todolist-api`
        * **Description:** API para gerenciamento de tarefas
        * **Package name:** `br.com.curso.todolist`
    * **Packaging:** Jar
    * **Java:** 17 (ou a versão que você instalou)

3.  No lado direito, em **Dependencies**, clique em "ADD DEPENDENCIES" e adicione as seguintes:

    * `Spring Web`: Essencial para criar aplicações web e APIs REST.
    * `Spring Data JPA`: Facilita a comunicação com o banco de dados.
    * `H2 Database`: Um banco de dados em memória, perfeito para desenvolvimento e testes.
    * `Lombok`: Ajuda a reduzir a quantidade de código repetitivo (como getters, setters e construtores).

4.  Clique no botão **GENERATE**. Um arquivo `.zip` será baixado.

5.  Descompacte o arquivo e abra a pasta gerada na sua IDE preferida (IntelliJ ou VS Code).

A estrutura de pastas inicial será parecida com esta:

```
todolist-api/
├── src/
│   ├── main/
│   │   ├── java/
│   │   │   └── br/com/curso/todolist/
│   │   │       └── TodolistApiApplication.java
│   │   └── resources/
│   │       └── application.properties
│   └── test/
└── pom.xml
```

-----

### **Etapa 1: Criando o Model (A Entidade `Tarefa`)**

O Model representa os dados da nossa aplicação. Vamos criar a classe `Tarefa`.

1.  Dentro do pacote `br.com.curso.todolist`, crie um novo pacote chamado `tarefa`.
2.  Dentro de `br.com.curso.todolist.tarefa`, crie um novo arquivo Java chamado `Tarefa.java`.

**Código para `Tarefa.java`:**

```java
package br.com.curso.todolist.tarefa;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.Data;

/**
 * @Entity: Marca esta classe como uma entidade JPA (uma tabela no banco de dados).
 * @Table(name = "tb_tarefas"): Especifica o nome da tabela no banco.
 * @Data (Lombok): Gera automaticamente getters, setters, toString, equals e hashCode.
 */
@Data
@Entity
@Table(name = "tb_tarefas")
public class Tarefa {

    /**
     * @Id: Marca este campo como a chave primária da tabela.
     * @GeneratedValue: Configura a estratégia de geração da chave primária.
     * IDENTITY significa que o próprio banco de dados irá gerar e gerenciar o valor.
     */
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String descricao;
    private boolean concluida;
}
```

-----

### **Etapa 2: Criando o Repository (A Camada de Acesso a Dados)**

O Repository é uma interface que nos dá os métodos para interagir com o banco de dados (salvar, buscar, deletar, etc.) sem precisarmos escrever SQL.

1.  No mesmo pacote `br.com.curso.todolist.tarefa`, crie uma nova **interface** Java chamada `TarefaRepository.java`.

**Código para `TarefaRepository.java`:**

```java
package br.com.curso.todolist.tarefa;

import org.springframework.data.jpa.repository.JpaRepository;

/**
 * JpaRepository é uma interface do Spring Data JPA que já vem com métodos CRUD prontos.
 * Precisamos apenas dizer qual a Entidade que ele irá gerenciar (Tarefa) e qual o tipo da chave primária (Long).
 */
public interface TarefaRepository extends JpaRepository<Tarefa, Long> {
}

```

É só isso\! O Spring Data JPA implementará essa interface em tempo de execução para nós.

-----

### **Etapa 3: Criando a Camada de Serviço (Regras de Negócio)**

É uma boa prática ter uma camada de Serviço para conter a lógica de negócio, mantendo o Controller "limpo".

1.  No pacote `br.com.curso.todolist.tarefa`, crie uma nova classe Java chamada `TarefaService.java`.

**Código para `TarefaService.java`:**

```java
package br.com.curso.todolist.tarefa;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;

/**
 * @Service: Marca a classe como um componente de serviço do Spring,
 * onde colocamos a lógica de negócio.
 */
@Service
public class TarefaService {

    // @Autowired: O Spring irá injetar uma instância de TarefaRepository aqui.
    @Autowired
    private TarefaRepository tarefaRepository;

    public Tarefa criar(Tarefa tarefa) {
        // Poderíamos ter validações aqui antes de salvar
        return tarefaRepository.save(tarefa);
    }

    public List<Tarefa> listarTodas() {
        return tarefaRepository.findAll();
    }

    public Optional<Tarefa> buscarPorId(Long id) {
        return tarefaRepository.findById(id);
    }

    public Tarefa atualizar(Long id, Tarefa tarefaAtualizada) {
        // Verifica se a tarefa existe antes de tentar atualizar
        return tarefaRepository.findById(id)
            .map(tarefaExistente -> {
                tarefaExistente.setDescricao(tarefaAtualizada.getDescricao());
                tarefaExistente.setConcluida(tarefaAtualizada.isConcluida());
                return tarefaRepository.save(tarefaExistente);
            }).orElseThrow(() -> new RuntimeException("Tarefa não encontrada com o id: " + id));
    }

    public void deletar(Long id) {
        // Verifica se a tarefa existe antes de deletar para evitar erros
        if (!tarefaRepository.existsById(id)) {
            throw new RuntimeException("Tarefa não encontrada com o id: " + id);
        }
        tarefaRepository.deleteById(id);
    }
}
```

-----

### **Etapa 4: Criando o Controller (A API REST)**

O Controller é a porta de entrada da nossa API. Ele recebe as requisições HTTP e as direciona para a camada de Serviço.

1.  No pacote `br.com.curso.todolist.tarefa`, crie uma nova classe Java chamada `TarefaController.java`.

**Código para `TarefaController.java`:**

```java
package br.com.curso.todolist.tarefa;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * @RestController: Combina @Controller e @ResponseBody, simplificando a criação de APIs REST.
 * @RequestMapping: Define o caminho base para todos os endpoints neste controller.
 * @CrossOrigin: Permite que requisições de outras origens (como nosso frontend Angular) sejam aceitas.
 */
@RestController
@RequestMapping("/api/tarefas")
@CrossOrigin(origins = "*")
public class TarefaController {

    @Autowired
    private TarefaService tarefaService;

    // CREATE
    @PostMapping
    public Tarefa criarTarefa(@RequestBody Tarefa tarefa) {
        return tarefaService.criar(tarefa);
    }

    // READ - Listar Todas
    @GetMapping
    public List<Tarefa> listarTarefas() {
        return tarefaService.listarTodas();
    }

    // READ - Buscar por ID
    @GetMapping("/{id}")
    public ResponseEntity<Tarefa> buscarTarefaPorId(@PathVariable Long id) {
        return tarefaService.buscarPorId(id)
                .map(ResponseEntity::ok) // Se encontrar, retorna 200 OK com a tarefa
                .orElse(ResponseEntity.notFound().build()); // Se não, retorna 404 Not Found
    }

    // UPDATE
    @PutMapping("/{id}")
    public ResponseEntity<Tarefa> atualizarTarefa(@PathVariable Long id, @RequestBody Tarefa tarefa) {
        try {
            Tarefa atualizada = tarefaService.atualizar(id, tarefa);
            return ResponseEntity.ok(atualizada);
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }

    // DELETE
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deletarTarefa(@PathVariable Long id) {
        try {
            tarefaService.deletar(id);
            return ResponseEntity.noContent().build(); // Retorna 204 No Content, sucesso sem corpo
        } catch (RuntimeException e) {
            return ResponseEntity.notFound().build();
        }
    }
}
```

**Neste ponto, a nossa API está completa\!** Vamos executá-la.

1.  Encontre o arquivo `TodolistApiApplication.java`.
2.  Clique com o botão direito sobre ele e selecione "Run 'TodolistApiApplication'".
3.  O console da sua IDE mostrará o log de inicialização do Spring Boot. Se tudo deu certo, você verá uma mensagem como `Started TodolistApiApplication in X.XXX seconds`.

-----

### **Etapa 5: Testando a API com Postman ou Insomnia**

Agora vamos agir como se fôssemos o frontend, enviando requisições para a nossa API em execução.

#### **Teste 1: Criar uma Tarefa (CREATE)**

* **Método HTTP:** `POST`
* **URL:** `http://localhost:8080/api/tarefas`
* **Body:** Vá para a aba "Body", selecione a opção `raw` e o formato `JSON`.
* **Conteúdo do Body:**
  ```json
  {
      "descricao": "Aprender a testar APIs REST",
      "concluida": false
  }
  ```
* **Ação:** Clique em "Send".
* **Resultado Esperado:** Você deve receber um status `200 OK` e, no corpo da resposta, o JSON da tarefa que você acabou de criar, agora com um `id` (provavelmente `1`).

#### **Teste 2: Listar Todas as Tarefas (READ)**

* **Método HTTP:** `GET`
* **URL:** `http://localhost:8080/api/tarefas`
* **Ação:** Clique em "Send".
* **Resultado Esperado:** Status `200 OK` e um array JSON no corpo da resposta contendo a tarefa criada no passo anterior.

#### **Teste 3: Atualizar uma Tarefa (UPDATE)**

* **Método HTTP:** `PUT`
* **URL:** `http://localhost:8080/api/tarefas/1` (use o `id` da tarefa que você criou)
* **Body:** Novamente, `raw` e `JSON`.
* **Conteúdo do Body:**
  ```json
  {
      "descricao": "API testada e atualizada com sucesso!",
      "concluida": true
  }
  ```
* **Ação:** Clique em "Send".
* **Resultado Esperado:** Status `200 OK` e o JSON da tarefa com os dados atualizados.

#### **Teste 4: Deletar uma Tarefa (DELETE)**

* **Método HTTP:** `DELETE`
* **URL:** `http://localhost:8080/api/tarefas/1`
* **Ação:** Clique em "Send".
* **Resultado Esperado:** Status `204 No Content`. A resposta não terá corpo, o que é normal para esta operação.

#### **Verificação Final**

Repita o **Teste 2 (Listar Todas)**. O resultado esperado agora é um status `200 OK` com um array JSON vazio `[]`, confirmando que a exclusão funcionou.

Excelente pergunta\! Visualizar a organização final das pastas e arquivos é fundamental para entender como as partes se conectam.

Ao seguir o passo a passo, a estrutura de pastas e arquivos do seu projeto backend (`todolist-api`) ficará assim:

```
todolist-api/
├── .gitignore         # Arquivo do Git para ignorar arquivos desnecessários
├── mvnw               # Executável do Maven Wrapper (para Unix/Linux)
├── mvnw.cmd           # Executável do Maven Wrapper (para Windows)
├── pom.xml            # O coração do projeto Maven: define as dependências e como construir o projeto
│
└── src/               # Pasta principal contendo todo o código-fonte
    ├── main/
    │   ├── java/
    │   │   └── br/
    │   │       └── com/
    │   │           └── curso/
    │   │               └── todolist/
    │   │                   │
    │   │                   ├── TodolistApiApplication.java # Ponto de entrada que inicia o servidor
    │   │                   │
    │   │                   └── tarefa/  # PACOTE DE FUNCIONALIDADE: TAREFA
    │   │                       │
    │   │                       ├── TarefaController.java  # (CONTROLLER) Recebe as requisições HTTP da API
    │   │                       ├── TarefaService.java     # (SERVICE) Contém as regras de negócio
    │   │                       ├── Tarefa.java            # (MODEL) A representação da nossa tabela no banco
    │   │                       └── TarefaRepository.java  # (REPOSITORY) Interface para acesso aos dados
    │   │
    │   └── resources/
    │       ├── static/         # Para arquivos estáticos como CSS, JS, imagens (não usamos nesta API)
    │       ├── templates/      # Para templates de views (não usamos nesta API)
    │       └── application.properties # Arquivo de configuração principal do Spring
    │
    └── test/              # Pasta para os códigos de teste
        └── java/
            └── br/
                └── com/
                    └── curso/
                        └── todolist/
                            └── TodolistApiApplicationTests.java # Arquivo de teste inicial
```

### **Análise da Estrutura (Pontos para explicar aos alunos):**

1.  **Organização por Funcionalidade (Feature):** Observe que, dentro do pacote principal (`br.com.curso.todolist`), criamos um subpacote `tarefa`. Todas as classes relacionadas à funcionalidade "Tarefa" (Controller, Service, Model, Repository) estão juntas dentro dele.

    * **Por que isso é bom?** Quando o projeto crescer e tivermos novas funcionalidades como `Usuario` ou `Categoria`, podemos simplesmente criar os pacotes `usuario/` e `categoria/`. Isso mantém o projeto extremamente organizado e fácil de navegar. É uma abordagem muito mais escalável do que criar pacotes por camada (ex: `controllers/`, `services/`, etc.).

2.  **`src/main/java` vs. `src/main/resources`:**

    * Todo o código **Java** compilável fica em `src/main/java`.
    * Todos os outros arquivos de recurso que a aplicação precisa, como configurações, scripts SQL, arquivos de internacionalização, ficam em `src/main/resources`. O `application.properties` é o exemplo mais claro aqui, onde podemos, por exemplo, mudar a porta do servidor (`server.port = 8081`) ou configurar a conexão com um banco de dados real.

3.  **`pom.xml`:** É o manifesto do projeto. Se um aluno perguntar "Onde está a declaração de que estamos usando o Spring Web ou o H2?", a resposta está neste arquivo. Ele lista todas as "peças de Lego" (dependências) que estamos usando para construir nossa aplicação.

4.  **`TodolistApiApplication.java`:** É o coração que bombeia o sangue. A anotação `@SpringBootApplication` dentro dele é o que ativa toda a mágica do Spring, escaneando o projeto em busca de componentes (`@RestController`, `@Service`, etc.) e configurando tudo automaticamente.

===

Excelente\! Ter a API funcionando perfeitamente é a base sólida que precisávamos. Agora que o "cérebro" da nossa aplicação está pronto, o próximo passo é construir a "face" dela – a interface com a qual o usuário irá interagir.

Seguindo nosso plano original, vamos começar com o **Frontend Web usando Angular**. Vamos criar uma aplicação web moderna e reativa que irá consumir a API que acabamos de construir.

-----

### **Próxima Etapa: Construindo a Interface Web com Angular**

**Objetivo:** Criar uma Single Page Application (SPA) para listar, adicionar, atualizar e remover tarefas, comunicando-se em tempo real com nosso backend Spring Boot.

#### **Passo 1: Preparando o Ambiente e Criando o Projeto Angular**

1.  **Verifique os pré-requisitos:** Abra o seu terminal ou prompt de comando e certifique-se de que o Node.js e o Angular CLI estão instalados.

    ```bash
    node -v
    ng version
    ```

    (Se não estiverem instalados, você pode baixá-los do site oficial do [Node.js](https://nodejs.org/) e instalar o Angular CLI com `npm install -g @angular/cli`).

2.  **Crie o projeto Angular:** Navegue até a pasta onde você guarda seus projetos (fora da pasta `todolist-api`) e execute o seguinte comando:

    ```bash
    ng new todolist-web
    ```

    O Angular CLI fará algumas perguntas:

    * `Would you like to add Angular routing?` (Gostaria de adicionar roteamento Angular?) -\> Digite `n` e pressione Enter (para este projeto simples, não precisaremos de rotas).
    * `Which stylesheet format would you like to use?` (Qual formato de folha de estilo você gostaria de usar?) -\> Selecione `CSS` (a opção mais simples e padrão).

    Aguarde o Angular CLI criar a pasta `todolist-web` e instalar todas as dependências.

3.  **Abra o novo projeto:** Abra a pasta `todolist-web` em uma **nova janela** do seu editor (VS Code é altamente recomendado para desenvolvimento Angular).

#### **Passo 2: Gerando os Blocos de Construção (Componentes e Serviços)**

Vamos usar o Angular CLI para criar a estrutura básica da nossa aplicação.

1.  **Navegue para a pasta do projeto** no seu terminal:

    ```bash
    cd todolist-web
    ```

2.  **Crie um modelo (interface) para a Tarefa:** Isso garante que nosso frontend "fale a mesma língua" que o backend.

    ```bash
    ng generate interface models/tarefa
    ```

    Isso criará a pasta `models` e o arquivo `tarefa.ts` dentro dela.

3.  **Crie o Serviço de Tarefas:** O serviço será o único responsável por se comunicar com a nossa API.

    ```bash
    ng generate service services/tarefa
    ```

    Isso criará a pasta `services` e o arquivo `tarefa.service.ts`.

4.  **Crie o Componente da Lista de Tarefas:** Este será o nosso principal componente visual.

    ```bash
    ng generate component components/task-list
    ```

    Isso criará a pasta `components/task-list` com 4 arquivos (`.html`, `.css`, `.ts`, `.spec.ts`).

#### **Passo 3: Codificando a Conexão com o Backend**

Agora vamos escrever o código para fazer a ponte entre o Angular e a API Spring Boot.

1.  **Defina a Interface `tarefa.ts`:**
    Abra o arquivo `src/app/models/tarefa.ts` e adicione os campos que correspondem à nossa entidade Java.

    ```typescript
    // src/app/models/tarefa.ts
    export interface Tarefa {
      id?: number; // O ID é opcional na criação, pois o backend o gera
      descricao: string;
      concluida: boolean;
    }
    ```

2.  **Configure o Módulo HTTP:** Para que nosso serviço possa fazer requisições web, precisamos importar o `HttpClientModule`.
    Abra o arquivo `src/app/app.module.ts` e modifique-o:

    ```typescript
    // src/app/app.module.ts
    import { NgModule } from '@angular/core';
    import { BrowserModule } from '@angular/platform-browser';
    import { HttpClientModule } from '@angular/common/http'; // 1. Importe o HttpClientModule
    import { FormsModule } from '@angular/forms'; // 2. Importe o FormsModule para usar ngModel

    import { AppComponent } from './app.component';
    import { TaskListComponent } from './components/task-list/task-list.component';

    @NgModule({
      declarations: [
        AppComponent,
        TaskListComponent
      ],
      imports: [
        BrowserModule,
        HttpClientModule, // 3. Adicione aos imports
        FormsModule       // 4. Adicione também o FormsModule
      ],
      providers: [],
      bootstrap: [AppComponent]
    })
    export class AppModule { }
    ```

3.  **Implemente o `TarefaService`:** Este é o passo crucial. Vamos criar os métodos que chamam nossa API.
    Abra `src/app/services/tarefa.service.ts` e adicione o seguinte código:

    ```typescript
    // src/app/services/tarefa.service.ts
    import { Injectable } from '@angular/core';
    import { HttpClient } from '@angular/common/http';
    import { Observable } from 'rxjs';
    import { Tarefa } from '../models/tarefa';

    @Injectable({
      providedIn: 'root'
    })
    export class TarefaService {

      // A URL base da nossa API que está rodando localmente
      private apiUrl = 'http://localhost:8080/api/tarefas';

      // Injetamos o HttpClient para poder fazer requisições HTTP
      constructor(private http: HttpClient) { }

      // READ: Retorna um Observable com a lista de tarefas
      getTarefas(): Observable<Tarefa[]> {
        return this.http.get<Tarefa[]>(this.apiUrl);
      }

      // CREATE: Envia uma nova tarefa para a API
      addTarefa(tarefa: Tarefa): Observable<Tarefa> {
        return this.http.post<Tarefa>(this.apiUrl, tarefa);
      }

      // UPDATE: Atualiza uma tarefa existente
      updateTarefa(tarefa: Tarefa): Observable<Tarefa> {
        const url = `${this.apiUrl}/${tarefa.id}`;
        return this.http.put<Tarefa>(url, tarefa);
      }

      // DELETE: Deleta uma tarefa pelo seu ID
      deleteTarefa(id: number): Observable<void> {
        const url = `${this.apiUrl}/${id}`;
        return this.http.delete<void>(url);
      }
    }
    ```

#### **Passo 4: Integrando o Componente Principal**

Por fim, vamos dizer ao Angular para usar nosso novo componente `task-list`.

1.  Abra o arquivo `src/app/app.component.html`.
2.  **Apague todo o conteúdo** que vem por padrão.
3.  Adicione apenas a tag do nosso componente:
    ```html
    <app-task-list></app-task-list>
    ```

Pronto\! A estrutura inicial e a camada de serviço do nosso frontend estão prontas. O próximo passo será construir a parte visual (`.html`) e a lógica (`.ts`) do nosso `TaskListComponent` para que o usuário possa, de fato, ver e interagir com as tarefas.


===


-----

### **Próxima Etapa (Versão Standalone): Construindo a Interface Web com Angular**

O objetivo e os passos de geração de arquivos são os mesmos, mas a forma como conectamos as dependências (como o `HttpClient` para fazer requisições e o `FormsModule` para formulários) é feita diretamente nos componentes ou na configuração central da aplicação, sem um `app.module.ts`.

#### **Passos 1 e 2: Geração de Arquivos (Sem Alterações)**

Os comandos que você rodou continuam perfeitamente válidos:

```bash
# Cria a interface do modelo (não muda nada)
ng generate interface models/tarefa

# Cria o serviço (não muda nada, ele já vem com "providedIn: 'root'")
ng generate service services/tarefa

# Cria o componente (ele será gerado com "standalone: true" por padrão)
ng generate component components/task-list
```

#### **Passo 3: Codificando a Conexão e Configuração (O Jeito Standalone)**

Aqui está a principal diferença. Não temos um `app.module.ts` para importar o `HttpClientModule`. Em vez disso, nós "provemos" o cliente HTTP na configuração da nossa aplicação.

1.  **Defina a Interface `tarefa.ts` (Sem alteração):**
    Abra `src/app/models/tarefa.ts` e garanta que ele esteja assim:

    ```typescript
    // src/app/models/tarefa.ts
    export interface Tarefa {
      id?: number;
      descricao: string;
      concluida: boolean;
    }
    ```

2.  **Implemente o `TarefaService` (Sem alteração):**
    O código do serviço em `src/app/services/tarefa.service.ts` permanece exatamente o mesmo. Ele é injetável na raiz (`providedIn: 'root'`) e está pronto para ser usado em qualquer lugar.

    ```typescript
    // src/app/services/tarefa.service.ts
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

      // ... todos os métodos (getTarefas, addTarefa, etc.) continuam iguais
      getTarefas(): Observable<Tarefa[]> {
        return this.http.get<Tarefa[]>(this.apiUrl);
      }
      // ... etc
    }
    ```

3.  **Configure o Acesso HTTP na Aplicação (A Grande Mudança):**
    Abra o arquivo `src/app/app.config.ts`. É aqui que configuramos os provedores globais da nossa aplicação.

    ```typescript
    // src/app/app.config.ts
    import { ApplicationConfig } from '@angular/core';
    import { provideRouter } from '@angular/router';

    import { routes } from './app.routes';
    import { provideHttpClient } from '@angular/common/http'; // 1. IMPORTE AQUI

    export const appConfig: ApplicationConfig = {
      providers: [
        provideRouter(routes),
        provideHttpClient() // 2. ADICIONE AQUI
      ]
    };
    ```

    Ao usar `provideHttpClient()`, você está disponibilizando todas as ferramentas necessárias para que o `HttpClient` funcione em toda a sua aplicação, substituindo o antigo `HttpClientModule`.

#### **Passo 4: Integrando os Componentes Standalone**

Componentes standalone precisam importar explicitamente outros componentes, diretivas ou pipes que utilizam em seus templates.

1.  **Faça o `AppComponent` usar o `TaskListComponent`:**
    Primeiro, precisamos dizer ao nosso componente principal (`AppComponent`) que ele pode usar o `TaskListComponent`.
    Abra o arquivo `src/app/app.component.ts`.

    ```typescript
    // src/app/app.component.ts
    import { Component } from '@angular/core';
    import { RouterOutlet } from '@angular/router';
    import { TaskListComponent } from './components/task-list/task-list.component'; // 1. IMPORTE o componente filho

    @Component({
      selector: 'app-root',
      standalone: true,
      imports: [
        RouterOutlet,
        TaskListComponent // 2. ADICIONE-O AOS IMPORTS
      ],
      templateUrl: './app.component.html',
      styleUrl: './app.component.css'
    })
    export class AppComponent {
      title = 'todolist-web';
    }
    ```

2.  **Limpe o Template Principal:**
    Agora, assim como antes, limpe o arquivo `src/app/app.component.html` e adicione apenas a tag do nosso novo componente.

    ```html
    <app-task-list></app-task-list>
    ```

**Resumo da Situação Atual:**

* Sua aplicação Angular agora está configurada corretamente para fazer requisições HTTP.
* O `AppComponent` (a casca da aplicação) está pronto para renderizar o `TaskListComponent`.
* O `TarefaService` está pronto para ser injetado e usado para buscar os dados da sua API.

**Próximo Passo Lógico:**

Agora estamos exatamente no ponto que queríamos: prontos para dar vida ao `TaskListComponent`. A próxima etapa será:

1.  Abrir o arquivo `task-list.component.ts` para injetar o `TarefaService` e criar os métodos que buscarão e manipularão os dados.
2.  Abrir o arquivo `task-list.component.html` para criar a estrutura visual (o formulário de adição e a lista de tarefas).


===

Com a estrutura e a configuração do Angular prontas, a próxima etapa é a mais visual e gratificante: **dar vida ao componente `TaskListComponent`**.

Vamos fazer isso em três partes:

1.  **A Lógica (o arquivo `.ts`):** Ensinar o componente a buscar, criar e deletar tarefas usando o serviço que criamos.
2.  **A Aparência (o arquivo `.html`):** Construir o formulário e a lista que o usuário verá e com os quais interagirá.
3.  **O Estilo (o arquivo `.css`):** Adicionar um pouco de estilo para que a aplicação fique mais agradável.

-----

### **Próxima Etapa: Implementando o Componente `TaskListComponent`**

#### **Passo 1: A Lógica do Componente (`task-list.component.ts`)**

Abra o arquivo `src/app/components/task-list/task-list.component.ts`. Vamos injetar nosso serviço e criar os métodos para gerenciar as tarefas.

**Substitua o conteúdo do arquivo por este código:**

```typescript
// src/app/components/task-list/task-list.component.ts
import { Component, OnInit } from '@angular/core';
import { TarefaService } from '../../services/tarefa.service';
import { Tarefa } from '../../models/tarefa';
import { CommonModule } from '@angular/common'; // Importe o CommonModule
import { FormsModule } from '@angular/forms';   // Importe o FormsModule

@Component({
  selector: 'app-task-list',
  standalone: true,
  // Para usar *ngFor, [(ngModel)], etc. em um componente standalone,
  // precisamos importar os módulos que os fornecem.
  imports: [
    CommonModule,
    FormsModule
  ],
  templateUrl: './task-list.component.html',
  styleUrl: './task-list.component.css'
})
export class TaskListComponent implements OnInit {

  // Array para armazenar as tarefas que vêm da API
  tarefas: Tarefa[] = [];
  // Objeto para vincular com o formulário de nova tarefa (two-way data binding)
  novaTarefa: Tarefa = { descricao: '', concluida: false };

  // Injetamos nosso serviço no construtor para poder usá-lo
  constructor(private tarefaService: TarefaService) { }

  // ngOnInit é um "gancho de ciclo de vida" do Angular.
  // O código aqui dentro é executado uma vez quando o componente é inicializado.
  ngOnInit(): void {
    this.carregarTarefas();
  }

  carregarTarefas(): void {
    // Usamos o serviço para buscar as tarefas e as armazenamos no nosso array
    this.tarefaService.getTarefas().subscribe(tarefasRecebidas => {
      this.tarefas = tarefasRecebidas;
    });
  }

  adicionarTarefa(): void {
    // Validação simples para não adicionar tarefas vazias
    if (this.novaTarefa.descricao.trim() === '') {
      return;
    }

    this.tarefaService.addTarefa(this.novaTarefa).subscribe(tarefaAdicionada => {
      // Adiciona a nova tarefa à lista local para atualização instantânea da UI
      this.tarefas.push(tarefaAdicionada);
      // Limpa o objeto para o próximo input do usuário
      this.novaTarefa = { descricao: '', concluida: false };
    });
  }

  // Este método será chamado quando o checkbox for alterado
  atualizarStatus(tarefa: Tarefa): void {
    this.tarefaService.updateTarefa(tarefa).subscribe();
  }

  deletarTarefa(id: number | undefined): void {
    if (id === undefined) return;

    this.tarefaService.deleteTarefa(id).subscribe(() => {
      // Remove a tarefa da lista local para atualização instantânea da UI
      this.tarefas = this.tarefas.filter(t => t.id !== id);
    });
  }
}
```

#### **Passo 2: A Aparência do Componente (`task-list.component.html`)**

Agora, vamos criar o HTML que permitirá ao usuário ver a lista e interagir com ela.

Abra o arquivo `src/app/components/task-list/task-list.component.html` e **substitua o conteúdo** por este:

```html
<div class="container">
  <h1>Minha Lista de Tarefas</h1>

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

**Conceitos chave aqui:**

* `(ngSubmit)="adicionarTarefa()"`: Quando o formulário for submetido, chama nosso método.
* `[(ngModel)]="novaTarefa.descricao"`: **Two-way Data Binding**. O valor do input está ligado à propriedade `novaTarefa.descricao` no nosso `.ts`. Se um muda, o outro também muda.
* `*ngFor="let tarefa of tarefas"`: Repete o elemento `<li>` para cada objeto `tarefa` dentro do nosso array `tarefas`.
* `[ngClass]="{'completed': tarefa.concluida}"`: Aplica a classe CSS `completed` ao `<span>` somente se a propriedade `tarefa.concluida` for `true`.
* `(click)="deletarTarefa(tarefa.id)"`: Quando o botão de deletar for clicado, chama o método `deletarTarefa`, passando o `id` da tarefa atual no loop.

#### **Passo 3: O Estilo do Componente (`task-list.component.css`)**

Para não ficar uma tela em branco, vamos adicionar um estilo mínimo.

Abra o arquivo `src/app/components/task-list/task-list.component.css` e **adicione** o seguinte código:

```css
/* src/app/components/task-list/task-list.component.css */
.container {
  max-width: 600px;
  margin: 2rem auto;
  font-family: sans-serif;
  padding: 1rem;
}

.form-add {
  display: flex;
  margin-bottom: 1.5rem;
}

.form-add input {
  flex-grow: 1;
  padding: 0.8rem;
  border: 1px solid #ccc;
  border-radius: 4px 0 0 4px;
}

.form-add button {
  padding: 0.8rem 1.2rem;
  border: none;
  background-color: #007bff;
  color: white;
  cursor: pointer;
  border-radius: 0 4px 4px 0;
}

.task-list {
  list-style: none;
  padding: 0;
}

.task-list li {
  display: flex;
  align-items: center;
  padding: 0.8rem;
  border-bottom: 1px solid #eee;
}

.task-list li:last-child {
  border-bottom: none;
}

.task-list li span {
  flex-grow: 1;
  margin-left: 1rem;
}

.task-list li span.completed {
  text-decoration: line-through;
  color: #888;
}

.delete-btn {
  border: none;
  background: transparent;
  color: #ff4d4d;
  cursor: pointer;
  font-size: 1.2rem;
  font-weight: bold;
}
```

#### **Passo 4: Rodar a Aplicação Completa\!**

Agora é a hora da verdade.

1.  **Garanta que sua API Spring Boot esteja rodando.** (Abra o projeto backend e execute a classe `TodolistApiApplication.java`).
2.  **Abra um novo terminal na pasta do projeto Angular (`todolist-web`)** e execute o comando:
    ```bash
    ng serve --open
    ```
    O `--open` fará com que seu navegador padrão abra automaticamente na página `http://localhost:4200`.

Se tudo correu bem, você verá sua lista de tarefas funcional\! Tente adicionar uma nova tarefa, marcar como concluída e deletá-la. Você verá a interface reagir instantaneamente enquanto, nos bastidores, seu frontend Angular conversa com seu backend Java.

===

Ótima observação\! Esses erros de compilação são muito comuns e o log de erros do Angular é excelente, pois nos diz exatamente onde está o problema. Vamos resolver isso.

A mensagem principal é clara: `Property 'addTarefa' does not exist on type 'TarefaService'`. Isso significa que o nosso componente `TaskListComponent` está tentando chamar métodos (`addTarefa`, `updateTarefa`, `deleteTarefa`) que não foram encontrados na classe `TarefaService`.

Provavelmente, o código no arquivo do serviço está incompleto.

-----

### **A Correção 🎯**

O problema está no arquivo `tarefa.service.ts`. Ele precisa ter todos os métodos que o nosso componente utiliza.

1.  **Abra o arquivo:** `src/app/services/tarefa.service.ts`
2.  **Substitua** o conteúdo dele pelo código completo abaixo, garantindo que todos os métodos CRUD estejam presentes:

<!-- end list -->

```typescript
// src/app/services/tarefa.service.ts

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

  // READ: Retorna um Observable com a lista de tarefas
  getTarefas(): Observable<Tarefa[]> {
    return this.http.get<Tarefa[]>(this.apiUrl);
  }

  // CREATE: Envia uma nova tarefa para a API
  addTarefa(tarefa: Tarefa): Observable<Tarefa> {
    return this.http.post<Tarefa>(this.apiUrl, tarefa);
  }

  // UPDATE: Atualiza uma tarefa existente
  updateTarefa(tarefa: Tarefa): Observable<Tarefa> {
    const url = `${this.apiUrl}/${tarefa.id}`;
    return this.http.put<Tarefa>(url, tarefa);
  }

  // DELETE: Deleta uma tarefa pelo seu ID
  deleteTarefa(id: number): Observable<void> {
    const url = `${this.apiUrl}/${id}`;
    return this.http.delete<void>(url);
  }
}
```

-----

### **O Que Foi Corrigido?**

* **Métodos Faltantes:** Adicionamos os métodos `addTarefa`, `updateTarefa` e `deleteTarefa` que o compilador não estava encontrando. Agora, quando o `TaskListComponent` chamar `this.tarefaService.addTarefa(...)`, o método existirá e o erro desaparecerá.
* **Erro de Tipo `any`:** O erro `Parameter 'tarefaAdicionada' implicitly has an 'any' type` geralmente acontece como consequência do primeiro erro. Como o método `addTarefa` não existia, o TypeScript não conseguia inferir o tipo do parâmetro no `subscribe`. Ao corrigir o serviço, este erro também deve ser resolvido.

**Depois de salvar o arquivo `tarefa.service.ts` com o código completo, o `ng serve` em "watch mode" irá detectar a mudança e tentar recompilar a aplicação automaticamente. Desta vez, deve funcionar sem erros\!** ✔️


===






