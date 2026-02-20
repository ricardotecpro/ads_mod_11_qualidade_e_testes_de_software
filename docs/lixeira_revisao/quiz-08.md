# Quiz 08 - Persistência de Dados (Room) 💾

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Para que servem as "SharedPreferences" no Android?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. SharedPreferences são ideais para dados simples e rápidos que não precisam de uma estrutura de tabela.">Salvar fotos em alta resolução.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! SharedPreferences são ideais para dados simples e rápidos que não precisam de uma estrutura de tabela.">Salvar pequenas configurações do tipo chave-valor (ex: nome, tema).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. SharedPreferences são ideais para dados simples e rápidos que não precisam de uma estrutura de tabela.">Criar um banco de dados relacional complexo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. SharedPreferences são ideais para dados simples e rápidos que não precisam de uma estrutura de tabela.">Enviar arquivos para a nuvem.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. O que é a biblioteca "Room"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Room faz parte do Jetpack e transforma tabelas em classes Kotlin de forma segura.">Um editor de fotos do Google.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Room faz parte do Jetpack e transforma tabelas em classes Kotlin de forma segura.">Uma camada de abstração sobre o SQLite que facilita o uso de bancos de dados no Android.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Room faz parte do Jetpack e transforma tabelas em classes Kotlin de forma segura.">Um framework para animações de interface.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Room faz parte do Jetpack e transforma tabelas em classes Kotlin de forma segura.">Uma ferramenta de chat interno.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Na arquitetura do Room, o que representa uma classe anotada com `@Entity`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Cada entidade (Entity) corresponde a uma linha na sua tabela do banco de dados.">Uma conexão de rede.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Cada entidade (Entity) corresponde a uma linha na sua tabela do banco de dados.">Uma tabela no banco de dados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Cada entidade (Entity) corresponde a uma linha na sua tabela do banco de dados.">Um botão na tela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Cada entidade (Entity) corresponde a uma linha na sua tabela do banco de dados.">Uma permissão do sistema.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual a função do "DAO" (Data Access Object) no Room?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O DAO é a interface onde escrevemos os comandos SQL ou anotações para manipular o banco.">Definir as cores do app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O DAO é a interface onde escrevemos os comandos SQL ou anotações para manipular o banco.">Navegar entre as telas.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O DAO é a interface onde escrevemos os comandos SQL ou anotações para manipular o banco.">Definir os métodos de acesso aos dados (Insert, Query, Update, Delete).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O DAO é a interface onde escrevemos os comandos SQL ou anotações para manipular o banco.">Gerenciar o GPS.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Por que é proibido acessar o banco de dados na "Thread Principal" (Main Thread)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Android bloqueia por padrão acessos pesados na Thread de UI para manter o app fluido.">Porque o Google cobra por acesso.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Android bloqueia por padrão acessos pesados na Thread de UI para manter o app fluido.">Porque operações de disco são lentas e podem travar a interface do usuário (ANR).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Android bloqueia por padrão acessos pesados na Thread de UI para manter o app fluido.">Porque o banco de dados só funciona offline.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Android bloqueia por padrão acessos pesados na Thread de UI para manter o app fluido.">Porque o código fica muito feio.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual anotação define uma chave primária autoincrementável no Room?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Chaves primárias garantem que cada registro seja único no banco.">@Key</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Chaves primárias garantem que cada registro seja único no banco.">@PrimaryKey(autoGenerate = true)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Chaves primárias garantem que cada registro seja único no banco.">@IdField</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Chaves primárias garantem que cada registro seja único no banco.">@MainKey</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Como o Room avisa a UI que um dado mudou no banco de dados de forma automática?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ao retornar LiveData no DAO, o banco "assina" as mudanças para a View.">Através de um sinal de fumaça.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ao retornar LiveData no DAO, o banco "assina" as mudanças para a View.">Reiniciando o aplicativo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ao retornar LiveData no DAO, o banco "assina" as mudanças para a View.">Retornando um `LiveData` ou `Flow` no método do DAO.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ao retornar LiveData no DAO, o banco "assina" as mudanças para a View.">Enviando uma notificação push.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que faz a classe anotada com `@Database`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A classe Database mantém as instâncias dos DAOs e a versão do banco.">Cria a interface gráfica.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A classe Database mantém as instâncias dos DAOs e a versão do banco.">Salva as fotos na galeria.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A classe Database mantém as instâncias dos DAOs e a versão do banco.">Atua como o ponto de entrada principal para a conexão com o banco SQLite.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A classe Database mantém as instâncias dos DAOs e a versão do banco.">Define as permissões de internet.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Imagine que você salvou o nome "João" nas SharedPreferences. Se o usuário limpar o cache do app nas configurações do Android, o que acontece?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Limpar dados do app remove SharedPreferences e bancos de dados locais.">O dado continua lá.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Limpar dados do app remove SharedPreferences e bancos de dados locais.">O dado é removido, pois SharedPreferences fazem parte dos dados privados do app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Limpar dados do app remove SharedPreferences e bancos de dados locais.">O celular formata sozinho.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Limpar dados do app remove SharedPreferences e bancos de dados locais.">O app para de funcionar.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. No iOS, qual o banco de dados nativo comparável ao Room?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Core Data é o framework de persistência robusto da Apple para dados estruturados.">Firebase</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Core Data é o framework de persistência robusto da Apple para dados estruturados.">UserDefaults</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Core Data é o framework de persistência robusto da Apple para dados estruturados.">Core Data (ou SwiftData)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Core Data é o framework de persistência robusto da Apple para dados estruturados.">CloudKit</div>
  <div class="quiz-feedback"></div>
</div>
