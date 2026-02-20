# Quiz 11 - Threads e Assincronismo 🧵

1. O que é a `Main Thread` (Thread Principal) no Android?
    - [ ] A thread que roda o GPS em segundo plano
    - [x] A thread responsável por desenhar a interface e reagir aos toques do usuário
    - [ ] O cabo principal que conecta o celular ao PC
    - [ ] O nome do processador principal do celular
    *Explicação: Tudo que é visual acontece nela. Se ela travar, o app congela.*

2. O que acontece se você rodar um loop infinito ou um download pesado na Main Thread?
    - [ ] O download termina mais rápido
    - [x] Ocorre o erro ANR (Application Not Responding) e o Android sugere fechar o app
    - [ ] O celular economiza bateria
    - [ ] As cores da tela mudam para vermelho
    *Explicação: Bloquear a thread principal impede o Android de redesenhar a tela (60 vezes por segundo).*

3. O que são Kotlin `Coroutines`?
    - [ ] Rotinas de academia para programadores
    - [x] Uma forma simplificada de escrever código assíncrono que parece sequencial
    - [ ] Um tipo de lista que se auto-deleta
    - [ ] O nome das cores do Material Design
    *Explicação: Coroutines permitem "pausar" uma função sem bloquear a linha de execução da tarefa.*

4. Qual a função de uma `suspend fun`?
    - [ ] Suspender o usuário por comportamento inadequado
    - [x] Indicar que a função pode ser pausada e executada de forma assíncrona
    - [ ] Deletar o código após a execução
    - [ ] Bloquear a memória RAM por tempo indeterminado
    *Explicação: Funções suspensas só podem ser chamadas de dentro de uma coroutine ou outra função suspensa.*

5. Qual `Dispatcher` deve ser usado para operações de entrada e saída (Rede, Banco de Dados)?
    - [ ] Dispatchers.Main
    - [x] Dispatchers.IO
    - [ ] Dispatchers.Default
    - [ ] Dispatchers.Unconfined
    *Explicação: O Dispatcher.IO é otimizado para tarefas que ficam "esperando" por respostas externas.*

6. Quando usamos o `Dispatchers.Main`?
    - [ ] Para salvar arquivos grandes no disco
    - [x] Para atualizar componentes visuais (TextView, Button) com o resultado de uma tarefa
    - [ ] Para minerar criptomoedas
    - [ ] Para baixar músicas
    *Explicação: Apenas o Dispatcher.Main tem permissão para alterar a interface do usuário.*

7. O que o comando `delay(1000)` faz de diferente de `Thread.sleep(1000)`?
    - [ ] Nada, são exatamente iguais
    - [x] delay suspende a coroutine sem travar a thread; sleep bloqueia a thread inteira
    - [ ] delay funciona apenas em segundos e sleep em milissegundos
    - [ ] delay apaga a memória temporária
    *Explicação: Usar delay permite que outras tarefas continuem rodando na mesma thread enquanto você "espera".*

8. O que acontece com a coroutine iniciada em `viewModelScope` quando o usuário sai da tela?
    - [ ] Ela continua rodando para sempre
    - [x] Ela é cancelada automaticamente, evitando vazamento de memória e crashes
    - [ ] Ela envia um e-mail de despedida para o servidor
    - [ ] Ela apaga os dados salvos
    *Explicação: O escopo vinculado ao ciclo de vida garante que tarefas inúteis sejam interrompidas quando a View morre.*

9. Qual o equivalente no Swift (iOS moderno) às Coroutines do Kotlin?
    - [ ] GCD (Grand Central Dispatch)
    - [x] Async / Await
    - [ ] Objective-C
    - [ ] CoreData
    *Explicação: O modelo de async/await do Swift é quase idêntico ao funcionamento das coroutines.*

10. O que é uma `Race Condition` (Condição de Corrida)?
    - [ ] Uma competição de quem programa mais rápido
    - [x] Quando duas tarefas tentam acessar/mudar o mesmo dado ao mesmo tempo, causando resultados errados
    - [ ] O nome do game engine do Android
    - [ ] Quando o Wi-Fi e o 4G disputam quem é mais rápido
    *Explicação: É um bug clássico de concorrência que exige técnicas de sincronização para ser resolvido.*