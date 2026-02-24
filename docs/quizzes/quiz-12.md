# Quiz 12 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que caracteriza um Teste Unitário?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Testar a menor parte testável de um software (função/método) de forma isolada.">Testar a menor parte testável de um software (função/método) de forma isolada.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Testar se o sistema abre no celular.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Testar a conexão com a internet.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Testar o sistema inteiro de uma vez.
   > **Explicação**: O isolamento é a chave do teste unitário.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Na Pirâmide de Testes, qual nível deve ter a maior quantidade de testes?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">UI / End-to-End.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Integração.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Unitários.">Unitários.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Testes Manuais.
   > **Explicação**: Testes unitários são mais rápidos, estáveis e baratos de manter.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. No padrão AAA, o termo "Arrange" significa:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Executar a função.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Preparar o cenário e os dados necessários para o teste.">Preparar o cenário e os dados necessários para o teste.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Verificar se o resultado deu certo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Organizar os arquivos no Windows.
   > **Explicação**: É a fase de setup do teste.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O "Assert" no padrão AAA serve para:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Iniciar o cronômetro.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Chamar a API externa.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Validar se o resultado real é igual ao resultado esperado.">Validar se o resultado real é igual ao resultado esperado.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Deletar os logs de erro.
   > **Explicação**: É o momento da verdade, onde o teste passa ou falha.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual a principal função de um "Mock"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Fazer piada com o código alheio.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Simular o comportamento de dependências externas (ex: banco de dados) para isolar o teste.">Simular o comportamento de dependências externas (ex: banco de dados) para isolar o teste.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Aumentar a velocidade do processador.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Substituir o testador humano.
   > **Explicação**: Mocks evitam que o teste unitário dependa de fatores externos lentos ou instáveis.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Um Teste de Integração foca em:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Testar se o CSS está bonito.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Validar a comunicação e o fluxo de dados entre dois ou mais módulos do sistema.">Validar a comunicação e o fluxo de dados entre dois ou mais módulos do sistema.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Contar quantas linhas de código foram escritas.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Testar apenas a lógica matemática de uma função.
   > **Explicação**: Verifica se as unidades trabalham bem juntas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Por que os Testes de UI (Topo da pirâmide) são feitos em menor quantidade?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque ninguém gosta de testar telas.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Porque são lentos, caros e muito sensíveis a mudanças visuais (frágeis).">Porque são lentos, caros e muito sensíveis a mudanças visuais (frágeis).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque eles são ilegais em alguns países.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque não encontram bugs reais.
   > **Explicação**: Devem ser usados apenas para os fluxos críticos devido ao alto custo de manutenção.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que é um "Falso Positivo" em testes automatizados?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Quando o teste passa, mas existe um bug.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Quando o teste falha, mas o sistema está funcionando corretamente.">Quando o teste falha, mas o sistema está funcionando corretamente.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Quando o teste demora muito para rodar.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Quando o desenvolvedor diz que testou, mas não testou.
   > **Explicação**: Geralmente causado por testes mal escritos ou ambientes instáveis.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Testes de Integração devem usar Mocks?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, sempre.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não, nunca.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Depende; preferencialmente utilizam dependências reais ou emuladas para validar a integração real.">Depende; preferencialmente utilizam dependências reais ou emuladas para validar a integração real.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Somente se o banco de dados for de graça.
   > **Explicação**: Diferente do unitário, o de integração quer ver a "conversa" real entre as partes.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Qual a vantagem de rodar testes unitários em cada commit?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ocupar o tempo do servidor de CI.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Feedback imediato ao desenvolvedor sobre regressões ou erros de lógica.">Feedback imediato ao desenvolvedor sobre regressões ou erros de lógica.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ganhar medalhas no GitHub.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Evitar que o computador desligue.
    > **Explicação**: Garante que o código novo não corrompa funcionalidades existentes (Regressão).</div>
  <div class="quiz-feedback"></div>
</div>

