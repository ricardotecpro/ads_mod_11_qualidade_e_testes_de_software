# Quiz 13 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual a principal vantagem da automação de testes E2E (End-to-End)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Reduzir o número de desenvolvedores na equipe.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Garantir que o código-fonte está bonito.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Simular a jornada real do usuário e economizar tempo em testes de regressão manuais.">Simular a jornada real do usuário e economizar tempo em testes de regressão manuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Aumentar a velocidade da internet.
   > **Explicação**: Automação web foca em repetir fluxos críticos de forma rápida e precisa.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. O que é o Selenium WebDriver?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma linguagem de programação.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Uma ferramenta veterana de automação que permite controlar navegadores programaticamente.">Uma ferramenta veterana de automação que permite controlar navegadores programaticamente.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um editor de texto para QAs.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um navegador novo.
   > **Explicação**: Selenium é a base histórica da automação web, suportando diversas linguagens.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual ferramenta moderna é conhecida pela sua velocidade e recursos de "auto-waiting"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Blocos de Notas.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Excel.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Playwright / Cypress.">Playwright / Cypress.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Postman.
   > **Explicação**: Playwright e Cypress resolvem muitos problemas de "flakiness" das ferramentas antigas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Na automação web, o que é um "Locator" (Localizador)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O GPS do celular do testador.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Uma estratégia para encontrar um elemento HTML na página (ex: ID, CSS, XPath).">Uma estratégia para encontrar um elemento HTML na página (ex: ID, CSS, XPath).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O endereço físico do servidor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um tipo de vírus.
   > **Explicação**: Sem localizadores, o robô não sabe em qual botão clicar.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual o seletor mais recomendado por ser mais estável?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Texto completo da página.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! ID único (`#id`) ou Atributos de Teste (`data-testid`).">ID único (`#id`) ou Atributos de Teste (`data-testid`).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Classe CSS (`.btn-red`).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">XPath absoluto.
   > **Explicação**: IDs e atributos dedicados a testes não costumam mudar quando o layout é alterado.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O que significa "Flakiness" (Instabilidade) em testes automatizados?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Quando o teste passa sempre.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Quando um teste ora passa, ora falha, sem que tenha havido mudança no código.">Quando um teste ora passa, ora falha, sem que tenha havido mudança no código.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Quando o computador do QA quebra.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Quando o código é escrito em Python.
   > **Explicação**: Testes instáveis perdem a credibilidade e geralmente ocorrem por problemas de sincronização.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Por que devemos evitar o uso excessivo de `sleep(5)` nos scripts?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque é proibido por lei.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Porque torna os testes desnecessariamente lentos; o ideal é usar "esperas inteligentes" (waits).">Porque torna os testes desnecessariamente lentos; o ideal é usar "esperas inteligentes" (waits).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque gasta muita energia elétrica.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Porque o robô pode dormir e não acordar.
   > **Explicação**: Esperas explícitas (sleep) são ineficientes; esperas dinâmicas são melhores.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O padrão "Page Object Model" (POM) visa:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Deixar o código mais confuso.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Melhorar a organização e manutenção, separando a lógica de interação da lógica do teste.">Melhorar a organização e manutenção, separando a lógica de interação da lógica do teste.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Criar páginas web automaticamente.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Substituir o uso de classes em Java.
   > **Explicação**: Com POM, se um botão mudar de lugar, você altera apenas em um arquivo centralizado.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual o papel das "Assertions" (Asserções) em um script de automação?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Clicar no botão.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Validar se o estado final do sistema é o esperado (ex: verificar se a mensagem de sucesso apareceu).">Validar se o estado final do sistema é o esperado (ex: verificar se a mensagem de sucesso apareceu).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Digitar a senha.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Reiniciar o Windows.
   > **Explicação**: Sem asserções, o teste apenas "anda" pelo sistema sem validar nada.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Automação de UI deve cobrir 100% de todos os fluxos possíveis?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, para dar segurança total.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Não, deve focar nos fluxos críticos (Happy Path) devido ao alto custo de manutenção.">Não, deve focar nos fluxos críticos (Happy Path) devido ao alto custo de manutenção.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Somente se o cliente pagar extra.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, se o time for grande.
    > **Explicação**: A base da pirâmide (Unitários) deve cobrir a maior parte da lógica; a UI foca no essencial.</div>
  <div class="quiz-feedback"></div>
</div>

