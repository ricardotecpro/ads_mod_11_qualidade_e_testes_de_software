# Quiz 05 - Interface Gráfica (UI) 🎨

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual a diferença fundamental entre uma View e um ViewGroup?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. ViewGroups (como LinearLayout e ConstraintLayout) servem para posicionar as Views na tela.">Uma View organiza o layout e um ViewGroup exibe o conteúdo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! ViewGroups (como LinearLayout e ConstraintLayout) servem para posicionar as Views na tela.">Uma View é um componente visual individual (botão, texto) e um ViewGroup é um container que organiza as Views.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. ViewGroups (como LinearLayout e ConstraintLayout) servem para posicionar as Views na tela.">Não há diferença, são sinônimos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. ViewGroups (como LinearLayout e ConstraintLayout) servem para posicionar as Views na tela.">ViewGroups só existem no iOS.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual unidade de medida deve ser usada para definir o tamanho de botões e margens no Android?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. dp escala automaticamente de acordo com a densidade de pixels da tela do dispositivo.">px (pixels)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. dp escala automaticamente de acordo com a densidade de pixels da tela do dispositivo.">pt (pontos)</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! dp escala automaticamente de acordo com a densidade de pixels da tela do dispositivo.">dp (density-independent pixels)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. dp escala automaticamente de acordo com a densidade de pixels da tela do dispositivo.">sp (scale-independent pixels)</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual unidade de medida é recomendada especificamente para o tamanho de textos (fontes)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. sp respeita as configurações de acessibilidade do usuário, aumentando se o usuário escolher letras grandes no sistema.">dp</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. sp respeita as configurações de acessibilidade do usuário, aumentando se o usuário escolher letras grandes no sistema.">px</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! sp respeita as configurações de acessibilidade do usuário, aumentando se o usuário escolher letras grandes no sistema.">sp</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. sp respeita as configurações de acessibilidade do usuário, aumentando se o usuário escolher letras grandes no sistema.">mm</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual Layout organiza seus filhos em uma única linha ou coluna?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O LinearLayout é linear, ou seja, segue uma única direção (horizontal ou vertical).">ConstraintLayout</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O LinearLayout é linear, ou seja, segue uma única direção (horizontal ou vertical).">FrameLayout</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O LinearLayout é linear, ou seja, segue uma única direção (horizontal ou vertical).">LinearLayout</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O LinearLayout é linear, ou seja, segue uma única direção (horizontal ou vertical).">RelativeLayout</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual a principal vantagem do ConstraintLayout em relação aos outros layouts?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ConstraintLayout reduz o aninhamento de telas, o que torna a renderização mais rápida.">É o layout mais antigo e compatível.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O ConstraintLayout reduz o aninhamento de telas, o que torna a renderização mais rápida.">Permite criar layouts complexos de forma plana, sem aninhar muitos ViewGroups, melhorando a performance.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ConstraintLayout reduz o aninhamento de telas, o que torna a renderização mais rápida.">Só funciona com imagens 3D.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ConstraintLayout reduz o aninhamento de telas, o que torna a renderização mais rápida.">Ele obriga o uso de Java em vez de Kotlin.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. No Android Studio, o que representa a aba "Split" ao editar um arquivo XML?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É o modo ideal para desenvolvedores, permitindo ver o resultado visual imediato das mudanças no código.">Divide a tela do computador em duas.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! É o modo ideal para desenvolvedores, permitindo ver o resultado visual imediato das mudanças no código.">Mostra o código XML de um lado e o preview visual do outro.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É o modo ideal para desenvolvedores, permitindo ver o resultado visual imediato das mudanças no código.">Separa o código Kotlin do XML.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É o modo ideal para desenvolvedores, permitindo ver o resultado visual imediato das mudanças no código.">Finaliza o processo de compilação.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. O atributo `android:layout_width="match_parent"` faz com que o componente:</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. match_parent diz ao componente para esticar até os limites do container onde ele está.">Tenha o tamanho exato do seu conteúdo interno.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! match_parent diz ao componente para esticar até os limites do container onde ele está.">Ocupe toda a largura disponível do seu componente pai (parent).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. match_parent diz ao componente para esticar até os limites do container onde ele está.">Tenha exatamente 100 pixels de largura.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. match_parent diz ao componente para esticar até os limites do container onde ele está.">Desapareça da tela.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual componente usamos para permitir que o usuário digite um texto (Input)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Diferente do TextView (exibição), o EditText permite a interação de escrita.">TextView</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Diferente do TextView (exibição), o EditText permite a interação de escrita.">EditText (ou TextInputEditText)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Diferente do TextView (exibição), o EditText permite a interação de escrita.">Button</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Diferente do TextView (exibição), o EditText permite a interação de escrita.">ImageButton</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Para que serve o atributo `android:hint` em um EditText?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O hint (dica) ajuda o usuário a entender o que ele deve digitar naquele campo.">É a senha secreta do campo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O hint (dica) ajuda o usuário a entender o que ele deve digitar naquele campo.">Define a cor do fundo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O hint (dica) ajuda o usuário a entender o que ele deve digitar naquele campo.">Exibe um texto de ajuda ou exemplo dentro do campo enquanto ele está vazio.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O hint (dica) ajuda o usuário a entender o que ele deve digitar naquele campo.">Define o limite máximo de caracteres.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. No iOS, qual tecnologia de layout é mais parecida com o ConstraintLayout do Android?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Tanto o ConstraintLayout quanto o Auto Layout baseiam-se em regras de posicionamento relativo entre os elementos.">SwiftUI</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Tanto o ConstraintLayout quanto o Auto Layout baseiam-se em regras de posicionamento relativo entre os elementos.">Objective-C</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Tanto o ConstraintLayout quanto o Auto Layout baseiam-se em regras de posicionamento relativo entre os elementos.">Auto Layout</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Tanto o ConstraintLayout quanto o Auto Layout baseiam-se em regras de posicionamento relativo entre os elementos.">Core Graphics</div>
  <div class="quiz-feedback"></div>
</div>
