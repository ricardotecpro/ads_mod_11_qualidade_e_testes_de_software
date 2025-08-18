Desmistificando o design e focando em ferramentas e processos práticos.

-----

### **Arquivo 1: `modulo-01-fundamentos-ui-ux.md`**

````markdown
# 🧠 Módulo 1: Fundamentos de UI/UX para Mentes Lógicas

Bem-vindo! Este módulo é a camada de base. Vamos traduzir os conceitos de design, muitas vezes vistos como "subjetivos", em princípios lógicos e regras que um programador pode entender e aplicar imediatamente. O objetivo é construir um *mindset* focado no usuário.

## 🤔 Aula 1: UI não é UX - Desvendando os Conceitos

É o erro mais comum. Vamos esclarecer de uma vez por todas.

- **UX (User Experience - Experiência do Usuário):** É a jornada completa, a sensação geral do usuário ao interagir com o produto. É sobre a **lógica, o fluxo e a eficiência**.
  - *Pergunta-chave:* "O usuário conseguiu resolver seu problema de forma fácil e agradável?"
  - *Analogia para Devs:* UX é a **arquitetura do sistema**. Define os fluxos de dados, os casos de uso e a lógica de negócios para garantir que o sistema seja robusto e eficiente.

- **UI (User Interface - Interface do Usuário):** É a parte visual e interativa, a superfície do produto. É sobre **cores, tipografia, espaçamento e componentes**.
  - *Pergunta-chave:* "A interface é clara, bonita e fácil de usar?"
  - *Analogia para Devs:* UI são os **componentes da sua biblioteca de frontend** (React, Vue, etc.) e o CSS que os estiliza.

```mermaid
graph TD
    subgraph Experiência do Produto
        A(UX - A Jornada)
        B(UI - Os Pontos de Contato)
    end
    A -- "Define o fluxo e a estrutura" --> B
    B -- "Apresenta visualmente a jornada" --> A
    
    style A fill:#cde4ff
    style B fill:#e7cfff
````

## ✅ Aula 2: As Leis da UX - Heurísticas de Nielsen

Jakob Nielsen definiu 10 "regras de ouro" de usabilidade que são como *unit tests* para a sua interface. Elas ajudam a identificar problemas de usabilidade de forma sistemática.

1.  **Visibilidade do estado do sistema:** Mantenha o usuário informado (ex: spinners de loading, mensagens de sucesso).
2.  **Correspondência entre o sistema e o mundo real:** Fale a língua do usuário. Use ícones e termos familiares (ex: um ícone de lixeira para apagar).
3.  **Controle e liberdade do usuário:** Permita que o usuário possa voltar e desfazer ações (ex: um botão "Cancelar" ou `Ctrl+Z`).
4.  **Consistência e padrões:** Um botão de "salvar" deve ter sempre a mesma aparência e comportamento em todo o sistema.
5.  **Prevenção de erros:** É melhor prevenir o erro do que exibir uma mensagem de erro (ex: desabilitar um botão "Salvar" até que o formulário esteja válido).

## 🎨 Aula 3: Princípios Fundamentais de UI

Estes são os blocos de construção de uma interface visualmente agradável e funcional.

  - **Hierarquia Visual:** Guie o olho do usuário para o que é mais importante. Use tamanho, cor e peso da fonte para criar uma ordem de leitura clara.
  - **Contraste:** Garante a legibilidade. Texto e fundo devem ter cores com contraste suficiente, especialmente para acessibilidade (WCAG).
  - **Espaço em Branco (Negative Space):** É a "respiração" do design. Evita que a interface pareça lotada e ajuda a agrupar elementos relacionados.
  - **Repetição e Alinhamento:** Crie um ritmo visual. Alinhe os elementos em uma grade e repita estilos para criar consistência.
  - **Teoria das Cores:**
      - **Psicologia:** Cores evocam emoções (azul = confiança, vermelho = urgência).
      - **Regra 60-30-10:** Use 60% de uma cor primária, 30% de uma secundária e 10% para destaques (accents).

<!-- end list -->

````

---

### **Arquivo 2: `modulo-02-processo-ux.md`**

```markdown
# 🗺️ Módulo 2: O Processo de UX - Da Ideia à Solução

