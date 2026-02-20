# Quiz 08 - Persistência de Dados (Room) 💾

1. Para que servem as "SharedPreferences" no Android?
    - [ ] Salvar fotos em alta resolução.
    - [x] Salvar pequenas configurações do tipo chave-valor (ex: nome, tema).
    - [ ] Criar um banco de dados relacional complexo.
    - [ ] Enviar arquivos para a nuvem.
    *Explicação: SharedPreferences são ideais para dados simples e rápidos que não precisam de uma estrutura de tabela.*

2. O que é a biblioteca "Room"?
    - [ ] Um editor de fotos do Google.
    - [x] Uma camada de abstração sobre o SQLite que facilita o uso de bancos de dados no Android.
    - [ ] Um framework para animações de interface.
    - [ ] Uma ferramenta de chat interno.
    *Explicação: O Room faz parte do Jetpack e transforma tabelas em classes Kotlin de forma segura.*

3. Na arquitetura do Room, o que representa uma classe anotada com `@Entity`?
    - [ ] Uma conexão de rede.
    - [x] Uma tabela no banco de dados.
    - [ ] Um botão na tela.
    - [ ] Uma permissão do sistema.
    *Explicação: Cada entidade (Entity) corresponde a uma linha na sua tabela do banco de dados.*

4. Qual a função do "DAO" (Data Access Object) no Room?
    - [ ] Definir as cores do app.
    - [ ] Navegar entre as telas.
    - [x] Definir os métodos de acesso aos dados (Insert, Query, Update, Delete).
    - [ ] Gerenciar o GPS.
    *Explicação: O DAO é a interface onde escrevemos os comandos SQL ou anotações para manipular o banco.*

5. Por que é proibido acessar o banco de dados na "Thread Principal" (Main Thread)?
    - [ ] Porque o Google cobra por acesso.
    - [x] Porque operações de disco são lentas e podem travar a interface do usuário (ANR).
    - [ ] Porque o banco de dados só funciona offline.
    - [ ] Porque o código fica muito feio.
    *Explicação: O Android bloqueia por padrão acessos pesados na Thread de UI para manter o app fluido.*

6. Qual anotação define uma chave primária autoincrementável no Room?
    - [ ] @Key
    - [x] @PrimaryKey(autoGenerate = true)
    - [ ] @IdField
    - [ ] @MainKey
    *Explicação: Chaves primárias garantem que cada registro seja único no banco.*

7. Como o Room avisa a UI que um dado mudou no banco de dados de forma automática?
    - [ ] Através de um sinal de fumaça.
    - [ ] Reiniciando o aplicativo.
    - [x] Retornando um `LiveData` ou `Flow` no método do DAO.
    - [ ] Enviando uma notificação push.
    *Explicação: Ao retornar LiveData no DAO, o banco "assina" as mudanças para a View.*

8. O que faz a classe anotada com `@Database`?
    - [ ] Cria a interface gráfica.
    - [ ] Salva as fotos na galeria.
    - [x] Atua como o ponto de entrada principal para a conexão com o banco SQLite.
    - [ ] Define as permissões de internet.
    *Explicação: A classe Database mantém as instâncias dos DAOs e a versão do banco.*

9. Imagine que você salvou o nome "João" nas SharedPreferences. Se o usuário limpar o cache do app nas configurações do Android, o que acontece?
    - [ ] O dado continua lá.
    - [x] O dado é removido, pois SharedPreferences fazem parte dos dados privados do app.
    - [ ] O celular formata sozinho.
    - [ ] O app para de funcionar.
    *Explicação: Limpar dados do app remove SharedPreferences e bancos de dados locais.*

10. No iOS, qual o banco de dados nativo comparável ao Room?
    - [ ] Firebase
    - [ ] UserDefaults
    - [x] Core Data (ou SwiftData)
    - [ ] CloudKit
    *Explicação: Core Data é o framework de persistência robusto da Apple para dados estruturados.*
