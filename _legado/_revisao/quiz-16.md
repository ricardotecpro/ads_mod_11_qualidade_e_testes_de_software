# Quiz 16 - Revisão Geral e Próximos Passos 🎓

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual camada do MVVM é responsável por gerenciar o estado da tela e sobreviver à rotação do celular?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewModel retém os dados e a lógica de apresentação, sendo o "cérebro" resiliente da UI.">View</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewModel retém os dados e a lógica de apresentação, sendo o "cérebro" resiliente da UI.">Model</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O ViewModel retém os dados e a lógica de apresentação, sendo o "cérebro" resiliente da UI.">ViewModel</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewModel retém os dados e a lógica de apresentação, sendo o "cérebro" resiliente da UI.">Repository</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Para que serve o arquivo "AndroidManifest.xml"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Manifest é o arquivo de configuração central exigido pelo sistema Android.">Para escrever funções em Kotlin.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Manifest é o arquivo de configuração central exigido pelo sistema Android.">Para declarar componentes como Activities, permissões e metadados vitais do app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Manifest é o arquivo de configuração central exigido pelo sistema Android.">Para salvar o histórico do usuário.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Manifest é o arquivo de configuração central exigido pelo sistema Android.">Para compilar o código Java.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual a principal vantagem de usar "Kotlin Coroutines" em vez de Threads comuns?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Coroutines permitem gerenciar milhares de tarefas simultâneas sem sobrecarregar o hardware.">Elas são coloridas.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Coroutines permitem gerenciar milhares de tarefas simultâneas sem sobrecarregar o hardware.">Elas só funcionam no iOS.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Coroutines permitem gerenciar milhares de tarefas simultâneas sem sobrecarregar o hardware.">São extremamente leves (consomem pouca memória) e facilitam a leitura de código assíncrono.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Coroutines permitem gerenciar milhares de tarefas simultâneas sem sobrecarregar o hardware.">Elas impedem todos os bugs.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual o componente usado para exibir listas de alto desempenho no Android?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O RecyclerView é a evolução da ListView, focada em reaproveitamento de memória.">ScrollView</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O RecyclerView é a evolução da ListView, focada em reaproveitamento de memória.">LinearLayout</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O RecyclerView é a evolução da ListView, focada em reaproveitamento de memória.">RecyclerView</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O RecyclerView é a evolução da ListView, focada em reaproveitamento de memória.">ListView (antiga)</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que é o "Material Design 3"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O M3 traz o conceito de "Material You", permitindo que o app se adapte ao estilo do usuário.">Um tipo de bateria.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O M3 traz o conceito de "Material You", permitindo que o app se adapte ao estilo do usuário.">O sistema de design mais atual do Google, focado em personalização e cores dinâmicas.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O M3 traz o conceito de "Material You", permitindo que o app se adapte ao estilo do usuário.">Uma linguagem de programação.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O M3 traz o conceito de "Material You", permitindo que o app se adapte ao estilo do usuário.">Um serviço de nuvem.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual biblioteca usamos para transformar uma API de internet em código Kotlin facilmente?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Retrofit abstrai toda a parte complexa de conexões HTTP e conversão de JSON.">Room</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Retrofit abstrai toda a parte complexa de conexões HTTP e conversão de JSON.">Espresso</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Retrofit abstrai toda a parte complexa de conexões HTTP e conversão de JSON.">Retrofit</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Retrofit abstrai toda a parte complexa de conexões HTTP e conversão de JSON.">Gradle</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Por que devemos usar "Dependency Injection" (como Hilt ou Koin) em projetos grandes?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Injeção de dependência desacopla o código, tornando-o modular e profissional.">Para o app ficar mais pesado.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Injeção de dependência desacopla o código, tornando-o modular e profissional.">Para facilitar a manutenção, troca de componentes e a escrita de testes automatizados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Injeção de dependência desacopla o código, tornando-o modular e profissional.">Para o Google dar mais destaque na loja.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Injeção de dependência desacopla o código, tornando-o modular e profissional.">Não é necessário em nenhum caso.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que é o "Jetpack Compose"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Compose é o futuro do Android, mudando a forma como desenhamos telas para ser mais parecida com Swift UI.">Um tipo de avião do Google.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Compose é o futuro do Android, mudando a forma como desenhamos telas para ser mais parecida com Swift UI.">O novo Toolkit declarativo para criar interfaces Android (sem usar XML).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Compose é o futuro do Android, mudando a forma como desenhamos telas para ser mais parecida com Swift UI.">Um banco de dados para fotos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Compose é o futuro do Android, mudando a forma como desenhamos telas para ser mais parecida com Swift UI.">Uma ferramenta de edição de vídeo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual o objetivo principal de um "Portfólio" de desenvolvedor Mobile?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Um portfólio rico em projetos nativos é o seu melhor cartão de visitas no mercado.">Guardar fotos das férias.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Um portfólio rico em projetos nativos é o seu melhor cartão de visitas no mercado.">Mostrar projetos reais e funcionais que comprovem seu domínio técnico para recrutadores.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Um portfólio rico em projetos nativos é o seu melhor cartão de visitas no mercado.">Ganhar curtidas em redes sociais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Um portfólio rico em projetos nativos é o seu melhor cartão de visitas no mercado.">Salvar links de sites favoritos.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Agora que você concluiu o curso de Desenvolvimento Mobile Nativo, qual o melhor próximo passo?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A tecnologia evolui rápido, e a prática constante é o que diferencia o entusiasta do profissional.">Parar de estudar.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A tecnologia evolui rápido, e a prática constante é o que diferencia o entusiasta do profissional.">Continuar praticando, criar seus próprios apps e explorar novas tecnologias como Jetpack Compose e KMP.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A tecnologia evolui rápido, e a prática constante é o que diferencia o entusiasta do profissional.">Deletar o Android Studio.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A tecnologia evolui rápido, e a prática constante é o que diferencia o entusiasta do profissional.">Esperar o Google lançar uma linguagem nova.</div>
  <div class="quiz-feedback"></div>
</div>
