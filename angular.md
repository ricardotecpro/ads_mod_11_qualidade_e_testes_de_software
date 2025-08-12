A principal oportunidade de melhoria está em unificar a trilha de aprendizado, focando exclusivamente na arquitetura **Standalone**, que é o padrão atual para novos projetos Angular. Isso elimina a necessidade de apresentar duas opções (`NgModule` vs. `Standalone`), o que pode confundir o aluno, e remove a repetição de código, tornando o guia mais conciso e direto.

A reestruturação a seguir adota uma abordagem mais narrativa e incremental, construindo o conhecimento passo a passo, desde a estrutura inicial até a aplicação funcional.

-----

### **Estrutura de Ensino Refinada e Reescrevita**

### **Módulo 2: Construindo a Interface Web com Angular**

**Objetivo:** Criar uma Single Page Application (SPA) moderna para gerenciar tarefas. Iremos construir uma interface interativa que se comunica em tempo real com o backend Spring Boot que preparamos, utilizando a arquitetura Standalone, o padrão atual do Angular.

-----

#### **Passo 1: Preparando o Terreno — O Projeto Angular Standalone**

Vamos começar criando nosso projeto e garantindo que o ambiente de desenvolvimento esteja pronto.

1.  **Pré-requisitos:** Abra seu terminal e verifique se o Node.js e o Angular CLI estão instalados.

    ```bash
    node -v
    ng version
    ```

    *(Caso não os tenha, instale o [Node.js](https://nodejs.org/) e, em seguida, o Angular CLI com o comando `npm install -g @angular/cli`)*.

2.  **Criação do Projeto:** No seu diretório de projetos (fora da pasta `todolist-api`), execute o comando de criação.

    ```bash
    ng new todolist-web
    ```

    O CLI fará algumas perguntas:

      * `Would you like to add Angular routing?` -\> `n` (Não usaremos rotas neste projeto simples).
      * `Which stylesheet format would you like to use?` -\> `CSS`.

    O Angular criará a pasta `todolist-web` e instalará as dependências. Por padrão, ele já usará a nova arquitetura **Standalone**, que é mais simples e não utiliza `NgModules`.

3.  **Abra o Projeto:** Abra a pasta `todolist-web` em uma nova janela do seu editor de código (VS Code é recomendado).

-----

#### **Passo 2: Definindo a Estrutura: Componentes e o Modelo de Dados**

Com o projeto criado, vamos gerar os blocos de construção da nossa aplicação.

1.  **A Interface de Dados (`Tarefa`):** Para garantir que nosso frontend entenda a estrutura de dados vinda do backend, criaremos uma "interface" TypeScript.

    ```bash
    # No terminal, dentro da pasta todolist-web
    ng generate interface models/tarefa
    ```

    Agora, abra o arquivo `src/app/models/tarefa.ts` e defina sua estrutura:

    ```typescript
    // src/app/models/tarefa.ts
    export interface Tarefa {
      id?: number; // ID é opcional, pois o backend o gera na criação.
      descricao: string;
      concluida: boolean;
    }
    ```

2.  **O Componente da Lista de Tarefas:** Este será o elemento visual principal da nossa aplicação.

    ```bash
    ng generate component components/task-list
    ```

    Isso cria uma pasta `task-list` com os arquivos do componente (`.ts`, `.html`, `.css`).

3.  **Integração do Novo Componente:** Vamos instruir o `AppComponent` (o componente raiz da aplicação) a exibir nosso novo `TaskListComponent`.

      * Abra `src/app/app.component.ts`.
      * Importe o `TaskListComponent` e adicione-o ao array `imports` do `@Component`.

    <!-- end list -->

    ```typescript
    // src/app/app.component.ts
    import { Component } from '@angular/core';
    import { RouterOutlet } from '@angular/router';
    import { TaskListComponent } from './components/task-list/task-list.component'; // 1. Importe aqui

    @Component({
      selector: 'app-root',
      standalone: true,
      imports: [
        RouterOutlet,
        TaskListComponent // 2. Adicione aqui
      ],
      templateUrl: './app.component.html',
      styleUrl: './app.component.css'
    })
    export class AppComponent {
      title = 'todolist-web';
    }
    ```

      * Por fim, substitua o conteúdo de `src/app/app.component.html` por apenas a tag do nosso componente:

    <!-- end list -->

    ```html
    <app-task-list></app-task-list>
    ```

-----

#### **Passo 3: Criando o Serviço de Comunicação (`TarefaService`)**

O serviço terá a responsabilidade exclusiva de se comunicar com nossa API. Isso mantém nosso código organizado.

1.  **Gere o Serviço:**

    ```bash
    ng generate service services/tarefa
    ```

2.  **Configurando o `HttpClient`:** Para fazer requisições web, precisamos configurar o `HttpClient` do Angular. Na arquitetura Standalone, isso é feito no arquivo `app.config.ts`.

      * Abra o arquivo `src/app/app.config.ts`.
      * Importe `provideHttpClient` e adicione-o ao array `providers`.

    <!-- end list -->

    ```typescript
    // src/app/app.config.ts
    import { ApplicationConfig } from '@angular/core';
    import { provideRouter } from '@angular/router';
    import { routes } from './app.routes';
    import { provideHttpClient } from '@angular/common/http'; // 1. Importe aqui

    export const appConfig: ApplicationConfig = {
      providers: [
        provideRouter(routes),
        provideHttpClient() // 2. Adicione aqui
      ]
    };
    ```

    Com isso, o `HttpClient` está disponível para ser injetado e usado em qualquer serviço da nossa aplicação.

3.  **Implemente os Métodos do Serviço:** Agora, vamos codificar o `TarefaService` para realizar as operações de CRUD (Create, Read, Update, Delete) na nossa API.

      * Abra `src/app/services/tarefa.service.ts` e substitua seu conteúdo:

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

      // A URL base da nossa API Spring Boot
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

-----

#### **Passo 4: Dando Vida ao `TaskListComponent`**

Esta é a etapa mais visual, onde conectaremos a lógica, o HTML e o CSS para criar a interface do usuário.

1.  **A Lógica (`task-list.component.ts`):** Vamos ensinar o componente a usar o `TarefaService` para gerenciar os dados.

      * Abra `src/app/components/task-list/task-list.component.ts` e substitua seu conteúdo.

    <!-- end list -->

    ```typescript
    // src/app/components/task-list/task-list.component.ts
    import { Component, OnInit } from '@angular/core';
    import { TarefaService } from '../../services/tarefa.service';
    import { Tarefa } from '../../models/tarefa';
    import { CommonModule } from '@angular/common'; // Necessário para *ngFor, etc.
    import { FormsModule } from '@angular/forms';   // Necessário para [(ngModel)]

    @Component({
      selector: 'app-task-list',
      standalone: true,
      // Em componentes standalone, importamos os módulos que usamos diretamente aqui.
      imports: [
        CommonModule,
        FormsModule
      ],
      templateUrl: './task-list.component.html',
      styleUrl: './task-list.component.css'
    })
    export class TaskListComponent implements OnInit {

      tarefas: Tarefa[] = [];
      novaTarefa: Tarefa = { descricao: '', concluida: false };

      constructor(private tarefaService: TarefaService) { }

      // ngOnInit é executado quando o componente é inicializado.
      ngOnInit(): void {
        this.carregarTarefas();
      }

      carregarTarefas(): void {
        this.tarefaService.getTarefas().subscribe(tarefasRecebidas => {
          this.tarefas = tarefasRecebidas;
        });
      }

      adicionarTarefa(): void {
        if (this.novaTarefa.descricao.trim() === '') return;

        this.tarefaService.addTarefa(this.novaTarefa).subscribe(tarefaAdicionada => {
          this.tarefas.push(tarefaAdicionada);
          this.novaTarefa = { descricao: '', concluida: false }; // Limpa o formulário
        });
      }

      atualizarStatus(tarefa: Tarefa): void {
        this.tarefaService.updateTarefa(tarefa).subscribe();
      }

      deletarTarefa(id: number | undefined): void {
        if (id === undefined) return;

        this.tarefaService.deleteTarefa(id).subscribe(() => {
          // Remove a tarefa da lista local para atualizar a UI instantaneamente
          this.tarefas = this.tarefas.filter(t => t.id !== id);
        });
      }
    }
    ```

2.  **A Aparência (`task-list.component.html`):** Agora, vamos criar o HTML para o formulário de adição e a lista de tarefas.

      * Abra `src/app/components/task-list/task-list.component.html` e substitua seu conteúdo.

    <!-- end list -->

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

3.  **O Estilo (`task-list.component.css`):** Por fim, adicione um pouco de CSS para a aplicação ficar mais agradável.

      * Abra `src/app/components/task-list/task-list.component.css` e adicione o código abaixo.

    <!-- end list -->

    ```css
    /* src/app/components/task-list/task-list.component.css */
    .container { max-width: 600px; margin: 2rem auto; font-family: sans-serif; padding: 1rem; }
    .form-add { display: flex; margin-bottom: 1.5rem; }
    .form-add input { flex-grow: 1; padding: 0.8rem; border: 1px solid #ccc; border-radius: 4px 0 0 4px; }
    .form-add button { padding: 0.8rem 1.2rem; border: none; background-color: #007bff; color: white; cursor: pointer; border-radius: 0 4px 4px 0; }
    .task-list { list-style: none; padding: 0; }
    .task-list li { display: flex; align-items: center; padding: 0.8rem; border-bottom: 1px solid #eee; }
    .task-list li:last-child { border-bottom: none; }
    .task-list li span { flex-grow: 1; margin-left: 1rem; }
    .task-list li span.completed { text-decoration: line-through; color: #888; }
    .delete-btn { border: none; background: transparent; color: #ff4d4d; cursor: pointer; font-size: 1.2rem; font-weight: bold; }
    ```

-----

#### **Passo 5: Rodando a Aplicação Completa\!**

É a hora da verdade\! Vamos conectar o frontend e o backend.

1.  **Inicie o Backend:** Garanta que sua API Spring Boot (`todolist-api`) esteja em execução.
2.  **Inicie o Frontend:** Em um novo terminal, na pasta do projeto Angular (`todolist-web`), execute:
    ```bash
    ng serve --open
    ```
    Seu navegador abrirá automaticamente em `http://localhost:4200`. Você deverá ver sua aplicação de lista de tarefas funcionando, pronta para adicionar, atualizar e remover itens.

-----

### **Conclusão do Módulo e Próximos Passos**

Parabéns\! Você construiu uma aplicação full-stack funcional com um backend robusto e um frontend moderno e reativo.

O ponto mais importante aqui é o **desacoplamento**: o frontend não sabe (e não precisa saber) nada sobre como o backend foi construído; ele apenas consome uma API.

Para provar o poder dessa arquitetura, nosso próximo módulo demonstrará essa flexibilidade de forma prática.

**Próxima Etapa: Módulo 3 - Construindo a Interface Desktop com JavaFX**

Vamos construir um segundo cliente, um aplicativo desktop nativo, que irá consumir **exatamente a mesma API backend** que nosso site Angular está usando, sem que nenhuma linha de código no servidor precise ser alterada. Isso solidificará o conceito de que uma API bem construída pode servir a múltiplos tipos de clientes (web, desktop, mobile) simultaneamente.

---

### [ricardotecpro.github.io](https://ricardotecpro.github.io/)