Design não é sobre inspiração divina, é sobre seguir um processo. Para programadores, pensar em UX é como pensar no ciclo de desenvolvimento de software: entender os requisitos antes de começar a codificar.

## 💎 Aula 1: O Diamante Duplo - Um Processo para Chamar de Seu

O Diamante Duplo é um modelo de processo de design que divide o trabalho em 4 fases, alternando entre pensamento divergente (explorar ideias) e convergente (focar em soluções).

```mermaid
graph LR
    A(Problema) --> B{Descobrir};
    B -- "Pesquisa, Entrevistas (Divergente)" --> C{Definir};
    C -- "Personas, Jornadas (Convergente)" --> D{Desenvolver};
    D -- "Ideação, Protótipos (Divergente)" --> E{Entregar};
    E -- "Testes, Validação (Convergente)" --> F(Solução);

    style B fill:#cde4ff
    style D fill:#cde4ff
    style C fill:#e7cfff
    style E fill:#e7cfff
````

  - **Fase 1: Descobrir:** Pesquisar e entender o problema do usuário, sem pensar em soluções.
  - **Fase 2: Definir:** Analisar a pesquisa e definir claramente qual é o problema principal a ser resolvido.
  - **Fase 3: Desenvolver:** Gerar o máximo de ideias possíveis para a solução (brainstorming, sketches).
  - **Fase 4: Entregar:** Construir, testar e refinar um protótipo da solução escolhida.

## 👥 Aula 2: Conhecendo o Usuário

Você não é o seu usuário. Para construir algo útil, você precisa entender para quem está construindo.

  - **Personas:** São arquétipos de usuários, personagens fictícios criados a partir de dados de pesquisa. Ajudam a criar empatia e a tomar decisões de design centradas no usuário.

      - *Exemplo:* "Ana, 35 anos, gerente de projetos, usuária de múltiplos apps de produtividade, precisa de uma forma rápida de delegar tarefas pelo celular."

  - **Mapas da Jornada do Usuário (User Journey Maps):** Visualizam a experiência do usuário passo a passo enquanto ele tenta atingir um objetivo. Mapeia ações, pensamentos, sentimentos e pontos de dor.

<!-- end list -->

```mermaid
usecaseDiagram
    actor "Ana (Persona)" as Ana
    Ana --> (Acessa o App)
    (Acessa o App) --> (Tenta criar tarefa)
    (Tenta criar tarefa) --> (Busca por "delegar")
    (Busca por "delegar") --> (Não encontra a opção) : "Ponto de Dor 😫"
    (Não encontra a opção) --> (Abandona o App)
```

## 📝 Aula 3: Wireframes e Protótipos

Antes de escrever o código final, você cria um rascunho. O mesmo vale para o design.

  - **Wireframe de Baixa Fidelidade (Low-fi):** Esboços básicos, feitos com papel e caneta ou ferramentas simples. Foco total na estrutura e no fluxo, sem se preocupar com cores ou fontes.
  - **Wireframe de Média Fidelidade (Mid-fi):** Layouts mais definidos, geralmente em tons de cinza. Foco no espaçamento, hierarquia e posicionamento dos componentes.
  - **Protótipo de Alta Fidelidade (Hi-fi):** A representação visual final da interface. Inclui cores, fontes, ícones e interatividade, parecendo o produto real. É o que geralmente é feito no Figma.

<!-- end list -->

````

---

### **Arquivo 3: `modulo-03-figma-para-programadores.md`**

```markdown
# 🛠️ Módulo 3: Figma para Desenvolvedores - Mão na Massa

