# Quiz 11 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual a ordem correta das fases do ciclo TDD?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Green -> Red -> Refactor.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Red -> Green -> Refactor.">Red -> Green -> Refactor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Refactor -> Red -> Green.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Green -> Refactor -> Red.
   > **Explicação**: Primeiro falha (Red), depois faz passar (Green) e por fim limpa o código (Refactor).</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Na fase "RED" do TDD, o que deve ser feito?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Corrigir o bug.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Escrever um teste que falhe para uma nova funcionalidade.">Escrever um teste que falhe para uma nova funcionalidade.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Deletar os arquivos antigos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Mudar o tema do VS Code para vermelho.
   > **Explicação**: O teste falha porque a lógica ainda não foi implementada.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. O objetivo da fase "GREEN" é:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Escrever o código mais complexo e perfeito do mundo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Escrever o código mínimo necessário para fazer o teste passar.">Escrever o código mínimo necessário para fazer o teste passar.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Pintar a tela de verde.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Validar a segurança da API.
   > **Explicação**: No Green, focamos apenas na funcionalidade, sem nos preocupar com a limpeza do código ainda.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Quando deve ocorrer a fase de "REFACTOR" no TDD?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Logo após o teste falhar no Red.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Somente após o teste passar no Green.">Somente após o teste passar no Green.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma vez por ano em todos os arquivos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Nunca, pois gasta muito tempo.
   > **Explicação**: Só refatoramos código que já funciona (está protegido pelos testes).</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. TDD é considerado uma técnica de design porque:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ajuda a escolher as cores do site.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Força o desenvolvedor a pensar na interface e usabilidade do código antes da implementação.">Força o desenvolvedor a pensar na interface e usabilidade do código antes da implementação.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O desenvolvedor precisa desenhar fluxogramas.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ele usa Mermaid.js.
   > **Explicação**: Pensar no teste primeiro ajuda a criar códigos mais modulares e desacoplados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O mantra do TDD "Nunca escreva código sem um teste que falhe" promove:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O aumento do número de bugs.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! 100% de cobertura de código para as novas funcionalidades.">100% de cobertura de código para as novas funcionalidades.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A demissão dos testadores manuais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A lentidão eterna do projeto.
   > **Explicação**: Garante que cada linha de código tenha um motivo claro e testado para existir.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. No passo Refactor, é permitido alterar o comportamento do código?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, para adicionar novas features.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Não, o comportamento externo deve permanecer o mesmo; apenas a estrutura interna melhora.">Não, o comportamento externo deve permanecer o mesmo; apenas a estrutura interna melhora.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, para corrigir bugs antigos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, se o cliente pedir.
   > **Explicação**: Refatoração por definição não altera funcionalidade.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual o benefício da "Documentação Viva" gerada pelo TDD?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O software escreve o manual em PDF sozinho.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Os testes mostram exemplos reais de como usar as funções e classes.">Os testes mostram exemplos reais de como usar as funções e classes.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O código fica cheio de comentários explicando tudo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O cliente pode ler os testes e entender a lógica.
   > **Explicação**: Testes bem escritos explicam as regras de negócio de forma técnica e verificável.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Se você escrever código além do necessário no Green, você está violando:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A lei de Murphy.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O princípio YAGNI (You Ain't Gonna Need It).">O princípio YAGNI (You Ain't Gonna Need It).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O design do site.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O horário de almoço.
   > **Explicação**: Escreva apenas o que o teste pede agora.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. O TDD garante que o sistema está 100% livre de bugs de integração?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, sempre.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Não, pois TDD foca principalmente em testes unitários; testes de integração ainda são necessários.">Não, pois TDD foca principalmente em testes unitários; testes de integração ainda são necessários.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Sim, se o ciclo for repetido 10 vezes.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não, o TDD aumenta o número de bugs.
    > **Explicação**: TDD garante a qualidade da unidade, mas a comunicação entre elas precisa de testes específicos.</div>
  <div class="quiz-feedback"></div>
</div>

