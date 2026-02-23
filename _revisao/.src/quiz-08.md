# Quiz 08 - Persistência de Dados 💾

1. Qual a melhor opção para salvar configurações simples do usuário (ex: "Tema Escuro")?
    - [ ] Banco de Dados SQLite
    - [x] SharedPreferences
    - [ ] Pasta de Downloads
    - [ ] Cloud Storage apenas
    *Explicação: SharedPreferences é ideal para pares chave-valor pequenos e persistentes.*

2. O que é o `Room`?
    - [ ] Um chat para desenvolvedores Android
    - [x] Uma biblioteca de persistência que facilita o uso do banco SQLite
    - [ ] O nome da pasta onde ficam as fotos no Android
    - [ ] Um sensor de presença do celular
    *Explicação: O Room é um ORM (Object-Relational Mapping) que mapeia classes Kotlin para tabelas SQL.*

3. Qual a função de um `@DAO` (Data Access Object)?
    - [ ] Desenhar os ícones do app
    - [x] Definir as operações de banco de dados (Insert, Update, Delete, Query)
    - [ ] Controlar o volume do celular
    - [ ] Validar o e-mail do usuário
    *Explicação: O DAO é a interface que contém os métodos para interagir com os dados.*

4. O que representa uma `@Entity` no Room?
    - [ ] Um fantasma do código
    - [x] Uma tabela no banco de dados (geralmente uma data class)
    - [ ] Uma animação de tela
    - [ ] Um tipo de erro de internet
    *Explicação: Cada instância da classeEntity representa uma linha na tabela do banco.*

5. Por que é proibido acessar o banco de dados na `Main Thread` (UI Thread)?
    - [ ] Porque o banco de dados é secreto
    - [x] Porque operações de IO são lentas e podem travar a interface do usuário (ANR)
    - [ ] Porque o Java consome muita bateria
    - [ ] Porque o Google cobra mais caro por isso
    *Explicação: IO de disco pode demorar e, se a thread principal travar por mais de 5s, o Android fecha o app.*

6. O que acontece se você mudar a estrutura do banco e não atualizar a versão?
    - [ ] O app ignora a mudança
    - [x] O app vai crashar ao tentar acessar o banco (IllegalStateException)
    - [ ] O celular apaga o banco de dados sozinho
    - [ ] Nada, o Room resolve tudo magicamente
    *Explicação: Mudar schemas exige uma estratégia de migração ou incremento de versão para o Room saber o que fazer.*

7. Qual a vantagem de usar o Room em vez de SQLite puro?
    - [ ] O app fica mais pesado
    - [x] Verificação de SQL em tempo de compilação e menos código repetitivo
    - [ ] O Room é gratuito e o SQLite é pago
    - [ ] Ele funciona sem internet
    *Explicação: O Room detecta erros de SQL antes de você rodar o app, economizando horas de debug.*

8. O que o termo `@PrimaryKey(autoGenerate = true)` faz?
    - [ ] Cria uma senha aleatória para o usuário
    - [x] Faz com que o banco gere um ID único e sequencial automaticamente
    - [ ] Abre o app sozinho
    - [ ] Criptografa o banco de dados
    *Explicação: Garante que cada item tenha um identificador único sem que você precise cuidar disso.*

9. Qual o equivalente no iOS (Apple) ao banco de dados Room?
    - [ ] iCloud
    - [x] Core Data ou SwiftData
    - [ ] Keychain
    - [ ] FileSystem
    *Explicação: São os frameworks oficiais da Apple para persistência de dados estruturados.*

10. Como recuperamos uma lista de itens do banco que se atualiza sozinha?
    - [ ] Fazendo um `while(true)`
    - [x] Retornando um `LiveData<List<Item>>` ou `Flow` no DAO
    - [ ] Reiniciando a Activity toda hora
    - [ ] Pedindo para o usuário clicar em "Atualizar"
    *Explicação: Quando o banco muda, o LiveData notifica a View automaticamente com a lista nova.*