Figma é a ferramenta de design de interface mais popular hoje. Para um dev, entendê-la é como ter acesso ao "código-fonte" do design. Este módulo é focado nas funcionalidades que mais importam para a implementação.

## 🖥️ Aula 1: Tour pela Interface
Vamos nos familiarizar com o ambiente:
- **Canvas:** A área de trabalho infinita.
- **Painel de Camadas (Layers Panel):** A estrutura de árvore dos seus elementos, similar ao DOM.
- **Painel de Propriedades (Properties Panel):** Onde você edita estilos (cores, fontes, etc.), similar a um painel de CSS.
- **Barra de Ferramentas:** Para criar formas, texto e frames.

## ✨ Aula 2: O Essencial para Devs - A Tríade do Poder

Estas três funcionalidades do Figma mapeiam diretamente para conceitos de desenvolvimento front-end. Dominá-las é fundamental.

1.  **Frames:** São os contêineres do seu design. Pense neles como um `<div>` ou o `<body>` da sua página. Eles definem os limites da sua tela ou componente.

2.  **Auto Layout:** **A funcionalidade mais importante para um programador.** É a implementação visual de **Flexbox** e **Grid**. Permite criar componentes que crescem e se adaptam ao conteúdo.
    - **Propriedades:** Direção (vertical/horizontal), espaçamento entre itens, padding.
    - **Benefício:** Você cria um design que se comporta exatamente como o layout que você irá codificar, eliminando adivinhação.

3.  **Components & Variants:** A base de qualquer design system.
    - **Component:** Um elemento de UI reutilizável (ex: um botão). Pense nele como uma **classe** ou um **componente React/Vue**.
    - **Variant:** Uma variação de um componente (ex: botão primário, secundário, desabilitado, com ícone). Pense nelas como as **props** do seu componente.

```mermaid
classDiagram
    class Button {
        <<Componente Base>>
        +Label
        +Icon
    }
    class "Primary Button" {
        <<Variante>>
        state: default
        state: hover
        state: disabled
    }
    class "Secondary Button" {
        <<Variante>>
        state: default
        state: hover
    }

    Button <|-- "Primary Button"
    Button <|-- "Secondary Button"
````

## 🔗 Aula 3: Prototipagem Interativa

O Figma permite conectar seus frames para criar um fluxo navegável, simulando a experiência do usuário.

  - **Conexões:** Arraste "macarrões" de um botão para outra tela.
  - **Interações:** Defina gatilhos (`On Click`, `While Hovering`).
  - **Animações:** Use transições suaves (`Smart Animate`) para simular animações de UI.
  - **Benefício para o Dev:** Você pode entender e validar o fluxo completo da aplicação antes de escrever uma única linha de código.

## 🔌 Aula 4: Plugins que Salvam Vidas

  - **Content Reel:** Preenche seu design com dados falsos (nomes, avatares, textos).
  - **Unsplash:** Insere imagens de alta qualidade diretamente no Figma.
  - **Iconify:** Acesso a milhares de ícones (Font Awesome, Material Icons) em formato vetorial (SVG).

<!-- end list -->

````

---

### **Arquivo 4: `modulo-04-design-systems-material-design.md`**

```markdown
# 📚 Módulo 4: Design Systems e Google Material Design

Se componentes são variáveis, um Design System é a biblioteca inteira. Para programadores, essa é a forma mais estruturada e escalável de pensar em design. É a "API da UI".

## 🧬 Aula 1: O que é um Design System?

Um Design System é a **única fonte da verdade (Single Source of Truth)** que agrupa todos os elementos que permitem que as equipes projetem, realizem e desenvolvam um produto.
- **Não é apenas um UI Kit:** Ele vai além dos componentes visuais.
- **Componentes Principais:**
  1.  **Biblioteca de Componentes:** Os botões, formulários, cards, etc. (o "código").
  2.  **Tokens de Design (Design Tokens):** Variáveis que armazenam atributos visuais. Ex: `$color-primary-500: #3F51B5;`, `$font-size-md: 16px;`. Mapeiam diretamente para variáveis CSS ou constantes no código.
  3.  **Diretrizes e Documentação:** As "regras" de como usar os componentes e tokens (a "documentação da API").

