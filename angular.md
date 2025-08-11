# Construindo o Frontend com Angular

Após criar a API, o próximo passo é desenvolver a interface web que irá interagir com ela.  
Utilizaremos **Angular** para criar uma *Single Page Application* (SPA) moderna e reativa.

---

## 1. Preparando o Ambiente e Criando o Projeto

### Pré-requisitos

Verifique se o Node.js e o Angular CLI estão instalados:

```bash
node -v
ng version
```

> **Nota:**  
> - Baixe o Node.js no [site oficial](https://nodejs.org/) se necessário.  
> - Para instalar o Angular CLI:  
>   ```bash
>   npm install -g @angular/cli
>   ```

---

### Criando o Projeto Angular

No terminal:

```bash
ng new todolist-web
```

Responda às perguntas:
- **Add Angular routing?** → `n`
- **Stylesheet format?** → `CSS`

Abra a pasta criada no VS Code.

---

### Gerando a Estrutura

```bash
cd todolist-web

# Modelo de dados
ng generate interface models/tarefa

# Serviço para consumir API
ng generate service services/tarefa

# Componente para listar tarefas
ng generate component components/task-list
```

---

## 2. Conectando o Frontend ao Backend

### Interface `Tarefa`

`src/app/models/tarefa.ts`:

```typescript
export interface Tarefa {
  id?: number;
  descricao: string;
  concluida: boolean;
}
```

---

### Opção A — Projeto com `app.module.ts`

**1. Configuração:**

```typescript
// src/app/app.module.ts
import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { FormsModule } from '@angular/forms';

import { AppComponent } from './app.component';
import { TaskListComponent } from './components/task-list/task-list.component';

@NgModule({
  declarations: [
    AppComponent,
    TaskListComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    FormsModule
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
```

**2. Serviço:**

```typescript
// src/app/services/tarefa.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Tarefa } from '../models/tarefa';

@Injectable({ providedIn: 'root' })
export class TarefaService {
  private apiUrl = 'http://localhost:8080/api/tarefas';

  constructor(private http: HttpClient) {}

  getTarefas(): Observable<Tarefa[]> {
    return this.http.get<Tarefa[]>(this.apiUrl);
  }

  addTarefa(tarefa: Tarefa): Observable<Tarefa> {
    return this.http.post<Tarefa>(this.apiUrl, tarefa);
  }

  updateTarefa(tarefa: Tarefa): Observable<Tarefa> {
    return this.http.put<Tarefa>(`${this.apiUrl}/${tarefa.id}`, tarefa);
  }

  deleteTarefa(id: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/${id}`);
  }
}
```

---

### Opção B — Projeto *Standalone*

`src/app/app.config.ts`:

```typescript
import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';
import { provideHttpClient } from '@angular/common/http';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient()
  ]
};
```

`src/app/app.component.ts`:

```typescript
import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { TaskListComponent } from './components/task-list/task-list.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, TaskListComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
export class AppComponent {
  title = 'todolist-web';
}
```

---

## 3. Componente `TaskListComponent`

**HTML (`app.component.html`):**
```html
<app-task-list></app-task-list>
```

**TypeScript:**
```typescript
import { Component, OnInit } from '@angular/core';
import { TarefaService } from '../../services/tarefa.service';
import { Tarefa } from '../../models/tarefa';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-task-list',
  standalone: true,
  imports: [CommonModule, FormsModule],
  templateUrl: './task-list.component.html',
  styleUrl: './task-list.component.css'
})
export class TaskListComponent implements OnInit {
  tarefas: Tarefa[] = [];
  novaTarefa: Tarefa = { descricao: '', concluida: false };

  constructor(private tarefaService: TarefaService) {}

  ngOnInit(): void {
    this.carregarTarefas();
  }

  carregarTarefas(): void {
    this.tarefaService.getTarefas().subscribe(data => this.tarefas = data);
  }

  adicionarTarefa(): void {
    if (!this.novaTarefa.descricao.trim()) return;
    this.tarefaService.addTarefa(this.novaTarefa).subscribe(tarefa => {
      this.tarefas.push(tarefa);
      this.novaTarefa = { descricao: '', concluida: false };
    });
  }

  atualizarStatus(tarefa: Tarefa): void {
    this.tarefaService.updateTarefa(tarefa).subscribe();
  }

  deletarTarefa(id?: number): void {
    if (id === undefined) return;
    this.tarefaService.deleteTarefa(id).subscribe(() => {
      this.tarefas = this.tarefas.filter(t => t.id !== id);
    });
  }
}
```

**HTML do componente:**
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

**CSS:**
```css
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

---

## 4. Executando

1. API Spring Boot rodando.  
2. No Angular:

```bash
ng serve --open
```

Acesse: [http://localhost:4200](http://localhost:4200)

---

## Erros Comuns

**Erro:**  
```
Property 'addTarefa' does not exist on type 'TarefaService'
```

**Solução:**  
Verifique se todos os métodos CRUD foram implementados no serviço `TarefaService`.
