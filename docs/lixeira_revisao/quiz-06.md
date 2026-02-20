# Quiz 06 - Navegação e Intents 🗺️

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. No Android, o que é uma "Intent"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Intents (Intenções) são os mensageiros que iniciam Activities, abrem câmeras, etc.">É o plano de marketing do aplicativo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Intents (Intenções) são os mensageiros que iniciam Activities, abrem câmeras, etc.">É um objeto de mensagem usado para solicitar uma ação de outro componente do app ou do sistema.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Intents (Intenções) são os mensageiros que iniciam Activities, abrem câmeras, etc.">É um tipo de variável que guarda números decimais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Intents (Intenções) são os mensageiros que iniciam Activities, abrem câmeras, etc.">É o comando para deletar o aplicativo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual a diferença entre uma Intent Explícita e uma Implícita?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Usamos explícitas para navegar dentro do próprio app e implícitas para interagir com outros apps.">A explícita é para iOS e a implícita para Android.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Usamos explícitas para navegar dentro do próprio app e implícitas para interagir com outros apps.">A explícita abre o navegador e a implícita abre uma tela interna.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Usamos explícitas para navegar dentro do próprio app e implícitas para interagir com outros apps.">A explícita define exatamente qual classe rodar; a implícita apenas declara a ação (ex: "abrir site").</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Usamos explícitas para navegar dentro do próprio app e implícitas para interagir com outros apps.">Não há diferença técnica.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Como passamos um dado do tipo Texto (String) para a próxima tela?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O método `putExtra` permite adicionar diversos tipos de dados ao "pacote" da intent.">intent.send("TEXTO")</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O método `putExtra` permite adicionar diversos tipos de dados ao "pacote" da intent.">intent.addExtra("CHAVE", "VALOR")</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O método `putExtra` permite adicionar diversos tipos de dados ao "pacote" da intent.">intent.putExtra("CHAVE", "VALOR")</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O método `putExtra` permite adicionar diversos tipos de dados ao "pacote" da intent.">intent.saveData("VALOR")</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual comando é usado para efetivamente iniciar a nova tela após configurar a Intent?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `startActivity` é o método padrão da classe Context/Activity para navegação.">go()</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `startActivity` é o método padrão da classe Context/Activity para navegação.">openActivity(intent)</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! `startActivity` é o método padrão da classe Context/Activity para navegação.">startActivity(intent)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `startActivity` é o método padrão da classe Context/Activity para navegação.">run(intent)</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que acontece com a Activity atual quando chamamos o método `finish()`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `finish()` encerra o ciclo de vida da Activity atual.">Ela fica em segundo plano para sempre.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `finish()` encerra o ciclo de vida da Activity atual.">Ela é reiniciada.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! `finish()` encerra o ciclo de vida da Activity atual.">Ela é destruída e removida da "Pilha de Voltar" (Back Stack).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. `finish()` encerra o ciclo de vida da Activity atual.">O celular desliga.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Como recuperamos um dado do tipo Inteiro que foi passado via Intent?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Para tipos primitivos, o Android exige um valor padrão caso a chave não seja encontrada.">intent.getInt("CHAVE")</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Para tipos primitivos, o Android exige um valor padrão caso a chave não seja encontrada.">intent.getIntExtra("CHAVE", valorPadrao)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Para tipos primitivos, o Android exige um valor padrão caso a chave não seja encontrada.">intent.extraValue("CHAVE")</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Para tipos primitivos, o Android exige um valor padrão caso a chave não seja encontrada.">intent.loadInt("CHAVE")</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Imagine que você está na Tela A, abriu a Tela B e depois a Tela C. Se o usuário apertar o botão "Voltar" do celular na Tela C, o que acontece por padrão?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Android mantém uma pilha (LIFO - Last In, First Out) de navegação.">O app fecha totalmente.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Android mantém uma pilha (LIFO - Last In, First Out) de navegação.">Ele volta para a Tela A.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Android mantém uma pilha (LIFO - Last In, First Out) de navegação.">Ele volta para a Tela B.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Android mantém uma pilha (LIFO - Last In, First Out) de navegação.">Ele abre o menu do Google.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual Intent Implícita seria usada para abrir o navegador em um site específico?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. ACTION_VIEW indica que queremos visualizar um conteúdo (URI).">Intent.ACTION_CALL</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. ACTION_VIEW indica que queremos visualizar um conteúdo (URI).">Intent.ACTION_SEND</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! ACTION_VIEW indica que queremos visualizar um conteúdo (URI).">Intent.ACTION_VIEW</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. ACTION_VIEW indica que queremos visualizar um conteúdo (URI).">Intent.ACTION_NAVIGATE</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Por que é importante chamar `finish()` após navegar da tela de Login para a Home?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Gerenciar a pilha de navegação é crucial para uma boa experiência de usuário (UX).">Para economizar bateria.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Gerenciar a pilha de navegação é crucial para uma boa experiência de usuário (UX).">Para evitar que o usuário volte para a tela de Login ao apertar o botão "Voltar" após já estar logado.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Gerenciar a pilha de navegação é crucial para uma boa experiência de usuário (UX).">Porque o Android só permite uma Activity aberta por vez.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Gerenciar a pilha de navegação é crucial para uma boa experiência de usuário (UX).">Para apagar os dados do usuário.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. No iOS, qual é o conceito equivalente às Intents para navegação entre ViewControllers?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No iOS clássico, usamos Segues para definir transições entre telas no Storyboard.">Protocols</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No iOS clássico, usamos Segues para definir transições entre telas no Storyboard.">Delegates</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! No iOS clássico, usamos Segues para definir transições entre telas no Storyboard.">Segues (ou Navigation Push)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No iOS clássico, usamos Segues para definir transições entre telas no Storyboard.">Core Data</div>
  <div class="quiz-feedback"></div>
</div>