## 🧱 Aula 2: Anatomia do Google Material Design

Material Design é o Design System do Google. É um excelente ponto de partida por ser maduro, bem documentado e ter bibliotecas de código para a maioria dos frameworks.
- **Princípios Fundamentais:**
  - **Material é a Metáfora:** A interface se comporta como papel e tinta, com superfícies e elevação (sombras).
  - **Ousado, Gráfico, Intencional:** Uso de cores vibrantes, tipografia clara e hierarquia para guiar o usuário.
  - **Movimento Gera Significado:** Animações não são apenas enfeites, elas dão feedback e guiam a atenção do usuário.

## 🔧 Aula 3: Componentes e Tokens na Prática
O Material Design define uma vasta gama de componentes prontos para uso:
- **Botões:** `Text`, `Outlined`, `Contained`.
- **Campos de Texto:** `Filled`, `Outlined`.
- **Cards, Diálogos, Menus, etc.**

### Tokens de Design: A Ponte para o Código
A forma mais eficiente de usar um design system é com tokens.
- **No Figma:** Usando `Styles` para cores e tipografia.
- **No Código:**
```css
/* Exemplo de uso de tokens em CSS */
:root {
  --color-primary: #6200EE;
  --font-size-button: 14px;
  --border-radius-medium: 4px;
}

.button-primary {
  background-color: var(--color-primary);
  font-size: var(--font-size-button);
  border-radius: var(--border-radius-medium);
}
````

## 🚀 Aula 4: Laboratório - Construindo com Material Design no Figma

Nesta aula prática, vamos ao **Figma Community** e buscamos por um "Material 3 Design Kit".

1.  **Duplicar o Kit:** Teremos acesso a todos os componentes e estilos do Material Design.
2.  **Montar uma Tela:** Vamos arrastar e soltar componentes para construir uma tela de login em minutos.
3.  **Customizar Tokens:** Vamos alterar a cor primária no painel de estilos e ver a mágica acontecer: todos os componentes que usam essa cor são atualizados instantaneamente. Isso simula a troca de um tema no app.

<!-- end list -->

````

---

### **Arquivo 5: `modulo-05-design-para-codigo.md`**

```markdown
# 🌉 Módulo 5: A Ponte entre Design e Código - O Handoff Perfeito

Este é o módulo final, onde tudo se conecta. O "handoff" é o processo de entregar o design para a equipe de desenvolvimento. Um bom handoff economiza horas de trabalho e evita inconsistências.

##📋 Aula 1: O que um Dev Precisa? A "API" do Design

Um desenvolvedor precisa de três coisas de um design para poder implementá-lo com precisão:
1.  **Especificações (Specs):** Medidas exatas de espaçamentos, tamanhos de fonte, códigos de cores, etc.
2.  **Assets:** Ícones (preferencialmente em SVG), imagens e outras mídias, já otimizados para a web.
3.  **Protótipo Interativo:** O fluxo de telas para entender a navegação e as interações.

## 🔍 Aula 2: Figma Dev Mode - O Melhor Amigo do Programador

O Figma possui um modo de visualização específico para desenvolvedores (`</>`).
- **Inspeção de Elementos:** Clique em qualquer elemento para ver suas propriedades CSS, iOS ou Android.
- **Medidas Automáticas:** Passe o mouse sobre um elemento e segure `Alt/Option` para ver as distâncias em relação aos elementos vizinhos.
- **Exportação de Assets:** Selecione um ícone ou imagem e exporte diretamente em SVG, PNG, etc.
- **Code Snippets:** Ele gera código de exemplo, que serve como um bom ponto de partida (mas não deve ser copiado e colado cegamente).

