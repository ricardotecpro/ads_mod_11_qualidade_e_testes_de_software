# Quiz 12 - Testes Unitários e de Integração 🔗

1. O que caracteriza um Teste Unitário?
   - [x] Testar a menor parte testável de um software (função/método) de forma isolada.
   - [ ] Testar se o sistema abre no celular.
   - [ ] Testar a conexão com a internet.
   - [ ] Testar o sistema inteiro de uma vez.
   > **Explicação**: O isolamento é a chave do teste unitário.

2. Na Pirâmide de Testes, qual nível deve ter a maior quantidade de testes?
   - [ ] UI / End-to-End.
   - [ ] Integração.
   - [x] Unitários.
   - [ ] Testes Manuais.
   > **Explicação**: Testes unitários são mais rápidos, estáveis e baratos de manter.

3. No padrão AAA, o termo "Arrange" significa:
   - [ ] Executar a função.
   - [x] Preparar o cenário e os dados necessários para o teste.
   - [ ] Verificar se o resultado deu certo.
   - [ ] Organizar os arquivos no Windows.
   > **Explicação**: É a fase de setup do teste.

4. O "Assert" no padrão AAA serve para:
   - [ ] Iniciar o cronômetro.
   - [ ] Chamar a API externa.
   - [x] Validar se o resultado real é igual ao resultado esperado.
   - [ ] Deletar os logs de erro.
   > **Explicação**: É o momento da verdade, onde o teste passa ou falha.

5. Qual a principal função de um "Mock"?
   - [ ] Fazer piada com o código alheio.
   - [x] Simular o comportamento de dependências externas (ex: banco de dados) para isolar o teste.
   - [ ] Aumentar a velocidade do processador.
   - [ ] Substituir o testador humano.
   > **Explicação**: Mocks evitam que o teste unitário dependa de fatores externos lentos ou instáveis.

6. Um Teste de Integração foca em:
   - [ ] Testar se o CSS está bonito.
   - [x] Validar a comunicação e o fluxo de dados entre dois ou mais módulos do sistema.
   - [ ] Contar quantas linhas de código foram escritas.
   - [ ] Testar apenas a lógica matemática de uma função.
   > **Explicação**: Verifica se as unidades trabalham bem juntas.

7. Por que os Testes de UI (Topo da pirâmide) são feitos em menor quantidade?
   - [ ] Porque ninguém gosta de testar telas.
   - [x] Porque são lentos, caros e muito sensíveis a mudanças visuais (frágeis).
   - [ ] Porque eles são ilegais em alguns países.
   - [ ] Porque não encontram bugs reais.
   > **Explicação**: Devem ser usados apenas para os fluxos críticos devido ao alto custo de manutenção.

8. O que é um "Falso Positivo" em testes automatizados?
   - [ ] Quando o teste passa, mas existe um bug.
   - [x] Quando o teste falha, mas o sistema está funcionando corretamente.
   - [ ] Quando o teste demora muito para rodar.
   - [ ] Quando o desenvolvedor diz que testou, mas não testou.
   > **Explicação**: Geralmente causado por testes mal escritos ou ambientes instáveis.

9. Testes de Integração devem usar Mocks?
   - [ ] Sim, sempre.
   - [ ] Não, nunca.
   - [x] Depende; preferencialmente utilizam dependências reais ou emuladas para validar a integração real.
   - [ ] Somente se o banco de dados for de graça.
   > **Explicação**: Diferente do unitário, o de integração quer ver a "conversa" real entre as partes.

10. Qual a vantagem de rodar testes unitários em cada commit?
    - [ ] Ocupar o tempo do servidor de CI.
    - [x] Feedback imediato ao desenvolvedor sobre regressões ou erros de lógica.
    - [ ] Ganhar medalhas no GitHub.
    - [ ] Evitar que o computador desligue.
    > **Explicação**: Garante que o código novo não corrompa funcionalidades existentes (Regressão).
