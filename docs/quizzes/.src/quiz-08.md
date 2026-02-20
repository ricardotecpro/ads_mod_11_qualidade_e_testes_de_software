# Quiz 08 - Técnicas de Teste: Caixa Branca ⚪

1. O Teste de Caixa Branca também é conhecido como:
   - [ ] Teste Funcional.
   - [x] Teste Estrutural ou Baseado em Código.
   - [ ] Teste de Usuário Final.
   - [ ] Teste de Corretude Visual.
   > **Explicação**: Recebe esse nome porque o testador "enxerga" a estrutura interna do programa.

2. A métrica "Cobertura de Instruções" (Statement Coverage) mede:
   - [ ] Quantos manuais foram lidos.
   - [x] O percentual de linhas de código que foram executadas pelos testes.
   - [ ] O número de vezes que o sistema travou.
   - [ ] A quantidade de comentários no código.
   > **Explicação**: Garante que cada instrução tenha sido processada pelo menos uma vez.

3. Por que ter 100% de cobertura de instruções não garante que o código está livre de bugs?
   - [ ] Porque os testadores podem estar mentindo.
   - [x] Porque as instruções podem ter sido executadas, mas não com todas as combinações de dados ou caminhos lógicos possíveis.
   - [ ] Porque cobertura de código é uma métrica inútil.
   - [ ] Porque bugs só existem em hardware.
   > **Explicação**: A lógica interna (ex: combinações de if/else) pode ser mais complexa que a simples execução das linhas.

4. O que é a Cobertura de Decisão (Decision Coverage)?
   - [ ] Contar quantos gerentes decidiram aprovar o projeto.
   - [x] Garantir que cada ponto de decisão (ex: IF) foi testado tanto como Verdadeiro quanto como Falso.
   - [ ] Testar apenas o caminho feliz.
   - [ ] Verificar se o banco de dados está online.
   > **Explicação**: Foca em percorrer todos os ramos de um desvio condicional.

5. No teste de caminhos, o que é um "Grafo de Fluxo de Controle"?
   - [ ] Um desenho artístico do sistema.
   - [x] Uma representação visual de todos os caminhos possíveis que a execução do código pode seguir.
   - [ ] Um organograma da empresa.
   - [ ] O mapa da rede de computadores.
   > **Explicação**: Ajuda a identificar caminhos complexos ou mortos no código.

6. A técnica de Caixa Branca é mais comumente realizada em qual nível de teste?
   - [ ] Teste de Aceitação (UAT).
   - [x] Teste Unitário.
   - [ ] Teste de Usabilidade.
   - [ ] Teste de Carga.
   > **Explicação**: Desenvolvedores usam caixa branca para validar suas próprias funções e classes.

7. Qual a principal vantagem da Caixa Branca?
   - [ ] Não precisa saber programar.
   - [x] Permite identificar trechos de código que nunca são executados (código morto) e erros de lógica ocultos.
   - [ ] É a técnica favorita dos clientes.
   - [ ] Reduz o custo de hardware.
   > **Explicação**: Dá visibilidade total sobre a eficiência e a limpeza da implementação.

8. O que é "Complexidade Ciclomática"?
   - [ ] Um programa que anda de bicicleta.
   - [x] Uma medida métrica que indica o número de caminhos linearmente independentes no código.
   - [ ] O tempo que leva para compilar o código.
   - [ ] O número de variáveis em uma função.
   > **Explicação**: Quanto maior a complexidade, mais difícil é testar e manter o código.

9. Testes de Caixa Branca podem ser usados para verificar:
   - [ ] Se o logotipo está no lugar certo.
   - [x] Fluxos de dados, caminhos de exceção e condições de laços (loops).
   - [ ] A satisfação do usuário final.
   - [ ] A beleza das cores da interface.
   > **Explicação**: Foca na robustez técnica e lógica do algoritmo.

10. Qual ferramenta é famosa por gerar relatórios de cobertura de código em Python?
    - [ ] Postman.
    - [ ] Selenium.
    - [x] Coverage.py (usando pytest-cov).
    - [ ] Photoshop.
    > **Explicação**: Coverage.py é a ferramenta padrão para medir a cobertura de testes em ecossistemas Python.
