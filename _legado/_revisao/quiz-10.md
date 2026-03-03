# Quiz 10 - APIs REST & Retrofit 🌍

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que significa a sigla REST?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. REST é um estilo de arquitetura para sistemas distribuídos que usam o protocolo HTTP.">Remote Execution System</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! REST é um estilo de arquitetura para sistemas distribuídos que usam o protocolo HTTP.">Representational State Transfer</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. REST é um estilo de arquitetura para sistemas distribuídos que usam o protocolo HTTP.">React State Type</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. REST é um estilo de arquitetura para sistemas distribuídos que usam o protocolo HTTP.">Reset Server Timer</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual biblioteca é o padrão da indústria para realizar requisições HTTP no Android Nativo?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Retrofit simplifica a criação de clientes HTTP transformando a API em uma interface Kotlin.">Volley (legado)</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Retrofit simplifica a criação de clientes HTTP transformando a API em uma interface Kotlin.">Retrofit (da Square)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Retrofit simplifica a criação de clientes HTTP transformando a API em uma interface Kotlin.">HttpUrlConnection (nativo)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Retrofit simplifica a criação de clientes HTTP transformando a API em uma interface Kotlin.">Fetch</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual formato de dados é quase onipresente em APIs REST modernas para troca de informações?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O JSON é leve, fácil de ler para humanos e máquinas, sendo o padrão ouro hoje.">XML</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O JSON é leve, fácil de ler para humanos e máquinas, sendo o padrão ouro hoje.">JSON (JavaScript Object Notation)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O JSON é leve, fácil de ler para humanos e máquinas, sendo o padrão ouro hoje.">CSV</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O JSON é leve, fácil de ler para humanos e máquinas, sendo o padrão ouro hoje.">Properties</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. O que faz um "Converter Factory" (como o GsonConverterFactory) no Retrofit?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O conversor automatiza a parte chata de "parsear" o texto do JSON manualmente.">Converte o celular em um servidor.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O conversor automatiza a parte chata de "parsear" o texto do JSON manualmente.">Transforma automaticamente o JSON recebido da internet em objetos Kotlin (Data Classes).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O conversor automatiza a parte chata de "parsear" o texto do JSON manualmente.">Traduz o app para inglês.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O conversor automatiza a parte chata de "parsear" o texto do JSON manualmente.">Converte imagens para texto.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Qual anotação define uma requisição do tipo "Obter Dados"?</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! @GET mapeia para o método GET do protocolo HTTP.">@GET("endpoint")</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. @GET mapeia para o método GET do protocolo HTTP.">@FETCH("endpoint")</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. @GET mapeia para o método GET do protocolo HTTP.">@RECEIVE("endpoint")</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. @GET mapeia para o método GET do protocolo HTTP.">@DOWNLOAD("endpoint")</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Por que usamos a palavra-chave `suspend` em funções do Retrofit no Kotlin?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Funções `suspend` trabalham com Coroutines, permitindo esperar a rede sem congelar a tela.">Para parar a internet do usuário.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Funções `suspend` trabalham com Coroutines, permitindo esperar a rede sem congelar a tela.">Para que a requisição seja assíncrona e não trave a interface (UI) do aplicativo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Funções `suspend` trabalham com Coroutines, permitindo esperar a rede sem congelar a tela.">Para aumentar a segurança do código.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Funções `suspend` trabalham com Coroutines, permitindo esperar a rede sem congelar a tela.">É apenas opcional.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Para que serve o arquivo "AndroidManifest.xml" no contexto de redes?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem essa permissão, o app crasha imediatamente ao tentar uma conexão externa.">Para salvar a senha do Wi-Fi.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Sem essa permissão, o app crasha imediatamente ao tentar uma conexão externa.">Para declarar a permissão `android.permission.INTERNET`, obrigatória para o app acessar a web.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem essa permissão, o app crasha imediatamente ao tentar uma conexão externa.">Para guardar o link da API.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Sem essa permissão, o app crasha imediatamente ao tentar uma conexão externa.">Para nada, o Android libera internet automaticamente.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que é um "Interceptor" no OkHttp (usado pelo Retrofit)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Interceptors são ótimos para centralizar a lógica de autenticação.">Um hacker que rouba dados.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Interceptors são ótimos para centralizar a lógica de autenticação.">Um componente que permite interceptar e modificar todas as requisições (ex: adicionar um Token de Login no Header).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Interceptors são ótimos para centralizar a lógica de autenticação.">Um comando de pausa.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Interceptors são ótimos para centralizar a lógica de autenticação.">O firewall do Android.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. O que representa o código de status HTTP "401 Unauthorized"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Códigos 4xx indicam erro do lado do cliente (App).">Página não encontrada.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Códigos 4xx indicam erro do lado do cliente (App).">Falha na autenticação (Token inválido ou usuário não logado).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Códigos 4xx indicam erro do lado do cliente (App).">Erro interno no servidor.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Códigos 4xx indicam erro do lado do cliente (App).">Requisição feita com sucesso.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. No iOS, qual seria a biblioteca de terceiros mais popular comparável ao Retrofit?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Embora o iOS tenha o `URLSession` muito bom, o Alamofire é a biblioteca externa mais usada para facilitar o HTTP.">CoreData</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Embora o iOS tenha o `URLSession` muito bom, o Alamofire é a biblioteca externa mais usada para facilitar o HTTP.">SwiftUI</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Embora o iOS tenha o `URLSession` muito bom, o Alamofire é a biblioteca externa mais usada para facilitar o HTTP.">Alamofire</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Embora o iOS tenha o `URLSession` muito bom, o Alamofire é a biblioteca externa mais usada para facilitar o HTTP.">CocoaPods</div>
  <div class="quiz-feedback"></div>
</div>
