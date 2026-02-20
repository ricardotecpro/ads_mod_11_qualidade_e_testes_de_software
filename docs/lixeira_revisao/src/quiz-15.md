# Quiz 15 - Publicação e Google Play Store 🚀

1. Qual a principal diferença entre o arquivo .apk e o .aab (Android App Bundle)?
    - [ ] .aab é apenas para iOS.
    - [x] .aab permite que o Google Play gere APKs otimizados para cada dispositivo, diminuindo o tamanho do download.
    - [ ] .apk é mais moderno e seguro.
    - [ ] Não há diferença, são apenas nomes.
    *Explicação: O App Bundle é o formato obrigatório hoje pois economiza espaço no celular do usuário.*

2. Para que serve a "Keystore" (Chave de Assinatura) no Android?
    - [ ] Para abrir o prédio do Google.
    - [x] Para assinar digitalmente o app, garantindo que as atualizações venham do mesmo desenvolvedor original.
    - [ ] Para criptografar o banco de dados.
    - [ ] Para baixar o Android Studio.
    *Explicação: Sem a mesma chave original, você perde o controle sobre as atualizações do seu app na loja.*

3. Qual o custo da taxa única para criar uma conta de desenvolvedor no Google Play Console?
    - [ ] $99 por ano.
    - [ ] É gratuito para estudantes.
    - [x] $25 (taxa única vitalícia).
    - [ ] $10 por mês.
    *Explicação: Diferente da Apple, o Google cobra apenas uma vez para você publicar quantos apps quiser.*

4. O que é o ProGuard/R8 no processo de build?
    - [ ] Um antivírus para o celular.
    - [x] Uma ferramenta de ofuscação e encolhimento de código (torna o código difícil de ler por piratas e diminui o tamanho do app).
    - [ ] Um plugin para mudar o tema do editor.
    - [ ] O sistema de GPS.
    *Explicação: O R8 remove código morto e renomeia classes para nomes curtos (a, b, c), protegendo a propriedade intelectual.*

5. Qual o papel do "Feature Graphic" (Arte de Destaque) na loja?
    - [ ] É o ícone do app.
    - [ ] É uma foto do desenvolvedor.
    - [x] É uma imagem promocional grande (1024x500) que aparece no topo da página do app para atrair usuários.
    - [ ] É o código fonte do aplicativo.
    *Explicação: Marketing visual é essencial para converter visitantes em downloads.*

6. Para que serve o "Canal de Teste Interno"?
    - [ ] Para ganhar dinheiro antes do lançamento.
    - [x] Para distribuir o app rapidamente para até 100 pessoas da sua equipe sem passar por uma revisão longa.
    - [ ] Para o app ficar escondido do Google.
    - [ ] Para rodar o app apenas no Wi-Fi.
    *Explicação: É a forma mais rápida de validar o app com colegas antes de abrir para o mundo.*

7. Na configuração do `build.gradle`, o que deve ser incrementado SEMPRE que você for enviar uma nova atualização para a loja?
    - [ ] applicationId
    - [ ] minSdkVersion
    - [x] versionCode (número inteiro)
    - [ ] compileSdk
    *Explicação: O Google Play não aceita dois pacotes com o mesmo versionCode.*

8. O que acontece durante o processo de "Revisão" do app pela equipe do Google?
    - [ ] Eles jogam seu jogo até o final.
    - [x] Verificam se o app segue as políticas de segurança, privacidade e se não contém vírus ou spam.
    - [ ] Eles reescrevem seu código.
    - [ ] Eles mudam suas cores.
    *Explicação: A revisão garante a qualidade e segurança da loja oficial.*

9. Qual é o equivalente ao Google Play Console no ecossistema Apple (iOS)?
    - [ ] App Store Reader
    - [x] App Store Connect (antigo iTunes Connect)
    - [ ] Xcode Cloud
    - [ ] Swift Dashboard
    *Explicação: É através do App Store Connect que os desenvolvedores iOS gerenciam seus apps e vendas.*

10. O que significa o termo "SEO" (ou ASO - App Store Optimization) para aplicativos?
    - [ ] Aumentar o brilho da tela.
    - [x] Otimizar o título, palavras-chave e descrição para que seu app apareça nos primeiros lugares das buscas da loja.
    - [ ] Diminuir o consumo de bateria.
    - [ ] Mudar o ícone toda semana.
    *Explicação: ASO é o "marketing de busca" dentro das lojas de aplicativos.*
