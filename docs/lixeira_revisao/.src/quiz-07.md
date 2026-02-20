# Quiz 07 - Arquitetura Moderna (MVVM) 🏗️

1. O que significa a sigla MVVM?
    - [ ] Multi-View Variable Management
    - [x] Model-View-ViewModel
    - [ ] Mobile-Value-Verification-Mode
    - [ ] Main-View-Variable-Model
    *Explicação: É o padrão de arquitetura recomendado pelo Google para separar lógica, dados e interface.*

2. No MVVM, qual a principal função da `View` (Activity/Fragment)?
    - [ ] Calcular fórmulas matemáticas complexas
    - [ ] Salvar dados no banco de dados
    - [x] Apenas exibir dados na tela e reagir às interações do usuário (cliques)
    - [ ] Gerenciar a conexão com a internet
    *Explicação: A View deve ser o mais "burra" possível, focando apenas no visual.*

3. Por que o `ViewModel` é importante para lidar com a rotação de tela?
    - [ ] Porque ele impede que a tela gire
    - [x] Porque ele sobrevive à destruição da Activity e mantém os dados na memória
    - [ ] Porque ele redesenha os botões mais rápido
    - [ ] Porque ele economiza bateria durante a rotação
    *Explicação: Diferente da Activity, o ViewModel não é reiniciado quando a orientação do celular muda.*

4. O que é o `LiveData`?
    - [ ] Um tipo de jogo online
    - [ ] Um banco de dados em tempo real da Google
    - [x] Um container de dados observável que respeita o ciclo de vida da View
    - [ ] Uma tag XML para exibir vídeos
    *Explicação: LiveData permite que a View saiba quando um dado mudou sem precisar perguntar toda hora.*

5. Qual o problema da abordagem "God Activity" (Activity que faz tudo)?
    - [ ] O app fica muito bonito
    - [x] O código fica difícil de manter, testar e propenso a bugs de memória
    - [ ] O Google Play não permite apps assim
    - [ ] O celular esquenta menos
    *Explicação: Concentrar todas as responsabilidades em um único arquivo torna o projeto um caos a longo prazo.*

6. O que significa "Observar" um dado (Observer Pattern)?
    - [ ] Ficar olhando para a tela esperando o app abrir
    - [x] Registrar uma função que será executada automaticamente sempre que o dado mudar
    - [ ] Hackear os dados de outros usuários
    - [ ] Tirar um print da tela
    *Explicação: A View "assina" o LiveData e é notificada toda vez que há uma atualização.*

7. Quem deve conter a lógica de negócio (ex: validar se uma senha é forte)?
    - [ ] O XML do Layout
    - [ ] O AndroidManifest
    - [x] O ViewModel (ou camadas abaixo dele como UseCases)
    - [ ] O botão de clique
    *Explicação: Lógicas de decisão devem ficar fora da Activity para serem testáveis e reutilizáveis.*

8. O que o método `MutableLiveData.setValue()` (ou `.value =`) faz?
    - [ ] Apaga o valor atual
    - [x] Atualiza o valor e notifica todos os observadores ativos
    - [ ] Bloqueia o acesso ao dado
    - [ ] Reinicia o ViewModel
    *Explicação: É através dessa alteração que a mágica da UI reativa acontece.*

9. Por que não devemos passar uma `Activity` como referência para dentro do `ViewModel`?
    - [ ] Porque o Java não permite
    - [x] Para evitar vazamento de memória (Memory Leak), já que o ViewModel vive mais que a Activity
    - [ ] Porque o código fica muito curto
    - [ ] Porque a Google cobra por cada referência passada
    *Explicação: Se o ViewModel segurar uma Activity que já foi destruída, o Android não consegue liberar essa memória.*

10. Qual a vantagem do MVVM para o trabalho em equipe?
    - [ ] Todos os programadores precisam mexer no mesmo arquivo
    - [x] Permite que designers mexam na View enquanto desenvolvedores trabalham no ViewModel/Model
    - [ ] O código fica em inglês automaticamente
    - [ ] Reduz o número de reuniões
    *Explicação: A clara separação de camadas permite que diferentes profissionais trabalhem em partes distintas sem conflitos.*