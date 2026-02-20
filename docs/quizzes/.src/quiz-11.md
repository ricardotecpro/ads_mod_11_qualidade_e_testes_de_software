# Quiz 11 - Desenvolvimento Orientado por Testes (TDD) 🔴🟢🔵

1. Qual a ordem correta das fases do ciclo TDD?
   - [ ] Green -> Red -> Refactor.
   - [x] Red -> Green -> Refactor.
   - [ ] Refactor -> Red -> Green.
   - [ ] Green -> Refactor -> Red.
   > **Explicação**: Primeiro falha (Red), depois faz passar (Green) e por fim limpa o código (Refactor).

2. Na fase "RED" do TDD, o que deve ser feito?
   - [ ] Corrigir o bug.
   - [x] Escrever um teste que falhe para uma nova funcionalidade.
   - [ ] Deletar os arquivos antigos.
   - [ ] Mudar o tema do VS Code para vermelho.
   > **Explicação**: O teste falha porque a lógica ainda não foi implementada.

3. O objetivo da fase "GREEN" é:
   - [ ] Escrever o código mais complexo e perfeito do mundo.
   - [x] Escrever o código mínimo necessário para fazer o teste passar.
   - [ ] Pintar a tela de verde.
   - [ ] Validar a segurança da API.
   > **Explicação**: No Green, focamos apenas na funcionalidade, sem nos preocupar com a limpeza do código ainda.

4. Quando deve ocorrer a fase de "REFACTOR" no TDD?
   - [ ] Logo após o teste falhar no Red.
   - [x] Somente após o teste passar no Green.
   - [ ] Uma vez por ano em todos os arquivos.
   - [ ] Nunca, pois gasta muito tempo.
   > **Explicação**: Só refatoramos código que já funciona (está protegido pelos testes).

5. TDD é considerado uma técnica de design porque:
   - [ ] Ajuda a escolher as cores do site.
   - [x] Força o desenvolvedor a pensar na interface e usabilidade do código antes da implementação.
   - [ ] O desenvolvedor precisa desenhar fluxogramas.
   - [ ] Ele usa Mermaid.js.
   > **Explicação**: Pensar no teste primeiro ajuda a criar códigos mais modulares e desacoplados.

6. O mantra do TDD "Nunca escreva código sem um teste que falhe" promove:
   - [ ] O aumento do número de bugs.
   - [x] 100% de cobertura de código para as novas funcionalidades.
   - [ ] A demissão dos testadores manuais.
   - [ ] A lentidão eterna do projeto.
   > **Explicação**: Garante que cada linha de código tenha um motivo claro e testado para existir.

7. No passo Refactor, é permitido alterar o comportamento do código?
   - [ ] Sim, para adicionar novas features.
   - [x] Não, o comportamento externo deve permanecer o mesmo; apenas a estrutura interna melhora.
   - [ ] Sim, para corrigir bugs antigos.
   - [ ] Sim, se o cliente pedir.
   > **Explicação**: Refatoração por definição não altera funcionalidade.

8. Qual o benefício da "Documentação Viva" gerada pelo TDD?
   - [ ] O software escreve o manual em PDF sozinho.
   - [x] Os testes mostram exemplos reais de como usar as funções e classes.
   - [ ] O código fica cheio de comentários explicando tudo.
   - [ ] O cliente pode ler os testes e entender a lógica.
   > **Explicação**: Testes bem escritos explicam as regras de negócio de forma técnica e verificável.

9. Se você escrever código além do necessário no Green, você está violando:
   - [ ] A lei de Murphy.
   - [x] O princípio YAGNI (You Ain't Gonna Need It).
   - [ ] O design do site.
   - [ ] O horário de almoço.
   > **Explicação**: Escreva apenas o que o teste pede agora.

10. O TDD garante que o sistema está 100% livre de bugs de integração?
    - [ ] Sim, sempre.
    - [x] Não, pois TDD foca principalmente em testes unitários; testes de integração ainda são necessários.
    - [ ] Sim, se o ciclo for repetido 10 vezes.
    - [ ] Não, o TDD aumenta o número de bugs.
    > **Explicação**: TDD garante a qualidade da unidade, mas a comunicação entre elas precisa de testes específicos.
