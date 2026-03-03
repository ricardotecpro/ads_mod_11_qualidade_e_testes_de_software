# Quiz 05 - Interface Gráfica (UI) 🎨

1. Qual a diferença fundamental entre uma View e um ViewGroup?
    - [ ] Uma View organiza o layout e um ViewGroup exibe o conteúdo.
    - [x] Uma View é um componente visual individual (botão, texto) e um ViewGroup é um container que organiza as Views.
    - [ ] Não há diferença, são sinônimos.
    - [ ] ViewGroups só existem no iOS.
    *Explicação: ViewGroups (como LinearLayout e ConstraintLayout) servem para posicionar as Views na tela.*

2. Qual unidade de medida deve ser usada para definir o tamanho de botões e margens no Android?
    - [ ] px (pixels)
    - [ ] pt (pontos)
    - [x] dp (density-independent pixels)
    - [ ] sp (scale-independent pixels)
    *Explicação: dp escala automaticamente de acordo com a densidade de pixels da tela do dispositivo.*

3. Qual unidade de medida é recomendada especificamente para o tamanho de textos (fontes)?
    - [ ] dp
    - [ ] px
    - [x] sp
    - [ ] mm
    *Explicação: sp respeita as configurações de acessibilidade do usuário, aumentando se o usuário escolher letras grandes no sistema.*

4. Qual Layout organiza seus filhos em uma única linha ou coluna?
    - [ ] ConstraintLayout
    - [ ] FrameLayout
    - [x] LinearLayout
    - [ ] RelativeLayout
    *Explicação: O LinearLayout é linear, ou seja, segue uma única direção (horizontal ou vertical).*

5. Qual a principal vantagem do ConstraintLayout em relação aos outros layouts?
    - [ ] É o layout mais antigo e compatível.
    - [x] Permite criar layouts complexos de forma plana, sem aninhar muitos ViewGroups, melhorando a performance.
    - [ ] Só funciona com imagens 3D.
    - [ ] Ele obriga o uso de Java em vez de Kotlin.
    *Explicação: O ConstraintLayout reduz o aninhamento de telas, o que torna a renderização mais rápida.*

6. No Android Studio, o que representa a aba "Split" ao editar um arquivo XML?
    - [ ] Divide a tela do computador em duas.
    - [x] Mostra o código XML de um lado e o preview visual do outro.
    - [ ] Separa o código Kotlin do XML.
    - [ ] Finaliza o processo de compilação.
    *Explicação: É o modo ideal para desenvolvedores, permitindo ver o resultado visual imediato das mudanças no código.*

7. O atributo `android:layout_width="match_parent"` faz com que o componente:
    - [ ] Tenha o tamanho exato do seu conteúdo interno.
    - [x] Ocupe toda a largura disponível do seu componente pai (parent).
    - [ ] Tenha exatamente 100 pixels de largura.
    - [ ] Desapareça da tela.
    *Explicação: match_parent diz ao componente para esticar até os limites do container onde ele está.*

8. Qual componente usamos para permitir que o usuário digite um texto (Input)?
    - [ ] TextView
    - [x] EditText (ou TextInputEditText)
    - [ ] Button
    - [ ] ImageButton
    *Explicação: Diferente do TextView (exibição), o EditText permite a interação de escrita.*

9. Para que serve o atributo `android:hint` em um EditText?
    - [ ] É a senha secreta do campo.
    - [ ] Define a cor do fundo.
    - [x] Exibe um texto de ajuda ou exemplo dentro do campo enquanto ele está vazio.
    - [ ] Define o limite máximo de caracteres.
    *Explicação: O hint (dica) ajuda o usuário a entender o que ele deve digitar naquele campo.*

10. No iOS, qual tecnologia de layout é mais parecida com o ConstraintLayout do Android?
    - [ ] SwiftUI
    - [ ] Objective-C
    - [x] Auto Layout
    - [ ] Core Graphics
    *Explicação: Tanto o ConstraintLayout quanto o Auto Layout baseiam-se em regras de posicionamento relativo entre os elementos.*
