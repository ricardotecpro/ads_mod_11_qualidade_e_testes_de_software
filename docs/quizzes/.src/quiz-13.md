# Quiz 13 - Automação de Testes Web 🤖

1. Qual a principal vantagem da automação de testes E2E (End-to-End)?
   - [ ] Reduzir o número de desenvolvedores na equipe.
   - [ ] Garantir que o código-fonte está bonito.
   - [x] Simular a jornada real do usuário e economizar tempo em testes de regressão manuais.
   - [ ] Aumentar a velocidade da internet.
   > **Explicação**: Automação web foca em repetir fluxos críticos de forma rápida e precisa.

2. O que é o Selenium WebDriver?
   - [ ] Uma linguagem de programação.
   - [x] Uma ferramenta veterana de automação que permite controlar navegadores programaticamente.
   - [ ] Um editor de texto para QAs.
   - [ ] Um navegador novo.
   > **Explicação**: Selenium é a base histórica da automação web, suportando diversas linguagens.

3. Qual ferramenta moderna é conhecida pela sua velocidade e recursos de "auto-waiting"?
   - [ ] Blocos de Notas.
   - [ ] Excel.
   - [x] Playwright / Cypress.
   - [ ] Postman.
   > **Explicação**: Playwright e Cypress resolvem muitos problemas de "flakiness" das ferramentas antigas.

4. Na automação web, o que é um "Locator" (Localizador)?
   - [ ] O GPS do celular do testador.
   - [x] Uma estratégia para encontrar um elemento HTML na página (ex: ID, CSS, XPath).
   - [ ] O endereço físico do servidor.
   - [ ] Um tipo de vírus.
   > **Explicação**: Sem localizadores, o robô não sabe em qual botão clicar.

5. Qual o seletor mais recomendado por ser mais estável?
   - [ ] Texto completo da página.
   - [x] ID único (`#id`) ou Atributos de Teste (`data-testid`).
   - [ ] Classe CSS (`.btn-red`).
   - [ ] XPath absoluto.
   > **Explicação**: IDs e atributos dedicados a testes não costumam mudar quando o layout é alterado.

6. O que significa "Flakiness" (Instabilidade) em testes automatizados?
   - [ ] Quando o teste passa sempre.
   - [x] Quando um teste ora passa, ora falha, sem que tenha havido mudança no código.
   - [ ] Quando o computador do QA quebra.
   - [ ] Quando o código é escrito em Python.
   > **Explicação**: Testes instáveis perdem a credibilidade e geralmente ocorrem por problemas de sincronização.

7. Por que devemos evitar o uso excessivo de `sleep(5)` nos scripts?
   - [ ] Porque é proibido por lei.
   - [x] Porque torna os testes desnecessariamente lentos; o ideal é usar "esperas inteligentes" (waits).
   - [ ] Porque gasta muita energia elétrica.
   - [ ] Porque o robô pode dormir e não acordar.
   > **Explicação**: Esperas explícitas (sleep) são ineficientes; esperas dinâmicas são melhores.

8. O padrão "Page Object Model" (POM) visa:
   - [ ] Deixar o código mais confuso.
   - [x] Melhorar a organização e manutenção, separando a lógica de interação da lógica do teste.
   - [ ] Criar páginas web automaticamente.
   - [ ] Substituir o uso de classes em Java.
   > **Explicação**: Com POM, se um botão mudar de lugar, você altera apenas em um arquivo centralizado.

9. Qual o papel das "Assertions" (Asserções) em um script de automação?
   - [ ] Clicar no botão.
   - [x] Validar se o estado final do sistema é o esperado (ex: verificar se a mensagem de sucesso apareceu).
   - [ ] Digitar a senha.
   - [ ] Reiniciar o Windows.
   > **Explicação**: Sem asserções, o teste apenas "anda" pelo sistema sem validar nada.

10. Automação de UI deve cobrir 100% de todos os fluxos possíveis?
    - [ ] Sim, para dar segurança total.
    - [x] Não, deve focar nos fluxos críticos (Happy Path) devido ao alto custo de manutenção.
    - [ ] Somente se o cliente pagar extra.
    - [ ] Sim, se o time for grande.
    > **Explicação**: A base da pirâmide (Unitários) deve cobrir a maior parte da lógica; a UI foca no essencial.
