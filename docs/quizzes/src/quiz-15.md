# Quiz 15 - Gestão de Defeitos e Ferramentas 🐛

1. Qual o principal objetivo de uma ferramenta de "Bug Tracking" como o Jira?
   - [ ] Enviar emails para o cliente.
   - [x] Registrar, priorizar e acompanhar o ciclo de vida dos defeitos encontrados.
   - [ ] Compilar o código-fonte.
   - [ ] Hospedar o site da empresa.
   > **Explicação**: Ferramentas de gestão trazem transparência e organização ao processo de QA.

2. No ciclo de vida de um bug, o estado "Aberto" significa:
   - [ ] O bug já foi corrigido.
   - [x] O bug foi validado e aguarda a ação do desenvolvedor para ser corrigido.
   - [ ] O sistema parou de funcionar sozinho.
   - [ ] O QA está de férias.
   > **Explicação**: Indica que o defeito é real e está na fila de trabalho.

3. O que um QA deve fazer quando um desenvolvedor marca um bug como "Resolvido/Corrigido"?
   - [ ] Acreditar e fechar o bug imediatamente.
   - [ ] Apagar o registro do bug.
   - [x] Realizar o Reteste no ambiente de QA para confirmar a correção.
   - [ ] Abrir um novo projeto.
   > **Explicação**: O reteste é obrigatório para garantir que a correção foi efetiva e não gerou novos problemas.

4. Um bug com "Alta Severidade" indica:
   - [ ] Que o erro é apenas visual e não afeta o uso.
   - [x] Que o impacto técnico no sistema é grande (ex: perda de dados, sistema travado).
   - [ ] Que o cliente está gritando no telefone.
   - [ ] Que o erro é impossível de corrigir.
   > **Explicação**: Severidade mede o dano técnico causado pelo defeito.

5. O termo "Prioridade" em um ticket de bug define:
   - [ ] Quem é o dono da empresa.
   - [x] A ordem de importância para a correção do ponto de vista do negócio/urgência.
   - [ ] Quantas linhas de código o bug tem.
   - [ ] A cor do ícone no Jira.
   > **Explicação**: Define "quando" o bug deve ser corrigido frente a outras tarefas.

6. O que é "Bug Leakage"?
   - [ ] Um vazamento de água no servidor.
   - [x] Defeitos que passaram despercebidos pelos testes e foram encontrados pelo usuário final em produção.
   - [ ] Quando o desenvolvedor conta o segredo do projeto.
   - [ ] Uma técnica de hacking.
   > **Explicação**: É uma métrica de qualidade; quanto menor o vazamento, melhor o processo de teste.

7. No Jira, uma "Issue" pode representar:
   - [ ] Um Bug.
   - [ ] Uma Melhoria (Improvement).
   - [ ] Uma Nova Funcionalidade (Story).
   - [x] Todas as alternativas anteriores.
   > **Explicação**: O Jira é flexível e permite gerenciar diversos tipos de itens de trabalho.

8. Por que "Evidências" (prints, logs) são cruciais em um report de bug?
   - [ ] Para o documento ficar mais colorido.
   - [x] Para comprovar a existência do erro e ajudar o desenvolvedor a diagnosticar a causa raiz.
   - [ ] Para ocupar espaço no servidor.
   - [ ] Somente se o bug for muito difícil.
   > **Explicação**: Evidências economizam tempo e evitam o "na minha máquina funciona".

9. Um bug "Postergado" (Deferred) é aquele que:
   - [ ] Nunca será corrigido.
   - [x] Teve sua correção adiada para uma versão ou sprint futura por decisão do negócio.
   - [ ] Foi corrigido mas voltou a aparecer.
   - [ ] Foi criado por engano.
   > **Explicação**: Indica que o bug é conhecido, mas não é a prioridade atual.

10. A reunião de "Bug Triage" serve para:
    - [ ] Tomar café com o time.
    - [x] Analisar os bugs abertos e decidir coletivamente sobre sua severidade, prioridade e quem irá corrigi-los.
    - [ ] Demitir o testador que encontrou o bug.
    - [ ] Celebrar o final do projeto.
    > **Explicação**: É um momento de alinhamento entre QA, Dev e Product Owner (PO).
