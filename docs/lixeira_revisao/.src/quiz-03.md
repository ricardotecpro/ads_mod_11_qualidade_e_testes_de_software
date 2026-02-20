# Quiz 03 - Modelagem de APIs RESTful 📡

1. O que significa o termo "Stateless" no REST?
    - [ ] O servidor armazena o estado do cliente em variáveis globais
    - [x] O servidor não guarda informações sobre sessões anteriores; cada requisição é independente
    - [ ] O app não precisa de internet para funcionar
    - [ ] O banco de dados nunca muda
    *Explicação: Stateless garante que o servidor possa escalar horizontalmente sem se preocupar em sincronizar sessões de usuários entre máquinas.*

2. Qual a regra de ouro para nomear URIs no REST?
    - [ ] Usar verbos de ação (ex: /getUsers)
    - [ ] Usar letras maiúsculas para destacar
    - [x] Usar substantivos no plural (ex: /usuarios)
    - [ ] Colocar a senha do usuário na URL
    *Explicação: URIs devem representar recursos (coisas), e não ações. A ação é definida pelo Verbo HTTP.*

3. Qual verbo HTTP deve ser usado para criar um novo recurso?
    - [ ] GET
    - [x] POST
    - [ ] PUT
    - [ ] DELETE
    *Explicação: O POST é o método padrão para submeter dados para a criação de novos recursos no servidor.*

4. Qual a diferença fundamental entre PUT e PATCH?
    - [ ] PUT é mais rápido que PATCH
    - [ ] PATCH remove o recurso e PUT cria um novo
    - [x] PUT substitui o recurso inteiro, enquanto PATCH faz atualizações parciais
    - [ ] Não há diferença, ambos fazem a mesma coisa
    *Explicação: Use PUT para "trocar" o objeto todo e PATCH para mudar apenas um campo (ex: mudar apenas o preço de um produto).*

5. Qual código de status indica que um recurso foi criado com sucesso?
    - [ ] 200 OK
    - [x] 201 Created
    - [ ] 204 No Content
    - [ ] 404 Not Found
    *Explicação: O 201 é específico para sinalizar que o POST resultou na criação física de um novo elemento.*

6. O que significa ser um método "Idempotente"?
    - [ ] Que ele gasta muita energia
    - [x] Que múltiplas requisições idênticas têm o mesmo efeito que uma só
    - [ ] Que ele só funciona com números inteiros
    - [ ] Que ele apaga o banco de dados
    *Explicação: GET, PUT e DELETE são idempotentes. Se você deletar o mesmo ID 10 vezes, o resultado final (o recurso não existir) é o mesmo.*

7. Por que o JSON é preferido em relação ao XML em APIs modernas?
    - [ ] Porque ele é colorido
    - [x] Porque é mais leve, menos verboso e mais fácil de ler/processar em JS
    - [ ] Porque o XML foi proibido pelo Google
    - [ ] Porque JSON aceita emojis e XML não
    *Explicação: O JSON tem uma sintaxe muito mais limpa e mapeia quase diretamente para objetos em linguagens modernas.*

8. O que o status code 403 Forbidden indica?
    - [ ] Que a página não existe
    - [ ] Que o usuário não está logado
    - [x] Que o usuário está logado, mas não tem permissão para aquele recurso
    - [ ] Que o servidor explodiu
    *Explicação: Diferente do 401 (sem login), o 403 diz que você é conhecido, mas "não tem entrada permitida aqui".*

9. Em REST, o que compõe uma Interface Uniforme?
    - [ ] Usar a mesma cor em todos os botões
    - [x] Uso de URIs para recursos, métodos HTTP padrão e representações de dados (JSON/XML)
    - [ ] Ter apenas um arquivo de código para tudo
    - [ ] Usar apenas um tipo de fonte de texto
    *Explicação: É o conjunto de regras que torna a API previsível e fácil de aprender por outros desenvolvedores.*

10. Qual a função do cabeçalho "Content-Type" em uma requisição?
    - [ ] Dizer o nome do autor da API
    - [x] Informar ao servidor qual o formato dos dados que estão sendo enviados (ex: application/json)
    - [ ] Aumentar a segurança da senha
    - [ ] Definir a cor de fundo do site
    *Explicação: Sem o Content-Type, o servidor pode não saber como interpretar o corpo (body) da mensagem recebida.*
