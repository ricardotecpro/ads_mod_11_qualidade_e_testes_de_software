# Quiz 07 - Arquitetura MVVM 🏗️

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que significa a sigla MVVM?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. MVVM é o padrão de arquitetura recomendado pelo Google para apps Android modernos.">Mobile View Variable Model</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! MVVM é o padrão de arquitetura recomendado pelo Google para apps Android modernos.">Model - View - ViewModel</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. MVVM é o padrão de arquitetura recomendado pelo Google para apps Android modernos.">Master View Visual Machine</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. MVVM é o padrão de arquitetura recomendado pelo Google para apps Android modernos.">Multiple View Version Method</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Na arquitetura MVVM, qual é a responsabilidade da camada VIEW?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A View deve ser "burra" e apenas refletir o estado enviado pelo ViewModel.">Realizar cálculos matemáticos complexos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A View deve ser "burra" e apenas refletir o estado enviado pelo ViewModel.">Salvar dados no banco de dados.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A View deve ser "burra" e apenas refletir o estado enviado pelo ViewModel.">Apenas exibir a interface e reagir a eventos do usuário (toques), sem lógica de negócio.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A View deve ser "burra" e apenas refletir o estado enviado pelo ViewModel.">Gerenciar a conexão de rede.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual componente é responsável por sobreviver a mudanças de configuração (como girar a tela) e guardar os dados da UI?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewModel foi criado para ter um ciclo de vida mais longo que a Activity, retendo dados durante recriações.">Activity</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewModel foi criado para ter um ciclo de vida mais longo que a Activity, retendo dados durante recriações.">Intent</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O ViewModel foi criado para ter um ciclo de vida mais longo que a Activity, retendo dados durante recriações.">ViewModel</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewModel foi criado para ter um ciclo de vida mais longo que a Activity, retendo dados durante recriações.">Fragment</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O que é o "LiveData"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O LiveData avisa a View quando um dado muda, mas só se a View estiver ativa.">Um serviço de streaming do Android.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O LiveData avisa a View quando um dado muda, mas só se a View estiver ativa.">Um tipo de bateria de longa duração.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O LiveData avisa a View quando um dado muda, mas só se a View estiver ativa.">Um container de dados observável que respeita o ciclo de vida da Activity/Fragment.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O LiveData avisa a View quando um dado muda, mas só se a View estiver ativa.">O banco de dados em tempo real do Google.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual a vantagem de uma Activity "Observar" (observe) um dado no ViewModel em vez de pedir o dado manualmente?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O padrão Observer garante que sempre que o dado mudar no ViewModel, a tela se atualize sozinha.">Gasta menos internet.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O padrão Observer garante que sempre que o dado mudar no ViewModel, a tela se atualize sozinha.">Garante que a UI esteja sempre sincronizada com os dados reais automaticamente.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O padrão Observer garante que sempre que o dado mudar no ViewModel, a tela se atualize sozinha.">Aumenta a velocidade do processador.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O padrão Observer garante que sempre que o dado mudar no ViewModel, a tela se atualize sozinha.">Deleta o cache do app.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Onde deve ficar a lógica de busca de dados (seja de uma API ou Banco)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Separação de conceitos: dados ficam no Model, lógica de UI no ViewModel, e exibição na View.">No método onCreate da Activity.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Separação de conceitos: dados ficam no Model, lógica de UI no ViewModel, e exibição na View.">No Model (frequentemente gerenciado por um Repository).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Separação de conceitos: dados ficam no Model, lógica de UI no ViewModel, e exibição na View.">Dentro do arquivo XML de layout.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Separação de conceitos: dados ficam no Model, lógica de UI no ViewModel, e exibição na View.">No arquivo AndroidManifest.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Por que a arquitetura MVVM facilita a escrita de "Testes Unitários"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Podemos testar o ViewModel em um computador simples, sem precisar de um celular/emulador ligado.">Porque você não precisa testar nada.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Podemos testar o ViewModel em um computador simples, sem precisar de um celular/emulador ligado.">Porque o Kotlin testa o código sozinho.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Podemos testar o ViewModel em um computador simples, sem precisar de um celular/emulador ligado.">Porque a lógica está isolada no ViewModel, que não depende de componentes visuais do Android para rodar.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Podemos testar o ViewModel em um computador simples, sem precisar de um celular/emulador ligado.">Porque o projeto fica com menos arquivos.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que acontece com o ViewModel quando a Activity que o criou é destruída definitivamente (ex: usuário apertou voltar)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewModel morre quando sua View associada morre definitivamente (não por rotação).">Ele fica na memória para sempre.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O ViewModel morre quando sua View associada morre definitivamente (não por rotação).">Ele também é destruído (limpo) para liberar memória.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewModel morre quando sua View associada morre definitivamente (não por rotação).">Ele se move para outro aplicativo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewModel morre quando sua View associada morre definitivamente (não por rotação).">Ele reinicia o celular.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Como o ViewModel se comunica de volta com a Activity no MVVM?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewModel nunca deve ter uma referência direta para a Activity, evitando vazamentos de memória.">Chamando `activity.updateUI()`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewModel nunca deve ter uma referência direta para a Activity, evitando vazamentos de memória.">Usando uma Intent.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O ViewModel nunca deve ter uma referência direta para a Activity, evitando vazamentos de memória.">Através de LiveData ou StateFlow (Fluxo de dados observável).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewModel nunca deve ter uma referência direta para a Activity, evitando vazamentos de memória.">Enviando um e-mail.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. No iOS moderno (SwiftUI), qual é o conceito que mais se assemelha ao ViewModel operando com LiveData?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O SwiftUI usa o padrão de reatividade onde a View se redesenha automaticamente quando um estado observado muda.">Structs</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O SwiftUI usa o padrão de reatividade onde a View se redesenha automaticamente quando um estado observado muda.">@IBAction</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O SwiftUI usa o padrão de reatividade onde a View se redesenha automaticamente quando um estado observado muda.">@ObservableObject ou @StateObject</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O SwiftUI usa o padrão de reatividade onde a View se redesenha automaticamente quando um estado observado muda.">Core Graphics</div>
  <div class="quiz-feedback"></div>
</div>
