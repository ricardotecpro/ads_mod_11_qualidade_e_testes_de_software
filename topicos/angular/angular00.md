**Tutorial de Angular** para conectar com a API Spring Boot. O objetivo aqui é desenvolver um front-end simples utilizando Angular que interage com a API RESTful desenvolvida no Spring Boot para exibir e manipular dados de produtos.

---

# **Tutorial: Conectando Angular com Spring Boot**

### **1. Preparação do Ambiente**

Antes de começarmos, é necessário ter as seguintes ferramentas instaladas:

- **Node.js** (recomenda-se a versão 14.x ou superior): [Baixe o Node.js](https://nodejs.org/).
- **Angular CLI**: Você pode instalar o Angular CLI globalmente com o seguinte comando:
  ```bash
  npm install -g @angular/cli
  ```
- **IDE** para trabalhar com Angular (como VS Code, WebStorm, etc.).

Certifique-se também de que o **Spring Boot** está funcionando corretamente e a API REST está acessível em `http://localhost:8080/produtos`.

---

### **2. Criando o Projeto Angular**

Vamos agora criar um novo projeto Angular para interagir com a nossa API Spring Boot.

1. **Criar um novo projeto Angular**:
   No terminal, execute o seguinte comando para criar um novo projeto Angular:
   ```bash
   ng new frontend --no-standalone
   ```

   O Angular CLI vai te perguntar várias opções de configuração. Você pode aceitar as configurações padrão (pressionando Enter) para a maioria das opções.

2. **Entrar na pasta do projeto**:
   Depois de criar o projeto, entre no diretório do projeto:
   ```bash
   cd frontend
   ```

3. **Instalar o Angular HTTP Client**:
   O Angular utiliza o **HttpClientModule** para fazer requisições HTTP. Vamos adicionar essa dependência ao projeto. No Angular, ele já vem integrado, mas você precisa importá-lo no módulo principal.

   No arquivo `src/app/app.module.ts`, faça as seguintes modificações:

   ```typescript
   import { NgModule } from '@angular/core';
   import { BrowserModule } from '@angular/platform-browser';
   import { AppComponent } from './app.component';
   import { HttpClientModule } from '@angular/common/http';  // Importando o HttpClientModule

   @NgModule({
     declarations: [
       AppComponent
     ],
     imports: [
       BrowserModule,
       HttpClientModule  // Adicionando o HttpClientModule aqui
     ],
     providers: [],
     bootstrap: [AppComponent]
   })
   export class AppModule { }
   ```

---

### **3. Criando o Serviço para a Comunicação com o Spring Boot**

Agora vamos criar um serviço no Angular que será responsável por fazer as requisições HTTP para o backend (Spring Boot).

1. **Criar o Serviço**:
   Utilize o Angular CLI para gerar o serviço. No terminal, execute:
   ```bash
   ng generate service produto
   ```

   Isso criará um arquivo chamado `produto.service.ts` dentro do diretório `src/app/`.

2. **Modificando o Serviço**:
   Agora edite o arquivo `produto.service.ts` para realizar as operações de **GET** (para listar os produtos).

   ```typescript
   import { Injectable } from '@angular/core';
   import { HttpClient } from '@angular/common/http';
   import { Observable } from 'rxjs';

   // Definindo a interface para o produto
   export interface Produto {
     id: number;
     nome: string;
     preco: number;
   }

   @Injectable({
     providedIn: 'root'
   })
   export class ProdutoService {

     private apiUrl = 'http://localhost:8080/produtos';  // URL da API do Spring Boot

     constructor(private http: HttpClient) { }

     // Método para obter todos os produtos
     getProdutos(): Observable<Produto[]> {
       return this.http.get<Produto[]>(this.apiUrl);
     }
   }
   ```

---

### **4. Exibindo os Produtos no Componente**

Agora, vamos exibir os produtos no componente principal da aplicação.

1. **Modificando o Componente Principal**:
   Abra o arquivo `src/app/app.component.ts` e edite-o da seguinte forma para chamar o serviço que criamos e exibir os produtos:

   ```typescript
   import { Component, OnInit } from '@angular/core';
   import { ProdutoService, Produto } from './produto.service';  // Importando o Serviço

   @Component({
     selector: 'app-root',
     templateUrl: './app.component.html',
     styleUrls: ['./app.component.css']
   })
   export class AppComponent implements OnInit {

     produtos: Produto[] = [];  // Lista de produtos

     constructor(private produtoService: ProdutoService) { }

     ngOnInit() {
       // Chama o serviço para obter os produtos
       this.produtoService.getProdutos().subscribe((dados) => {
         this.produtos = dados;
       });
     }
   }
   ```

2. **Modificando o Template HTML**:
   Agora, vamos exibir os produtos no arquivo `src/app/app.component.html`.

   ```html
   <div style="text-align:center">
     <h1>Lista de Produtos</h1>
     <ul>
       <li *ngFor="let produto of produtos">
         {{ produto.nome }} - R$ {{ produto.preco }}
       </li>
     </ul>
   </div>
   ```

---

### **5. Executando o Projeto Angular**

1. **Rodando a Aplicação Angular**:
   No terminal, dentro da pasta do projeto Angular (`frontend`), execute o comando para iniciar o servidor de desenvolvimento:

   ```bash
   ng serve
   ```

   Isso iniciará a aplicação Angular em `http://localhost:4200`.

2. **Verificando a Conexão**:
   Agora, abra o navegador e acesse `http://localhost:4200`. Você verá uma lista de produtos sendo exibida, que são consumidos da API Spring Boot.

---

### **6. Habilitando CORS no Spring Boot**

Como o Angular e o Spring Boot estarão rodando em portas diferentes (Angular em `localhost:4200` e Spring Boot em `localhost:8080`), o navegador pode bloquear as requisições devido à política de CORS (Cross-Origin Resource Sharing).

Para resolver isso, você precisa configurar o Spring Boot para permitir requisições CORS.

No Spring Boot, você pode configurar isso no **controller** ou globalmente.

#### **Configurando CORS no Controller**

Edite o seu **ProdutoController** para permitir CORS:

```java
package com.exemplo.demo.controllers;

import com.exemplo.demo.models.Produto;
import com.exemplo.demo.repositories.ProdutoRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@CrossOrigin(origins = "http://localhost:4200")  // Permitindo acesso ao Angular
public class ProdutoController {

    @Autowired
    private ProdutoRepository produtoRepository;

    @GetMapping("/produtos")
    public List<Produto> obterProdutos() {
        return produtoRepository.findAll();
    }
}
```

#### **Configurando CORS Globalmente**

Você também pode habilitar CORS globalmente, criando uma configuração de **WebMvcConfigurer**:

```java
package com.exemplo.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.servlet.config.annotation.CorsRegistry;
import org.springframework.web.servlet.config.annotation.WebMvcConfigurer;

@Configuration
public class WebConfig implements WebMvcConfigurer {

    @Override
    public void addCorsMappings(CorsRegistry registry) {
        registry.addMapping("/**").allowedOrigins("http://localhost:4200");
    }
}
```

---

### **7. Conclusão**

Agora você tem uma aplicação Angular conectada à sua API Spring Boot! Com esse tutorial, você:

- Criou um projeto Angular.
- Utilizou o **HttpClientModule** para fazer requisições HTTP.
- Criou um serviço Angular para consumir a API Spring Boot.
- Exibiu dados de produtos na interface do Angular.
- Configurou o CORS no Spring Boot para permitir requisições do front-end.

Agora você pode expandir o projeto para incluir funcionalidades como **adicionar**, **editar** e **excluir** produtos, autenticação com JWT, etc.


---

### [ricardotecpro.github.io](https://ricardotecpro.github.io/)
