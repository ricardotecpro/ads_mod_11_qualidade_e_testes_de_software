# Quiz 08 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O Teste de Caixa Branca também é conhecido como:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Teste Funcional.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Teste Estrutural ou Baseado em Código.">Teste Estrutural ou Baseado em Código.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Teste de Usuário Final.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Teste de Corretude Visual.
   > **Explicação**: Recebe esse nome porque o testador "enxerga" a estrutura interna do programa.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. A métrica "Cobertura de Instruções" (Statement Coverage) mede:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Quantos manuais foram lidos.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O percentual de linhas de código que foram executadas pelos testes.">O percentual de linhas de código que foram executadas pelos testes.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O número de vezes que o sistema travou.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A quantidade de comentários no código.
   > **Explicação**: Garante que cada instrução tenha sido processada pelo menos uma vez.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Por que ter 100% de cobertura de instruções não garante que o código está livre de bugs?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque os testadores podem estar mentindo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Porque as instruções podem ter sido executadas, mas não com todas as combinações de dados ou caminhos lógicos possíveis.">Porque as instruções podem ter sido executadas, mas não com todas as combinações de dados ou caminhos lógicos possíveis.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque cobertura de código é uma métrica inútil.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque bugs só existem em hardware.
   > **Explicação**: A lógica interna (ex: combinações de if/else) pode ser mais complexa que a simples execução das linhas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O que é a Cobertura de Decisão (Decision Coverage)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Contar quantos gerentes decidiram aprovar o projeto.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Garantir que cada ponto de decisão (ex: IF) foi testado tanto como Verdadeiro quanto como Falso.">Garantir que cada ponto de decisão (ex: IF) foi testado tanto como Verdadeiro quanto como Falso.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Testar apenas o caminho feliz.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Verificar se o banco de dados está online.
   > **Explicação**: Foca em percorrer todos os ramos de um desvio condicional.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. No teste de caminhos, o que é um "Grafo de Fluxo de Controle"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um desenho artístico do sistema.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Uma representação visual de todos os caminhos possíveis que a execução do código pode seguir.">Uma representação visual de todos os caminhos possíveis que a execução do código pode seguir.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um organograma da empresa.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O mapa da rede de computadores.
   > **Explicação**: Ajuda a identificar caminhos complexos ou mortos no código.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. A técnica de Caixa Branca é mais comumente realizada em qual nível de teste?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Teste de Aceitação (UAT).</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Teste Unitário.">Teste Unitário.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Teste de Usabilidade.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Teste de Carga.
   > **Explicação**: Desenvolvedores usam caixa branca para validar suas próprias funções e classes.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Qual a principal vantagem da Caixa Branca?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não precisa saber programar.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Permite identificar trechos de código que nunca são executados (código morto) e erros de lógica ocultos.">Permite identificar trechos de código que nunca são executados (código morto) e erros de lógica ocultos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">É a técnica favorita dos clientes.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Reduz o custo de hardware.
   > **Explicação**: Dá visibilidade total sobre a eficiência e a limpeza da implementação.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que é "Complexidade Ciclomática"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um programa que anda de bicicleta.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Uma medida métrica que indica o número de caminhos linearmente independentes no código.">Uma medida métrica que indica o número de caminhos linearmente independentes no código.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O tempo que leva para compilar o código.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O número de variáveis em uma função.
   > **Explicação**: Quanto maior a complexidade, mais difícil é testar e manter o código.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Testes de Caixa Branca podem ser usados para verificar:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Se o logotipo está no lugar certo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Fluxos de dados, caminhos de exceção e condições de laços (loops).">Fluxos de dados, caminhos de exceção e condições de laços (loops).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A satisfação do usuário final.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A beleza das cores da interface.
   > **Explicação**: Foca na robustez técnica e lógica do algoritmo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Qual ferramenta é famosa por gerar relatórios de cobertura de código em Python?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Postman.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Selenium.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Coverage.py (usando pytest-cov).">Coverage.py (usando pytest-cov).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Photoshop.
    > **Explicação**: Coverage.py é a ferramenta padrão para medir a cobertura de testes em ecossistemas Python.</div>
  <div class="quiz-feedback"></div>
</div>

