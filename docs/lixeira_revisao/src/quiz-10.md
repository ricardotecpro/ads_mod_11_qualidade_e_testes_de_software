# Quiz 10 - APIs REST & Retrofit 🌍

1. O que significa a sigla REST?
    - [ ] Remote Execution System
    - [x] Representational State Transfer
    - [ ] React State Type
    - [ ] Reset Server Timer
    *Explicação: REST é um estilo de arquitetura para sistemas distribuídos que usam o protocolo HTTP.*

2. Qual biblioteca é o padrão da indústria para realizar requisições HTTP no Android Nativo?
    - [ ] Volley (legado)
    - [x] Retrofit (da Square)
    - [ ] HttpUrlConnection (nativo)
    - [ ] Fetch
    *Explicação: O Retrofit simplifica a criação de clientes HTTP transformando a API em uma interface Kotlin.*

3. Qual formato de dados é quase onipresente em APIs REST modernas para troca de informações?
    - [ ] XML
    - [x] JSON (JavaScript Object Notation)
    - [ ] CSV
    - [ ] Properties
    *Explicação: O JSON é leve, fácil de ler para humanos e máquinas, sendo o padrão ouro hoje.*

4. O que faz um "Converter Factory" (como o GsonConverterFactory) no Retrofit?
    - [ ] Converte o celular em um servidor.
    - [x] Transforma automaticamente o JSON recebido da internet em objetos Kotlin (Data Classes).
    - [ ] Traduz o app para inglês.
    - [ ] Converte imagens para texto.
    *Explicação: O conversor automatiza a parte chata de "parsear" o texto do JSON manualmente.*

5. Qual anotação define uma requisição do tipo "Obter Dados"?
    - [x] @GET("endpoint")
    - [ ] @FETCH("endpoint")
    - [ ] @RECEIVE("endpoint")
    - [ ] @DOWNLOAD("endpoint")
    *Explicação: @GET mapeia para o método GET do protocolo HTTP.*

6. Por que usamos a palavra-chave `suspend` em funções do Retrofit no Kotlin?
    - [ ] Para parar a internet do usuário.
    - [x] Para que a requisição seja assíncrona e não trave a interface (UI) do aplicativo.
    - [ ] Para aumentar a segurança do código.
    - [ ] É apenas opcional.
    *Explicação: Funções `suspend` trabalham com Coroutines, permitindo esperar a rede sem congelar a tela.*

7. Para que serve o arquivo "AndroidManifest.xml" no contexto de redes?
    - [ ] Para salvar a senha do Wi-Fi.
    - [x] Para declarar a permissão `android.permission.INTERNET`, obrigatória para o app acessar a web.
    - [ ] Para guardar o link da API.
    - [ ] Para nada, o Android libera internet automaticamente.
    *Explicação: Sem essa permissão, o app crasha imediatamente ao tentar uma conexão externa.*

8. O que é um "Interceptor" no OkHttp (usado pelo Retrofit)?
    - [ ] Um hacker que rouba dados.
    - [x] Um componente que permite interceptar e modificar todas as requisições (ex: adicionar um Token de Login no Header).
    - [ ] Um comando de pausa.
    - [ ] O firewall do Android.
    *Explicação: Interceptors são ótimos para centralizar a lógica de autenticação.*

9. O que representa o código de status HTTP "401 Unauthorized"?
    - [ ] Página não encontrada.
    - [x] Falha na autenticação (Token inválido ou usuário não logado).
    - [ ] Erro interno no servidor.
    - [ ] Requisição feita com sucesso.
    *Explicação: Códigos 4xx indicam erro do lado do cliente (App).*

10. No iOS, qual seria a biblioteca de terceiros mais popular comparável ao Retrofit?
    - [ ] CoreData
    - [ ] SwiftUI
    - [x] Alamofire
    - [ ] CocoaPods
    *Explicação: Embora o iOS tenha o `URLSession` muito bom, o Alamofire é a biblioteca externa mais usada para facilitar o HTTP.*
