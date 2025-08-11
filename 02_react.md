# Sequência didática para um curso de React, do zero ao avançado

## com foco em uma experiência de aprendizado clara e prática para ambientes Windows e Linux.

Vamos começar essa jornada\! 🚀

-----

## **Curso Definitivo de React ⚛️: Do Zero ao Avançado**

**Bem-vindo(a) ao curso que irá transformar você em um(a) desenvolvedor(a) React\!**

Este guia foi desenhado para levar você desde os primeiros passos na configuração do ambiente, em Windows ou Linux, até tópicos avançados como gerenciamento de estado profissional e otimização de performance.

### **Módulo 1: A Fundação - Primeiros Passos no Ecossistema React 🌍**

Vamos começar preparando nosso ambiente e entendendo por que o React é tão poderoso.

#### **Aula 1: O que é React e Configuração do Ambiente 🛠️**

  * **Por que React?**
      * O que é uma biblioteca vs. um framework.
      * O conceito de **Virtual DOM** e como ele torna as atualizações de UI eficientes.
      * Pensamento declarativo: "Diga o que você quer, não como fazer".
  * **Preparando o Ambiente (Node.js + npm):**
      * **Windows:** A forma mais fácil é baixar o instalador LTS do [site oficial do Node.js](https://nodejs.org/). Ele já vem com o npm.
      * **Linux:** A melhor prática é usar um gerenciador de versões como o `nvm` (Node Version Manager).
        ```bash
        # Instala o nvm (pode variar um pouco, consulte o repo oficial)
        curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash

        # Instala a versão LTS (Long Term Support) do Node.js
        nvm install --lts
        ```
      * **Verificação:** Abra seu terminal (CMD/PowerShell no Windows, Terminal no Linux) e digite `node -v` e `npm -v` para confirmar a instalação.

#### **Aula 2: Criando seu Primeiro Projeto com Vite ⚡**

  * **Vite, a Ferramenta de Build Moderna:** Esqueça o antigo `create-react-app`. Vite é incrivelmente mais rápido\!
  * **Criando o projeto:** No seu terminal, execute o comando:
    ```bash
    npm create vite@latest meu-primeiro-app -- --template react
    ```
  * **Navegando na Estrutura de Pastas 📂:**
      * `src`: Onde todo o nosso código-fonte viverá.
      * `src/main.jsx`: O ponto de entrada da nossa aplicação.
      * `src/App.jsx`: Nosso primeiro componente React.
  * **Rodando a aplicação:**
    ```bash
    cd meu-primeiro-app
    npm install  # Instala as dependências
    npm run dev  # Inicia o servidor de desenvolvimento
    ```
  * Seu primeiro "Olá, Mundo React"\! 🎉

-----

### **Módulo 2: Os Pilares do React - Componentes e JSX 🧱**

Agora vamos entender os blocos de construção fundamentais de qualquer aplicação React.

#### **Aula 3: JSX - Misturando HTML e JavaScript 📝**

  * **O que é JSX?** Uma extensão de sintaxe para JavaScript que se parece com HTML.
  * **Regras do JSX:**
      * Todo componente deve retornar um único elemento raiz (use `<>` - Fragments - para agrupar).
      * Atributos HTML como `class` se tornam `className`.
      * Use chaves `{}` para "escapar" para o JavaScript (ex: `<h1>{nomeDoUsuario}</h1>`).
  * **Exemplo Prático:** Criando um componente de cartão de perfil com dados dinâmicos.

#### **Aula 4: Componentes Funcionais e Props 👨‍👩‍👧**

  * **Componentes são Funções:** A maneira moderna de escrever React é usando funções que retornam JSX.
  * **Props (Propriedades):** Como passar dados de um componente "pai" para um componente "filho".
  * **Exemplo Prático:**
      * Criar um componente `CartaoDeVideo` que recebe `titulo` e `urlDaThumbnail` como props.
      * No `App.jsx`, renderizar vários `CartaoDeVideo`, cada um com props diferentes.

-----

### **Módulo 3: Interatividade e Estado da Aplicação 🎮**

Vamos fazer nossa aplicação reagir às ações do usuário.

#### **Aula 5: O Hook `useState` - Memória para Componentes 🧠**

  * **O que são Hooks?** Funções especiais que nos permitem usar recursos do React (como o estado) em componentes funcionais.
  * **`useState`:** O hook fundamental para adicionar estado a um componente.
  * **Exemplo Prático:** Construir um componente de contador que incrementa um número a cada clique no botão. 🔢

#### **Aula 6: Lidando com Eventos e Formulários ✍️**

  * **Eventos:** `onClick`, `onChange`, `onSubmit`, etc.
  * **Componentes Controlados (Controlled Components):** A maneira React de lidar com formulários. O estado do React é a "única fonte da verdade".
  * **Exemplo Prático:** Criar um formulário de login com campos de e-mail e senha cujo estado é gerenciado pelo `useState`.

-----

### **Módulo 4: Ciclo de Vida e Efeitos Colaterais 🔄**

O que fazer quando precisamos interagir com o "mundo exterior" (APIs, timers, etc.)?

#### **Aula 7: O Hook `useEffect` - Sincronizando com o Exterior 📡**

  * **O que são "Efeitos Colaterais" (Side Effects)?** Qualquer coisa que um componente faz além de renderizar a UI (ex: buscar dados, manipular o DOM diretamente).
  * **Sintaxe do `useEffect`:** A função e o array de dependências.
  * **Casos de Uso Comuns:**
    1.  **Executar na montagem:** Buscar dados de uma API quando o componente aparece na tela (`[]`).
    2.  **Executar em atualizações:** Reagir a mudanças em uma variável de estado ou prop (`[minhaVariavel]`).
  * **Exemplo Prático:** Criar um componente que busca e exibe uma lista de posts de uma API pública como a [JSONPlaceholder](https://jsonplaceholder.typicode.com/).

-----

### **Módulo 5: Construindo Aplicações Maiores 🏗️**

Vamos aprender as técnicas para organizar e escalar nossos projetos.

#### **Aula 8: Roteamento com React Router DOM 🗺️**

  * **O que é uma SPA (Single Page Application)?**
  * **Instalando o React Router:** `npm install react-router-dom`.
  * **Configurando Rotas:** `BrowserRouter`, `Routes`, `Route`, e `Link`.
  * **Exemplo Prático:** Criar uma aplicação com 3 páginas: Home, Sobre, e Contato, e navegar entre elas sem recarregar a página.

#### **Aula 9: Estratégias de Estilização 💅**

  * **CSS Simples e CSS Modules:** Como importar arquivos CSS e o poder do escopo local.
  * **CSS-in-JS (Styled Components):** Escrevendo CSS diretamente no seu arquivo JavaScript.
  * **Frameworks de UI (Tailwind CSS):** Uma abordagem "utility-first" para estilização rápida.
  * **Exemplo Prático:** Estilizar um componente de botão usando duas abordagens diferentes para comparar.

-----

### **Módulo 6: Hooks Avançados e Padrões de Código ✨**

Vamos elevar nosso nível de React e escrever código mais limpo e performático.

#### **Aula 10: `useContext` - Fugindo do "Prop Drilling"  useContext**

  * **O Problema do "Prop Drilling":** Passar props por vários níveis de componentes.
  * **A Context API:** Uma forma de compartilhar estado globalmente sem passar props manualmente.
  * **Exemplo Prático:** Criar um "trocador de tema" (Claro/Escuro) que afeta a aplicação inteira, usando `useContext`. ☀️🌙

#### **Aula 11: `useReducer` - Gerenciando Estados Complexos ⚙️**

  * **Quando `useState` não é suficiente?**
  * **A Lógica do `useReducer`:** `estado`, `ação` (action) e o `redutor` (reducer).
  * **Exemplo Prático:** Refatorar um formulário complexo ou uma lista de tarefas (adicionar, remover, concluir) para usar `useReducer`.

#### **Aula 12: Otimização com `useMemo` e `useCallback` ⚡**

  * **O que é Memoização?** Armazenar o resultado de cálculos pesados para não os refazer desnecessariamente.
  * **`useMemo`:** Para memorizar valores/resultados de funções.
  * **`useCallback`:** Para memorizar a própria definição de uma função.
  * **Exemplo Prático:** Otimizar um componente que filtra uma lista grande de itens.

#### **Aula 13: Criando Hooks Personalizados 🎣**

  * **A Regra de Ouro:** "Não repita a si mesmo" (Don't Repeat Yourself - DRY).
  * **Extraindo Lógica Reutilizável:** Como criar seus próprios hooks (ex: `useFetch`, `useLocalStorage`).
  * **Exemplo Prático:** Criar um hook `useFetch` que encapsula toda a lógica de `useEffect` para buscar dados de uma API.

-----

### **Módulo 7: Gerenciamento de Estado Profissional 🗄️**

Para aplicações muito grandes, um gerenciador de estado dedicado se torna essencial.

#### **Aula 14: Introdução ao Redux com Redux Toolkit 🛒**

  * **Por que Redux?** Estado global previsível, depuração poderosa.
  * **Redux Toolkit (RTK):** A forma moderna e simplificada de usar Redux.
  * **Conceitos do RTK:** `configureStore`, `createSlice` (que combina actions e reducers).
  * **Exemplo Prático:** Construir um carrinho de compras simples onde o estado é gerenciado pelo Redux.

-----

### **Módulo 8: Tópicos Avançados e Ecossistema 🔬**

Vamos explorar ferramentas e conceitos que completam o conhecimento de um desenvolvedor React sênior.

#### **Aula 15: Testando sua Aplicação com Vitest e RTL ✅**

  * **Por que testar?**
  * **Vitest:** Um framework de testes moderno e rápido, perfeito para projetos Vite.
  * **React Testing Library (RTL):** Testando seus componentes da forma como o usuário os utiliza.
  * **Exemplo Prático:** Escrever testes para um formulário de login (renderização e interação).

#### **Aula 16: Integrando com TypeScript 🇹**

  * **Tipagem Estática no JavaScript:** Adicionando segurança e autocompletar ao seu projeto.
  * **Iniciando um projeto com o template `react-ts`.**
  * **Tipando Props e Estado (`useState<Tipo>()`).**
  * **Exemplo Prático:** Converter um componente JavaScript simples para TypeScript.

-----

### **Módulo 9: Projeto Final - Construindo uma Aplicação Completa 🏆**

Vamos unir todo o conhecimento adquirido para criar um projeto do mundo real.

#### **Projeto: "Blog Pessoal" ou "Gerenciador de Projetos (Kanban)"**

  * **Requisitos:**
      * Múltiplas páginas usando **React Router**.
      * Busca de dados de uma API (pode ser uma API fake como a JSONPlaceholder ou uma que você mesmo construiu).
      * Autenticação de usuário simulada.
      * Gerenciamento de estado global (com **Context API** ou **Redux Toolkit**) para dados do usuário e temas.
      * Formulários para criar e editar conteúdo.
      * Código limpo e reutilizável com **Hooks Personalizados**.

Ao final deste curso, você não apenas saberá como criar aplicações React, mas também entenderá os padrões e as melhores práticas para construir software escalável, performático e de alta qualidade. **Parabéns\!** 🎉