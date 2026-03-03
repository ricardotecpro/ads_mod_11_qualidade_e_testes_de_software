# Quiz 11 - Threads e Coroutines 🧵

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que é a "Main Thread" (ou UI Thread) no Android?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Quase tudo que é visual acontece na Main Thread, que deve estar sempre livre para não travar.">Uma thread que fica baixando arquivos em background.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Quase tudo que é visual acontece na Main Thread, que deve estar sempre livre para não travar.">A thread principal responsável por desenhar a interface e processar toques do usuário.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Quase tudo que é visual acontece na Main Thread, que deve estar sempre livre para não travar.">A conexão de internet do celular.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Quase tudo que é visual acontece na Main Thread, que deve estar sempre livre para não travar.">O carregador de bateria.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. O que causa o erro "ANR" (Application Not Responding)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Se a Main Thread for bloqueada por mais de ~5 segundos, o Android mata o app para proteger o sistema.">Falta de espaço em disco.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Se a Main Thread for bloqueada por mais de ~5 segundos, o Android mata o app para proteger o sistema.">Bloquear a Main Thread por muito tempo (ex: fazendo uma operação pesada ou download).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Se a Main Thread for bloqueada por mais de ~5 segundos, o Android mata o app para proteger o sistema.">O usuário esqueceu de carregar o celular.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Se a Main Thread for bloqueada por mais de ~5 segundos, o Android mata o app para proteger o sistema.">Usar muitas cores no layout.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. O que são Kotlin Coroutines?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Coroutines são muito leves (podem rodar milhares ao mesmo tempo) e facilitam o código assíncrono.">Um novo tipo de tela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Coroutines são muito leves (podem rodar milhares ao mesmo tempo) e facilitam o código assíncrono.">Uma linguagem de banco de dados.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Coroutines são muito leves (podem rodar milhares ao mesmo tempo) e facilitam o código assíncrono.">Mecanismos de concorrência leve que permitem escrever código assíncrono de forma sequencial.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Coroutines são muito leves (podem rodar milhares ao mesmo tempo) e facilitam o código assíncrono.">Pequenos robôs que consertam o código.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual a função da palavra-chave `suspend` em Kotlin?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Funções suspend são o coração das Coroutines.">Deletar a função da memória.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Funções suspend são o coração das Coroutines.">Indicar que a função pode ser pausada e continuada depois sem bloquear a thread atual.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Funções suspend são o coração das Coroutines.">Tornar a função invisível para outras classes.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Funções suspend são o coração das Coroutines.">Faz com que a função rode apenas em feriados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Para que serve o `Dispatcher.IO` no Kotlin?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Dispatcher.IO usa um conjunto de threads otimizadas para espera de rede ou disco.">Para atualizar a barra de progresso na tela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Dispatcher.IO usa um conjunto de threads otimizadas para espera de rede ou disco.">Para fazer cálculos matemáticos intensos (CPU).</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Dispatcher.IO usa um conjunto de threads otimizadas para espera de rede ou disco.">Para realizar operações de entrada/saída (Rede, Banco de Dados, Arquivos).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Dispatcher.IO usa um conjunto de threads otimizadas para espera de rede ou disco.">Para tocar músicas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual Dispatcher deve ser usado OBRIGATORIAMENTE para atualizar um componente visual (ex: `txtNome.text = "João"`)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Apenas a Main Thread tem permissão para alterar a interface gráfica no Android.">Dispatchers.IO</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Apenas a Main Thread tem permissão para alterar a interface gráfica no Android.">Dispatchers.Default</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Apenas a Main Thread tem permissão para alterar a interface gráfica no Android.">Dispatchers.Main</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Apenas a Main Thread tem permissão para alterar a interface gráfica no Android.">Dispatchers.Unconfined</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. O que é o `viewModelScope`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Usar viewModelScope garante que downloads sejam cancelados se o usuário sair da tela, evitando vazamentos e crashes.">Um telescópio para ver o código.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Usar viewModelScope garante que downloads sejam cancelados se o usuário sair da tela, evitando vazamentos e crashes.">Um escopo de coroutine ligado ao ciclo de vida do ViewModel; limpa tudo automaticamente quando o ViewModel morre.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Usar viewModelScope garante que downloads sejam cancelados se o usuário sair da tela, evitando vazamentos e crashes.">O banco de dados do Google.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Usar viewModelScope garante que downloads sejam cancelados se o usuário sair da tela, evitando vazamentos e crashes.">Uma variável global para todo o app.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que caracteriza uma comunicação via "Socket" (TCP) em relação ao REST?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Diferente do REST (pergunta/resposta), o Socket deixa um canal aberto para ambos os lados falarem a qualquer momento.">É mais lenta.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Diferente do REST (pergunta/resposta), o Socket deixa um canal aberto para ambos os lados falarem a qualquer momento.">É uma conexão bidirecional persistente (Full-Duplex), ideal para chats ou jogos em tempo real.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Diferente do REST (pergunta/resposta), o Socket deixa um canal aberto para ambos os lados falarem a qualquer momento.">Só funciona com Bluetooth.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Diferente do REST (pergunta/resposta), o Socket deixa um canal aberto para ambos os lados falarem a qualquer momento.">É um formato de imagem.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. No iOS moderno, qual o conceito equivalente às Kotlin Coroutines para lidar com assincronismo?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Swift recentemente adotou uma sintaxe de Async/Await muito parecida com as Coroutines do Kotlin.">GCD (Grand Central Dispatch)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Swift recentemente adotou uma sintaxe de Async/Await muito parecida com as Coroutines do Kotlin.">OperationQueues</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Swift recentemente adotou uma sintaxe de Async/Await muito parecida com as Coroutines do Kotlin.">Async / Await</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Swift recentemente adotou uma sintaxe de Async/Await muito parecida com as Coroutines do Kotlin.">Closures</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. O que faz a função `withContext()` dentro de uma Coroutine?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. withContext é essencial para orquestrar em qual thread cada pedaço do código deve rodar.">Fecha o aplicativo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! withContext é essencial para orquestrar em qual thread cada pedaço do código deve rodar.">Permite trocar temporariamente de Thread (ex: sair da Main e ir para IO) e voltar após terminar.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. withContext é essencial para orquestrar em qual thread cada pedaço do código deve rodar.">Salva o estado do celular.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. withContext é essencial para orquestrar em qual thread cada pedaço do código deve rodar.">Muda o idioma do app.</div>
  <div class="quiz-feedback"></div>
</div>
