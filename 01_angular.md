## Frontend Web usando Angular

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

### **Próxima Etapa (Versão Standalone): Construindo a Interface Web com Angular**

O objetivo e os passos de geração de arquivos são os mesmos, mas a forma como conectamos as dependências (como o `HttpClient` para fazer requisições e o `FormsModule` para formulários) é feita diretamente nos componentes ou na configuração central da aplicação, sem um `app.module.ts`.

#### **Passos 1 e 2: Geração de Arquivos**

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













Esses erros de compilação são muito comuns e o log de erros do Angular é excelente, pois nos diz exatamente onde está o problema. Vamos resolver isso.

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