```mermaid
sequenceDiagram
    participant Designer as Designer
    participant Figma as Figma (Dev Mode)
    participant Developer as Desenvolvedor

    Designer->>Figma: Cria o design e componentes
    Designer->>Developer: Compartilha o link do Figma
    Developer->>Figma: Abre em Dev Mode
    Figma-->>Developer: Mostra specs, CSS, assets
    Developer->>Developer: Traduz design para código de componentes
````

## 🔄 Aula 3: Mapeando Componentes Figma para Componentes de Código

A verdadeira magia acontece quando a estrutura do Figma reflete a estrutura do seu código.

  - **Componente Figma (`Button`):** Corresponde a um componente `Button.jsx` no React.
  - **Variantes Figma (`primary`, `size='large'`):** Correspondem às `props` do seu componente (`<Button variant="primary" size="large">`).
  - **Texto e Ícones:** Correspondem ao `children` ou a `props` específicas do componente.
  - **Auto Layout:** Mapeia diretamente para as propriedades do Flexbox em CSS (`display: flex`, `flex-direction`, `gap`, `padding`).

\#\#📱 Aula 4: Design Responsivo no Figma

Uma aplicação precisa funcionar em múltiplos tamanhos de tela. O Figma nos ajuda a projetar isso.

  - **Constraints (Restrições):** Regras que fixam um elemento a um dos lados do seu `Frame` pai (topo, base, esquerda, direita). Útil para layouts mais simples.
  - **Auto Layout (Novamente\!):** A melhor forma de criar layouts responsivos. Ao definir as regras de `Hug contents` (abraçar conteúdo) ou `Fill container` (preencher contêiner), você cria um comportamento que se adapta naturalmente, assim como no CSS moderno.
  - **Prática:** Criar um card de perfil e garantir que ele se adapte corretamente de uma tela de 360px (mobile) para uma de 1280px (desktop).

-----

### **Arquivo 6: `sugestoes-manutencao-ui-ux.md`**

```markdown
# ✨ Sugestões Adicionais para Manter a Qualidade no Longo Prazo

O mundo do design e das ferramentas evolui rapidamente. Manter este curso relevante exige atenção constante.

## 🔄 1. Acompanhar as Atualizações do Figma

- **Figma Config:** A conferência anual do Figma sempre traz novidades massivas (como o Dev Mode). É crucial assistir e incorporar as novas funcionalidades ao curso.
- **Revisão Semestral:** A cada 6 meses, revise a interface e os exemplos do Figma para garantir que não estejam desatualizados.

## 📚 2. Evolução dos Design Systems

- **Material Design:** O Google lança novas versões (Material 2, Material 3). O curso deve ser atualizado para refletir as diretrizes mais recentes.
- **Outros Design Systems:** Considere adicionar uma aula bônus sobre outros design systems populares, como o **Ant Design** ou o **Atlassian Design System**, para dar aos alunos uma visão mais ampla.

## ♿ 3. Foco Crescente em Acessibilidade (a11y)

- **Módulo de Acessibilidade:** Este é um tópico cada vez mais importante. Crie um módulo opcional dedicado a projetar para acessibilidade.
  - **Tópicos:** Contraste de cores (WCAG), navegação por teclado, design para leitores de tela.
  - **Plugins:** Apresente plugins do Figma que ajudam a verificar o contraste e outras regras de acessibilidade.

## 🤝 4. Aprofundar a Colaboração Dev-Design

- **Ferramentas de Handoff:** Explore e mencione outras ferramentas que se integram ao Figma, como o **Storybook**, que permite criar uma documentação viva de componentes de código, conectando o design à implementação real.
- **Feedback dos Alunos:** Use o feedback de programadores que fizeram o curso para refinar os exemplos e focar ainda mais nas dores e necessidades específicas dessa ponte entre design e desenvolvimento.
```