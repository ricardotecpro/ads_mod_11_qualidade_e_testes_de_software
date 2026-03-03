# Quiz 05 - Interface Gráfica (UI) 🎨

1. Qual a diferença fundamental entre uma View e um ViewGroup?
    - [ ] Views são invisíveis e ViewGroups são visíveis
    - [x] View é um componente atômico (ex: Botão) e ViewGroup organiza outras Views (Layout)
    - [ ] ViewGroups não podem conter outras Views
    - [ ] Views são para Java e ViewGroups para Kotlin
    *Explicação: ViewGroups (como LinearLayout) funcionam como containers que organizam a posição das Views filhas.*

2. Por que o ConstraintLayout é recomendado como padrão para layouts modernos?
    - [ ] Porque ele é o mais antigo e estável
    - [x] Porque permite criar layouts complexos sem aninhamento excessivo, melhorando a performance
    - [ ] Porque ele só funciona com o mouse
    - [ ] Porque ele apaga o XML automaticamente
    *Explicação: Ele mantém a hierarquia do layout plana ("flat"), o que exige menos processamento do Android para desenhar a tela.*

3. Qual a unidade de medida correta para margens e tamanhos de botões?
    - [ ] px (Pixels)
    - [ ] sp (Scale-independent Pixels)
    - [x] dp (Density-independent Pixels)
    - [ ] cm (Centímetros)
    *Explicação: dp garante que o componente tenha o mesmo tamanho físico em telas com diferentes densidades de densidade.*

4. Quando usamos o `sp` em vez de `dp`?
    - [ ] Para imagens de alta resolução
    - [x] Para tamanhos de texto, respeitando a configuração de acessibilidade do usuário
    - [ ] Para cores de fundo
    - [ ] Para velocidades de animação
    *Explicação: sp escala conforme o tamanho da fonte que o usuário configurou nas opções do Android.*

5. O que faz o `LinearLayout` com `orientation="vertical"`?
    - [ ] Coloca os itens um ao lado do outro horizontalmente
    - [x] Empilha os itens um abaixo do outro em uma coluna
    - [ ] Centraliza todos os itens no meio da tela
    - [ ] Gira a tela do celular automaticamente
    *Explicação: A orientação define o sentido em que os novos componentes serão adicionados.*

6. Qual o equivalente no iOS (Xcode) ao sistema de constraints do Android?
    - [ ] Interface Builder
    - [x] Auto Layout
    - [ ] Cocoa Touch
    - [ ] UIKit
    *Explicação: Ambos usam o conceito de restrições (âncoras) para definir posições relativas entre componentes.*

7. Para que serve o `layout_weight` no LinearLayout?
    - [ ] Para definir o peso do app na Google Play
    - [x] Para distribuir o espaço restante entre os componentes de forma proporcional
    - [ ] Para aumentar a grossura das bordas do botão
    - [ ] Para pesar o código e torná-lo mais lento
    *Explicação: É uma forma de dizer "este botão deve ocupar 2x mais espaço que o outro".*

8. Como habilitamos o ViewBinding no projeto?
    - [ ] Instalando um plugin no Chrome
    - [x] No arquivo build.gradle, dentro do bloco android { viewBinding = true }
    - [ ] Criando um arquivo .txt chamado binding
    - [ ] O Android Studio já habilita sozinho em todos os projetos antigos
    *Explicação: É uma configuração de nível de módulo que gera as classes de binding automaticamente.*

9. O que é o `Material Design`?
    - [ ] Um curso de desenho clássico
    - [x] O sistema de design criado pela Google para unificar a visual das interfaces
    - [ ] O nome do vidro protetor da tela do celular
    - [ ] Uma marca de roupas para programadores
    *Explicação: Ele fornece diretrizes estéticas e componentes prontos (cards, botões flutuantes, etc) para o Android.*

10. Qual a função de um `FrameLayout`?
    - [ ] Organizar itens em uma grade (grid)
    - [x] Bloquear uma área da tela para exibir um item de cada vez ou sobrepostos
    - [ ] Fazer a moldura do celular
    - [ ] Impedir que o usuário clique fora do app
    *Explicação: É o layout mais simples, ideal para quando você quer empilhar Views ou usar Fragmentos.*