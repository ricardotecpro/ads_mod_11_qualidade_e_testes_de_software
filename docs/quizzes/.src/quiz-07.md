# Quiz 07 - Técnicas de Teste: Caixa Preta 🌑

1. O teste de Caixa Preta foca em:
   - [ ] A estrutura interna e os algoritmos do código.
   - [x] As entradas e saídas esperadas com base nos requisitos funcionais.
   - [ ] A cor do monitor do testador.
   - [ ] O número de linhas de comentários.
   > **Explicação**: Caixa Preta ignora o "como" o código foi feito e foca no "quê" ele faz.

2. A técnica de "Partição de Equivalência" serve para:
   - [ ] Dividir o salário dos testadores igualmente.
   - [x] Agrupar dados de entrada que produzem o mesmo tipo de resultado, testando apenas um exemplo de cada grupo.
   - [ ] Testar todos os números de 1 a 1 milhão um por um.
   - [ ] Separar bugs de interface de bugs de banco de dados.
   > **Explicação**: Reduz o número de testes necessários mantendo a cobertura.

3. Se um campo aceita valores de 10 a 20, quais são os "Valores Limite"?
   - [ ] 0, 50, 100.
   - [ ] 15 apenas.
   - [x] 9, 10, 11 e 19, 20, 21.
   - [ ] 10-20.
   > **Explicação**: Testamos as bordas (dentro e fora) onde o erro é mais provável.

4. Na técnica de "Tabela de Decisão", analisamos:
   - [ ] Onde os desenvolvedores devem sentar.
   - [x] Combinações de diferentes condições de entrada para determinar o resultado esperado.
   - [ ] O preço de licenças de software.
   - [ ] A ordem alfabética dos requisitos.
   > **Explicação**: É útil para lógicas de negócio complexas com múltiplas variáveis.

5. Um teste de Caixa Preta pode ser executado por:
   - [ ] Apenas por quem escreveu o código.
   - [x] Por testadores, usuários finais ou desenvolvedores, sem necessidade de ler o código.
   - [ ] Apenas pelo compilador.
   - [ ] Somente por inteligência artificial.
   > **Explicação**: Como não exige ler o código, qualquer pessoa pode realizá-lo com base no manual ou especificação.

6. O que é um "Valor Inválido" em Partição de Equivalência?
   - [ ] Um valor que quebra o computador.
   - [x] Um dado que não deve ser aceito pelo sistema segundo as regras.
   - [ ] Um número negativo sempre.
   - [ ] O nome do usuário.
   > **Explicação**: Testar entradas inválidas é essencial para garantir a robustez do sistema.

7. Por que os Testes de Caixa Preta são importantes para a Validação?
   - [ ] Porque eles são mais rápidos que os de Caixa Branca.
   - [x] Porque eles confirmam se o sistema faz o que o usuário realmente precisa.
   - [ ] Porque eles encontram erros de sintaxe no código.
   - [ ] Porque eles usam menos memória do servidor.
   > **Explicação**: Estão ligados diretamente aos requisitos de negócio e experiência do usuário.

8. Se uma entrada de texto aceita de 1 a 10 caracteres, o valor "11" pertence a qual partição?
   - [ ] Partição Válida.
   - [x] Partição Inválida Superior.
   - [ ] Partição de Valor Nulo.
   - [ ] Partição de Memória.
   > **Explicação**: Qualquer valor acima do limite máximo é uma partição inválida.

9. A técnica de "Transição de Estados" é usada para testar:
   - [ ] A mudança de governo em um país.
   - [x] Sistemas onde o comportamento depende do que aconteceu anteriormente (ex: status de um pedido).
   - [ ] A velocidade de upload de arquivos.
   - [ ] A cor de fundo de um botão.
   > **Explicação**: Foca em fluxos onde uma ação leva a um novo estado (Aberto -> Pago -> Enviado).

10. A principal desvantagem da Caixa Preta pura é:
    - [ ] É muito difícil de aprender.
    - [x] Pode deixar caminhos internos do código (como um 'if' escondido) sem serem testados.
    - [ ] Exige computadores de alta performance.
    - [ ] Só funciona para sites.
    > **Explicação**: Como não olhamos o código, não sabemos se 100% da lógica interna foi percorrida.
