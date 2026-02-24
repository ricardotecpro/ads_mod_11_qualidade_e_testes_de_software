# Quiz 06 - Controle de Versão e CI 🐙

1. O que é o Git?
   - [ ] Uma rede social para desenvolvedores.
   - [x] Um sistema de controle de versão distribuído.
   - [ ] Uma linguagem de programação de alto desempenho.
   - [ ] Um provedor de internet.
   > **Explicação**: Git permite rastrear mudanças no código e colaborar com outros desenvolvedores.

2. O que faz o comando `git commit`?
   - [ ] Envia o código para o servidor remoto.
   - [x] Salva as alterações no repositório local com uma mensagem descritiva.
   - [ ] Apaga todas as mudanças feitas no dia.
   - [ ] Cria uma conta no GitHub.
   > **Explicação**: O commit cria um "ponto de restauração" histórico no seu repositório local.

3. Qual a função de uma "Branch" (Ramo) no Git?
   - [ ] Desligar o computador do colega.
   - [x] Criar uma linha de desenvolvimento isolada da principal.
   - [ ] Deletar arquivos duplicados.
   - [ ] Traduzir o código para português.
   > **Explicação**: Branches permitem trabalhar em novas features sem afetar o código estável (`main`).

4. No contexto do GitHub Actions, o que é um "Workflow"?
   - [ ] A mesa de trabalho do desenvolvedor.
   - [x] Um processo automatizado configurado no repositório (ex: para rodar testes).
   - [ ] Uma lista de bugs pendentes.
   - [ ] O manual de marca da empresa.
   > **Explicação**: Workflows automatizam tarefas como build, teste e deploy.

5. A Integração Contínua (CI) tem como objetivo:
   - [ ] Integrar o software com as redes sociais.
   - [ ] Forçar todos os desenvolvedores a trabalharem na mesma sala.
   - [x] Detectar e resolver conflitos e erros o mais rápido possível.
   - [ ] Aumentar o tempo de entrega do projeto.
   > **Explicação**: CI automatiza a verificação de cada alteração enviada ao repositório.

6. O que acontece se a etapa de "Testes" falhar em um Pipeline de CI?
   - [ ] O código é enviado para produção do mesmo jeito.
   - [x] O pipeline é interrompido e os desenvolvedores são notificados da falha.
   - [ ] O Git deleta o repositório automaticamente.
   - [ ] Nada, os testes são opcionais.
   > **Explicação**: O objetivo do CI é impedir que códigos quebrados avancem no ciclo.

7. Qual arquivo é comumente usado para configurar o GitHub Actions?
   - [ ] index.html
   - [ ] main.py
   - [x] Um arquivo .yml na pasta .github/workflows.
   - [ ] config.txt
   > **Explicação**: Arquivos YAML (YAML Ain't Markup Language) são o padrão para configurações de pipelines.

8. O comando `git push` serve para:
   - [ ] Trazer as mudanças do servidor para o seu PC.
   - [x] Enviar seus commits locais para um repositório remoto (ex: GitHub).
   - [ ] Pedir pizza para o time.
   - [ ] Resetar a senha do Windows.
   > **Explicação**: Push (empurrar) sincroniza seu trabalho local com o servidor compartilhado.

9. Quando ocorre um "Merge Conflict" no Git?
   - [ ] Quando dois desenvolvedores brigam na reunião.
   - [x] Quando dois commits alteram a mesma linha do mesmo arquivo de forma contraditória.
   - [ ] Quando o HD do servidor está cheio.
   - [ ] Quando o código está escrito em duas linguagens diferentes.
   > **Explicação**: Conflitos exigem intervenção humana para decidir qual versão do código prevalecerá.

10. A prática de "Shift Left" em CI/CD prega que:
    - [ ] Devemos mover as mesas para a esquerda.
    - [x] Os testes devem começar o mais cedo possível no ciclo de desenvolvimento.
    - [ ] Só devemos testar no final do projeto.
    - [ ] Os desenvolvedores devem digitar apenas com a mão esquerda.
    > **Explicação**: Testar cedo reduz custos e aumenta a qualidade final.
