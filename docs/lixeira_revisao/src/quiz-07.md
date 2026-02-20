# Quiz 07 - Arquitetura MVVM 🏗️

1. O que significa a sigla MVVM?
    - [ ] Mobile View Variable Model
    - [x] Model - View - ViewModel
    - [ ] Master View Visual Machine
    - [ ] Multiple View Version Method
    *Explicação: MVVM é o padrão de arquitetura recomendado pelo Google para apps Android modernos.*

2. Na arquitetura MVVM, qual é a responsabilidade da camada VIEW?
    - [ ] Realizar cálculos matemáticos complexos.
    - [ ] Salvar dados no banco de dados.
    - [x] Apenas exibir a interface e reagir a eventos do usuário (toques), sem lógica de negócio.
    - [ ] Gerenciar a conexão de rede.
    *Explicação: A View deve ser "burra" e apenas refletir o estado enviado pelo ViewModel.*

3. Qual componente é responsável por sobreviver a mudanças de configuração (como girar a tela) e guardar os dados da UI?
    - [ ] Activity
    - [ ] Intent
    - [x] ViewModel
    - [ ] Fragment
    *Explicação: O ViewModel foi criado para ter um ciclo de vida mais longo que a Activity, retendo dados durante recriações.*

4. O que é o "LiveData"?
    - [ ] Um serviço de streaming do Android.
    - [ ] Um tipo de bateria de longa duração.
    - [x] Um container de dados observável que respeita o ciclo de vida da Activity/Fragment.
    - [ ] O banco de dados em tempo real do Google.
    *Explicação: O LiveData avisa a View quando um dado muda, mas só se a View estiver ativa.*

5. Qual a vantagem de uma Activity "Observar" (observe) um dado no ViewModel em vez de pedir o dado manualmente?
    - [ ] Gasta menos internet.
    - [x] Garante que a UI esteja sempre sincronizada com os dados reais automaticamente.
    - [ ] Aumenta a velocidade do processador.
    - [ ] Deleta o cache do app.
    *Explicação: O padrão Observer garante que sempre que o dado mudar no ViewModel, a tela se atualize sozinha.*

6. Onde deve ficar a lógica de busca de dados (seja de uma API ou Banco)?
    - [ ] No método onCreate da Activity.
    - [x] No Model (frequentemente gerenciado por um Repository).
    - [ ] Dentro do arquivo XML de layout.
    - [ ] No arquivo AndroidManifest.
    *Explicação: Separação de conceitos: dados ficam no Model, lógica de UI no ViewModel, e exibição na View.*

7. Por que a arquitetura MVVM facilita a escrita de "Testes Unitários"?
    - [ ] Porque você não precisa testar nada.
    - [ ] Porque o Kotlin testa o código sozinho.
    - [x] Porque a lógica está isolada no ViewModel, que não depende de componentes visuais do Android para rodar.
    - [ ] Porque o projeto fica com menos arquivos.
    *Explicação: Podemos testar o ViewModel em um computador simples, sem precisar de um celular/emulador ligado.*

8. O que acontece com o ViewModel quando a Activity que o criou é destruída definitivamente (ex: usuário apertou voltar)?
    - [ ] Ele fica na memória para sempre.
    - [x] Ele também é destruído (limpo) para liberar memória.
    - [ ] Ele se move para outro aplicativo.
    - [ ] Ele reinicia o celular.
    *Explicação: O ViewModel morre quando sua View associada morre definitivamente (não por rotação).*

9. Como o ViewModel se comunica de volta com a Activity no MVVM?
    - [ ] Chamando `activity.updateUI()`.
    - [ ] Usando uma Intent.
    - [x] Através de LiveData ou StateFlow (Fluxo de dados observável).
    - [ ] Enviando um e-mail.
    *Explicação: O ViewModel nunca deve ter uma referência direta para a Activity, evitando vazamentos de memória.*

10. No iOS moderno (SwiftUI), qual é o conceito que mais se assemelha ao ViewModel operando com LiveData?
    - [ ] Structs
    - [ ] @IBAction
    - [x] @ObservableObject ou @StateObject
    - [ ] Core Graphics
    *Explicação: O SwiftUI usa o padrão de reatividade onde a View se redesenha automaticamente quando um estado observado muda.*
