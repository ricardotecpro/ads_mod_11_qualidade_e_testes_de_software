# Quiz 01 - Introdução

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que melhor define a qualidade de software?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A ausência total de bugs no código.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O grau em que um sistema satisfaz os requisitos especificados e as necessidades do usuário.">O grau em que um sistema satisfaz os requisitos especificados e as necessidades do usuário.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">A rapidez com que o desenvolvedor entrega a funcionalidade.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O uso das ferramentas mais modernas do mercado.
   > **Explicação**: Qualidade é a conformidade com requisitos e adequação ao uso, não apenas a falta de erros técnicos.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual a principal diferença entre erro e defeito?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Erro é uma ação humana; Defeito é a presença de uma imperfeição no artefato.">Erro é uma ação humana; Defeito é a presença de uma imperfeição no artefato.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Defeito é uma ação humana; Erro é o que o usuário vê.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Não há diferença, são sinônimos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Erro ocorre em produção; Defeito ocorre em desenvolvimento.
   > **Explicação**: Erros são cometidos por pessoas (equívocos), que geram defeitos (bugs) escondidos no código.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Quando um defeito se torna uma falha?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Assim que o código é salvo no repositório.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Quando o desenvolvedor lê o código e percebe o erro.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Quando o defeito é executado e o sistema apresenta um comportamento inesperado.">Quando o defeito é executado e o sistema apresenta um comportamento inesperado.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Quando o cliente cancela o contrato.
   > **Explicação**: A falha é a manifestação visível do defeito durante a execução do software.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. A atividade de "Verificação" foca em:</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Garantir que o produto está sendo construído corretamente segundo os processos.">Garantir que o produto está sendo construído corretamente segundo os processos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Garantir que o produto final atende ao que o cliente pediu.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Corrigir bugs em produção.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Escrever casos de teste automatizados.
   > **Explicação**: Verificação olha para o processo ("estamos construindo certo?"), enquanto validação olha para o produto ("fizemos o que foi pedido?").</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual fase foca em "estamos construindo o produto correto"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Verificação.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Validação.">Validação.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Depuração (Debug).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Compilação.
   > **Explicação**: Validação é o confronto do produto final contra as necessidades reais do usuário.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. O papel do QA na equipe moderna é:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Ser o "policial" que impede o lançamento do software.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O único responsável pela qualidade de todo o sistema.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Agir como um facilitador da qualidade, integrando-se ao time para prevenir erros.">Agir como um facilitador da qualidade, integrando-se ao time para prevenir erros.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Apenas documentar o que os desenvolvedores fazem.
   > **Explicação**: O QA moderno (Agile Testing) trabalha preventivamente e compartilha a responsabilidade pela qualidade com todo o time.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Qual o maior impacto de um bug encontrado apenas em produção?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Nenhum, basta corrigir e dar deploy.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">O desenvolvedor ganha uma advertência.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Custo de correção muito superior ao de bugs encontrados no início, além de danos à imagem.">Custo de correção muito superior ao de bugs encontrados no início, além de danos à imagem.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Aumento na cobertura de testes.
   > **Explicação**: Quanto mais tarde um bug é encontrado, mais caro e arriscado é corrigi-lo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Segundo a ISO/IEC 25010, qual característica foca na facilidade de uso?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Eficiência de desempenho.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Manutenibilidade.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Usabilidade.">Usabilidade.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Portabilidade.
   > **Explicação**: Usabilidade é a característica que mede o esforço necessário para usar o software.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Inspeções de código e revisões de documentos são exemplos de:</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Teste Dinâmico.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Teste Estático (Verificação).">Teste Estático (Verificação).</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Teste de Aceitação.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Teste de Stress.
   > **Explicação**: Testes estáticos não exigem a execução do código; eles analisam os artefatos diretamente.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. A qualidade de software deve ser uma preocupação de quem?</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Apenas do testador.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Apenas do Gerente de Projetos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="Incorreto. Tente novamente.">Apenas do cliente.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! De todos os envolvidos no ciclo de vida do desenvolvimento.
    > **Explicação**: Qualidade é uma responsabilidade coletiva (Whole Team Approach).">De todos os envolvidos no ciclo de vida do desenvolvimento.
    > **Explicação**: Qualidade é uma responsabilidade coletiva (Whole Team Approach).</div>
  <div class="quiz-feedback"></div>
</div>

