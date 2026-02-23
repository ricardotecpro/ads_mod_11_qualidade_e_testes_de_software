# Quiz 11 - Threads e Coroutines 🧵

1. O que é a "Main Thread" (ou UI Thread) no Android?
    - [ ] Uma thread que fica baixando arquivos em background.
    - [x] A thread principal responsável por desenhar a interface e processar toques do usuário.
    - [ ] A conexão de internet do celular.
    - [ ] O carregador de bateria.
    *Explicação: Quase tudo que é visual acontece na Main Thread, que deve estar sempre livre para não travar.*

2. O que causa o erro "ANR" (Application Not Responding)?
    - [ ] Falta de espaço em disco.
    - [x] Bloquear a Main Thread por muito tempo (ex: fazendo uma operação pesada ou download).
    - [ ] O usuário esqueceu de carregar o celular.
    - [ ] Usar muitas cores no layout.
    *Explicação: Se a Main Thread for bloqueada por mais de ~5 segundos, o Android mata o app para proteger o sistema.*

3. O que são Kotlin Coroutines?
    - [ ] Um novo tipo de tela.
    - [ ] Uma linguagem de banco de dados.
    - [x] Mecanismos de concorrência leve que permitem escrever código assíncrono de forma sequencial.
    - [ ] Pequenos robôs que consertam o código.
    *Explicação: Coroutines são muito leves (podem rodar milhares ao mesmo tempo) e facilitam o código assíncrono.*

4. Qual a função da palavra-chave `suspend` em Kotlin?
    - [ ] Deletar a função da memória.
    - [x] Indicar que a função pode ser pausada e continuada depois sem bloquear a thread atual.
    - [ ] Tornar a função invisível para outras classes.
    - [ ] Faz com que a função rode apenas em feriados.
    *Explicação: Funções suspend são o coração das Coroutines.*

5. Para que serve o `Dispatcher.IO` no Kotlin?
    - [ ] Para atualizar a barra de progresso na tela.
    - [ ] Para fazer cálculos matemáticos intensos (CPU).
    - [x] Para realizar operações de entrada/saída (Rede, Banco de Dados, Arquivos).
    - [ ] Para tocar músicas.
    *Explicação: O Dispatcher.IO usa um conjunto de threads otimizadas para espera de rede ou disco.*

6. Qual Dispatcher deve ser usado OBRIGATORIAMENTE para atualizar um componente visual (ex: `txtNome.text = "João"`)?
    - [ ] Dispatchers.IO
    - [ ] Dispatchers.Default
    - [x] Dispatchers.Main
    - [ ] Dispatchers.Unconfined
    *Explicação: Apenas a Main Thread tem permissão para alterar a interface gráfica no Android.*

7. O que é o `viewModelScope`?
    - [ ] Um telescópio para ver o código.
    - [x] Um escopo de coroutine ligado ao ciclo de vida do ViewModel; limpa tudo automaticamente quando o ViewModel morre.
    - [ ] O banco de dados do Google.
    - [ ] Uma variável global para todo o app.
    *Explicação: Usar viewModelScope garante que downloads sejam cancelados se o usuário sair da tela, evitando vazamentos e crashes.*

8. O que caracteriza uma comunicação via "Socket" (TCP) em relação ao REST?
    - [ ] É mais lenta.
    - [x] É uma conexão bidirecional persistente (Full-Duplex), ideal para chats ou jogos em tempo real.
    - [ ] Só funciona com Bluetooth.
    - [ ] É um formato de imagem.
    *Explicação: Diferente do REST (pergunta/resposta), o Socket deixa um canal aberto para ambos os lados falarem a qualquer momento.*

9. No iOS moderno, qual o conceito equivalente às Kotlin Coroutines para lidar com assincronismo?
    - [ ] GCD (Grand Central Dispatch)
    - [ ] OperationQueues
    - [x] Async / Await
    - [ ] Closures
    *Explicação: O Swift recentemente adotou uma sintaxe de Async/Await muito parecida com as Coroutines do Kotlin.*

10. O que faz a função `withContext()` dentro de uma Coroutine?
    - [ ] Fecha o aplicativo.
    - [x] Permite trocar temporariamente de Thread (ex: sair da Main e ir para IO) e voltar após terminar.
    - [ ] Salva o estado do celular.
    - [ ] Muda o idioma do app.
    *Explicação: withContext é essencial para orquestrar em qual thread cada pedaço do código deve rodar.*
