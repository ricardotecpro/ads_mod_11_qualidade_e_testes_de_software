# Quiz 04 - Estrutura App Android 🏗️

1. Qual a função do arquivo `AndroidManifest.xml`?
    - [ ] Guardar as senhas dos usuários
    - [x] Definir componentes básicos, permissões e metadados do app
    - [ ] Traduzir o app para outros idiomas
    - [ ] Gerar as cores do layout
    *Explicação: É o arquivo de configuração central onde o Android "descobre" o que o seu app faz.*

2. Em qual método do Ciclo de Vida da Activity devemos configurar o layout?
    - [ ] onStart()
    - [x] onCreate()
    - [ ] onResume()
    - [ ] onDestroy()
    *Explicação: O onCreate é chamado assim que a Activity nasce, sendo o local ideal para o setContentView.*

3. O que acontece quando o usuário recebe uma ligação e a Activity sai da frente dele?
    - [ ] Ela é destruída imediatamente
    - [x] Ela entra no estado onPause() e depois onStop()
    - [ ] Ela continua rodando em segundo plano sem gastar bateria
    - [ ] O app fecha sozinho
    *Explicação: A Activity fica "congelada" em background, aguardando o retorno do usuário.*

4. Para que serve a pasta `res/layout`?
    - [ ] Para guardar fotos da galeria
    - [x] Para armazenar os arquivos XML de interface (telas)
    - [ ] Para salvar o banco de dados
    - [ ] Para guardar o código Kotlin
    *Explicação: Nela ficam as definições visuais de como os botões e textos são organizados.*

5. Qual a vantagem de usar `Strings.xml` em vez de texto fixo no código?
    - [ ] O app fica mais rápido
    - [x] Facilita a tradução (internacionalização) e manutenção do app
    - [ ] O Google exige para publicar na loja
    - [ ] Os hackers não conseguem ler as mensagens
    *Explicação: Centralizar textos permite traduzir o app para outros idiomas apenas criando novos arquivos de valores.*

6. O que é o `ViewBinding`?
    - [ ] Uma forma de colar o celular na parede
    - [x] Um recurso que gera uma classe para acessar as Views do XML de forma segura e rápida
    - [ ] Um site para baixar ícones grátis
    - [ ] O nome do motor gráfico do Android
    *Explicação: Ele substitui o antigo findViewById, evitando erros de "null" e tipagem incorreta.*

7. O que representa o estado `onResume()`?
    - [ ] O app está carregando os dados
    - [x] O usuário está interagindo com a tela (foco ativo)
    - [ ] O app foi desinstalado
    - [ ] O celular está em modo avião
    *Explicação: É o ponto onde o app está 100% pronto para receber toques e comandos do usuário.*

8. Qual componente do iOS é equivalente à Activity do Android?
    - [ ] Podfile
    - [x] UIViewController
    - [ ] AppDelegate
    - [ ] Storyboard
    *Explicação: Ambos são responsáveis por gerenciar o ciclo de vida e a interação de uma tela específica.*

9. Qual o comportamento do Android quando o sistema fica sem memória?
    - [ ] Ele desliga o celular
    - [x] Ele pode matar Activities que estão em background (Stop) para liberar RAM
    - [ ] Ele apaga as fotos do usuário
    - [ ] Ele pede permissão para fechar o app
    *Explicação: O gerenciador de processos do Android prioriza o app que o usuário está vendo no momento.*

10. O que significa a pasta `res/drawable`?
    - [ ] Onde guardamos os rascunhos do projeto
    - [x] Onde ficam os recursos gráficos (imagens, ícones, formas XML)
    - [ ] Onde salvamos as músicas do app
    - [ ] Onde o código Java é compilado
    *Explicação: É o repositório central de ativos visuais do aplicativo.*