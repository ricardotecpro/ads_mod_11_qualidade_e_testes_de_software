# Quiz 10 - Consumindo API REST (Retrofit) 🌍

1. O que é o JSON (JavaScript Object Notation)?
    - [ ] Uma nova linguagem de programação
    - [x] Um formato leve de troca de dados entre sistemas, baseado em chave-valor
    - [ ] O nome do criador do Android
    - [ ] Um tipo de imagem de alta qualidade
    *Explicação: JSON é o padrão universal para APIs REST hoje em dia.*

2. Qual a função da biblioteca `Retrofit`?
    - [ ] Editar fotos e vídeos
    - [x] Facilitar o consumo de APIs REST, transformando rotas HTTP em interfaces Kotlin
    - [ ] Aumentar a velocidade do Wi-Fi
    - [ ] Limpar o cache do celular
    *Explicação: O Retrofit abstrai toda a complexidade de fazer requisições de rede manualmente.*

3. Para que serve o `Converter Factory` (ex: GsonConverterFactory)?
    - [ ] Para converter o app em um site
    - [x] Para transformar automaticamente o texto JSON recebido em objetos Kotlin (Data Classes)
    - [ ] Para traduzir o código de Java para Kotlin
    - [ ] Para mudar o fuso horário do app
    *Explicação: Sem o conversor, você teria que processar o texto do JSON campo por campo manualmente.*

4. O que a anotação `@GET("users")` faz na interface do Retrofit?
    - [ ] Baixa o app da rede social
    - [x] Define que aquele método fará uma requisição HTTP do tipo GET na rota "/users"
    - [ ] Apaga todos os usuários do banco
    - [ ] Envia uma mensagem para o suporte
    *Explicação: As anotações mapeiam as funções do código para os endereços (endpoints) da API.*

5. Qual a permissão obrigatória no `AndroidManifest.xml` para acessar APIs?
    - [ ] android.permission.CAMERA
    - [x] android.permission.INTERNET
    - [ ] android.permission.GPS
    - [ ] android.permission.CALL_PHONE
    *Explicação: Sem essa permissão, o sistema operacional bloqueia qualquer tentativa de conexão externa do app.*

6. O que acontece se o JSON trouxer um campo `id` e sua Data Class não tiver esse campo?
    - [ ] O app crasha imediatamente
    - [x] O Retrofit ignora o campo e continua o processamento normalmente
    - [ ] O celular reinicia
    - [ ] O Google Play remove o seu app
    *Explicação: Você só precisa mapear os campos que realmente pretende usar no seu código.*

7. O que é um `Endpoint` em uma API?
    - [ ] O fim da bateria do celular
    - [x] A URL específica que representa um recurso (ex: /perfil, /produtos)
    - [ ] O botão de desligar o app
    - [ ] O nome do servidor da empresa
    *Explicação: Cada endpoint é como um "endereço" para um pedido específico.*

8. Para que serve o `viewModelScope.launch` ao chamar uma API?
    - [ ] Para rodar a chamada na thread principal e travar a tela
    - [x] Para iniciar uma coroutine que gerencia a chamada de rede de forma assíncrona
    - [ ] Para aumentar o volume do som
    - [ ] Para tirar um print automático
    *Explicação: Chamadas de rede demoram e não podem bloquear a interface do usuário.*

9. O que é um `Bearer Token`?
    - [ ] Um tipo de urso de pelúcia
    - [x] Uma forma de autenticação onde um código (token) é enviado no cabeçalho da requisição
    - [ ] O nome do servidor da Google
    - [ ] Um comando para formatar o celular
    *Explicação: É usado para provar à API que o usuário está logado e tem permissão.*

10. Como o Retrofit lida com erros de rede (ex: falta de internet)?
    - [ ] Ele resolve o problema sozinho e conecta o Wi-Fi
    - [x] Ele lança uma exceção que você deve capturar usando `try/catch`
    - [ ] Ele fecha o app sem avisar
    - [ ] Ele manda um SMS para o desenvolvedor
    *Explicação: O tratamento de erros de conexão é responsabilidade do desenvolvedor para garantir uma boa UX.*