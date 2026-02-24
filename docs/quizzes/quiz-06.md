# Quiz 06 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que é o Git?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma rede social para desenvolvedores.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Um sistema de controle de versão distribuído.">Um sistema de controle de versão distribuído.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma linguagem de programação de alto desempenho.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Um provedor de internet.
   > **Explicação**: Git permite rastrear mudanças no código e colaborar com outros desenvolvedores.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. O que faz o comando `git commit`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Envia o código para o servidor remoto.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Salva as alterações no repositório local com uma mensagem descritiva.">Salva as alterações no repositório local com uma mensagem descritiva.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Apaga todas as mudanças feitas no dia.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Cria uma conta no GitHub.
   > **Explicação**: O commit cria um "ponto de restauração" histórico no seu repositório local.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual a função de uma "Branch" (Ramo) no Git?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Desligar o computador do colega.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Criar uma linha de desenvolvimento isolada da principal.">Criar uma linha de desenvolvimento isolada da principal.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Deletar arquivos duplicados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Traduzir o código para português.
   > **Explicação**: Branches permitem trabalhar em novas features sem afetar o código estável (`main`).</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. No contexto do GitHub Actions, o que é um "Workflow"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A mesa de trabalho do desenvolvedor.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Um processo automatizado configurado no repositório (ex: para rodar testes).">Um processo automatizado configurado no repositório (ex: para rodar testes).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Uma lista de bugs pendentes.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O manual de marca da empresa.
   > **Explicação**: Workflows automatizam tarefas como build, teste e deploy.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. A Integração Contínua (CI) tem como objetivo:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Integrar o software com as redes sociais.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Forçar todos os desenvolvedores a trabalharem na mesma sala.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Detectar e resolver conflitos e erros o mais rápido possível.">Detectar e resolver conflitos e erros o mais rápido possível.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Aumentar o tempo de entrega do projeto.
   > **Explicação**: CI automatiza a verificação de cada alteração enviada ao repositório.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O que acontece se a etapa de "Testes" falhar em um Pipeline de CI?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O código é enviado para produção do mesmo jeito.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O pipeline é interrompido e os desenvolvedores são notificados da falha.">O pipeline é interrompido e os desenvolvedores são notificados da falha.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O Git deleta o repositório automaticamente.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Nada, os testes são opcionais.
   > **Explicação**: O objetivo do CI é impedir que códigos quebrados avancem no ciclo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Qual arquivo é comumente usado para configurar o GitHub Actions?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">index.html</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">main.py</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Um arquivo .yml na pasta .github/workflows.">Um arquivo .yml na pasta .github/workflows.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">config.txt
   > **Explicação**: Arquivos YAML (YAML Ain't Markup Language) são o padrão para configurações de pipelines.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O comando `git push` serve para:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Trazer as mudanças do servidor para o seu PC.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Enviar seus commits locais para um repositório remoto (ex: GitHub).">Enviar seus commits locais para um repositório remoto (ex: GitHub).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Pedir pizza para o time.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Resetar a senha do Windows.
   > **Explicação**: Push (empurrar) sincroniza seu trabalho local com o servidor compartilhado.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Quando ocorre um "Merge Conflict" no Git?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Quando dois desenvolvedores brigam na reunião.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Quando dois commits alteram a mesma linha do mesmo arquivo de forma contraditória.">Quando dois commits alteram a mesma linha do mesmo arquivo de forma contraditória.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Quando o HD do servidor está cheio.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Quando o código está escrito em duas linguagens diferentes.
   > **Explicação**: Conflitos exigem intervenção humana para decidir qual versão do código prevalecerá.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. A prática de "Shift Left" em CI/CD prega que:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Devemos mover as mesas para a esquerda.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Os testes devem começar o mais cedo possível no ciclo de desenvolvimento.">Os testes devem começar o mais cedo possível no ciclo de desenvolvimento.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Só devemos testar no final do projeto.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Os desenvolvedores devem digitar apenas com a mão esquerda.
    > **Explicação**: Testar cedo reduz custos e aumenta a qualidade final.</div>
  <div class="quiz-feedback"></div>
</div>

