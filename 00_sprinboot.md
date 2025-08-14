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
          * **Package name:** `br.com.curso.todolistapi`
      * **Packaging:** Jar
      * **Java:** 21 (ou a versão que você instalou)

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
│   │   │   └── br/com/curso/todolistapi/
│   │   │       └── TodolistApiApplication.java
│   │   └── resources/
│   │       └── application.properties
│   └── test/
└── pom.xml
```

-----

### **Etapa 1: Criando o Model (A Entidade `Tarefa`)**

O Model representa os dados da nossa aplicação. Vamos criar a classe `Tarefa`.

1.  Dentro do pacote `br.com.curso.todolistapi`, crie um novo pacote chamado `tarefa`.
2.  Dentro de `br.com.curso.todolistapi.tarefa`, crie um novo arquivo Java chamado `Tarefa.java`.

**Código para `Tarefa.java`:**

```java
package br.com.curso.todolistapi.tarefa;

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

1.  No mesmo pacote `br.com.curso.todolistapi.tarefa`, crie uma nova **interface** Java chamada `TarefaRepository.java`.

**Código para `TarefaRepository.java`:**

```java
package br.com.curso.todolistapi.tarefa;

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

1.  No pacote `br.com.curso.todolistapi.tarefa`, crie uma nova classe Java chamada `TarefaService.java`.

**Código para `TarefaService.java`:**

```java
package br.com.curso.todolistapi.tarefa;

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

1.  No pacote `br.com.curso.todolistapi.tarefa`, crie uma nova classe Java chamada `TarefaController.java`.

**Código para `TarefaController.java`:**

```java
package br.com.curso.todolistapi.tarefa;

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

**Parabéns\!** Seus alunos agora têm um backend robusto e funcional, e sabem como verificar cada parte dele. Eles estão prontos para construir os clientes web e desktop.

---

### [ricardotecpro.github.io](https://ricardotecpro.github.io/)
