# Quiz 14 - Testes, Qualidade e Debugging 🐞

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual a principal diferença entre um Teste Unitário e um Teste de UI no Android?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Testes Unitários são a base da pirâmide (rápidos e baratos), enquanto testes de UI (Espresso) são mais lentos e complexos.">Testes de UI são mais rápidos.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Testes Unitários são a base da pirâmide (rápidos e baratos), enquanto testes de UI (Espresso) são mais lentos e complexos.">Testes Unitários testam lógica rápida na JVM (computador); Testes de UI rodam no emulador/celular clicando na tela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Testes Unitários são a base da pirâmide (rápidos e baratos), enquanto testes de UI (Espresso) são mais lentos e complexos.">Testes Unitários só funcionam com Java.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Testes Unitários são a base da pirâmide (rápidos e baratos), enquanto testes de UI (Espresso) são mais lentos e complexos.">Não há diferença, são o mesmo arquivo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Para que serve o "Logcat" no Android Studio?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É o console de saída onde o desenvolvedor monitora toda a saúde do app em tempo real.">Para desenhar ícones.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! É o console de saída onde o desenvolvedor monitora toda a saúde do app em tempo real.">Para visualizar mensagens de sistema, erros e logs personalizados que ajudam a encontrar bugs.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É o console de saída onde o desenvolvedor monitora toda a saúde do app em tempo real.">Para salvar o app na nuvem.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. É o console de saída onde o desenvolvedor monitora toda a saúde do app em tempo real.">Para aumentar a velocidade da internet.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual o nível de log (`Log.x`) deve ser usado para indicar um erro crítico que faz o app parar de funcionar conforme esperado?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Log.e aparece em vermelho no Logcat e ajuda a identificar falhas graves rapidamente.">Log.v (Verbose)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Log.e aparece em vermelho no Logcat e ajuda a identificar falhas graves rapidamente.">Log.d (Debug)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Log.e aparece em vermelho no Logcat e ajuda a identificar falhas graves rapidamente.">Log.i (Info)</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Log.e aparece em vermelho no Logcat e ajuda a identificar falhas graves rapidamente.">Log.e (Error)</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O que é um "Breakpoint" no processo de Debugging?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Breakpoints permitem a inspeção "ao vivo" do estado do app linha por linha.">Uma tecla que quebrou.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Breakpoints permitem a inspeção "ao vivo" do estado do app linha por linha.">Um ponto de interrupção no código onde a execução para para o desenvolvedor analisar o valor das variáveis.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Breakpoints permitem a inspeção "ao vivo" do estado do app linha por linha.">O final do programa.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Breakpoints permitem a inspeção "ao vivo" do estado do app linha por linha.">Um erro de compilação.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual biblioteca é o padrão para realizar testes de interface (UI) no Android?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Espresso permite encontrar elementos na tela (`withId`) e realizar ações (`click()`, `typeText()`).">JUnit</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Espresso permite encontrar elementos na tela (`withId`) e realizar ações (`click()`, `typeText()`).">Mockito</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Espresso permite encontrar elementos na tela (`withId`) e realizar ações (`click()`, `typeText()`).">Espresso</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Espresso permite encontrar elementos na tela (`withId`) e realizar ações (`click()`, `typeText()`).">Retrofit</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O que o framework JUnit faz?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O JUnit é o framework de testes mais popular do mundo Java/Kotlin.">Desenha layouts.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O JUnit é o framework de testes mais popular do mundo Java/Kotlin.">Fornece a estrutura para escrever e rodar testes unitários (anotações como `@Test`).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O JUnit é o framework de testes mais popular do mundo Java/Kotlin.">Faz o build do app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O JUnit é o framework de testes mais popular do mundo Java/Kotlin.">Envia o app para a loja.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Por que devemos usar `try/catch` em operações de rede?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O tratamento de exceções garante que o app continue rodando mesmo diante de imprevistos externos.">Para o código ficar mais longo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O tratamento de exceções garante que o app continue rodando mesmo diante de imprevistos externos.">Para evitar que o app feche (Crash) caso a internet falhe ou o servidor retorne erro.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O tratamento de exceções garante que o app continue rodando mesmo diante de imprevistos externos.">Para o download ser mais rápido.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O tratamento de exceções garante que o app continue rodando mesmo diante de imprevistos externos.">Porque é obrigatório em todas as funções.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que significa "Refatorar" um código?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Refatorar é essencial para manter a saúde do projeto a longo prazo.">Adicionar novas funcionalidades.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Refatorar é essencial para manter a saúde do projeto a longo prazo.">Reorganizar e limpar o código existente para melhorar a qualidade, sem mudar o que ele faz para o usuário.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Refatorar é essencial para manter a saúde do projeto a longo prazo.">Apagar todo o projeto e começar do zero.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Refatorar é essencial para manter a saúde do projeto a longo prazo.">Traduzir o app.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual é a ferramenta de testes automatizados da Apple para o iOS?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O XCTest é o framework nativo da Apple para testes unitários, de performance e de UI.">Espresso iOS</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O XCTest é o framework nativo da Apple para testes unitários, de performance e de UI.">AppleTest</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O XCTest é o framework nativo da Apple para testes unitários, de performance e de UI.">XCTest</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O XCTest é o framework nativo da Apple para testes unitários, de performance e de UI.">SwiftUnit</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Qual a porcentagem ideal de cobertura de testes unitários recomendada pela "Pirâmide de Testes"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Testes unitários são a fundação por serem rápidos, estáveis e fáceis de manter.">0% (não precisa testar).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Testes unitários são a fundação por serem rápidos, estáveis e fáceis de manter.">10% (testar só o login).</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Testes unitários são a fundação por serem rápidos, estáveis e fáceis de manter.">Cerca de 70% (deve ser a maior parte dos seus testes).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Testes unitários são a fundação por serem rápidos, estáveis e fáceis de manter.">100% (testar cada linha exaustivamente).</div>
  <div class="quiz-feedback"></div>
</div>
