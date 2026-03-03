# Quiz 04 - Estrutura de um Aplicativo Android 🏗️

1. O que é o arquivo "build.gradle" em um projeto Android?
    - [ ] É onde desenhamos a interface visual.
    - [ ] É o arquivo que contém as fotos do app.
    - [x] É o arquivo de configuração de dependências e automação de build.
    - [ ] É o código fonte principal em Kotlin.
    *Explicação: O Gradle gerencia quais bibliotecas seu app usa e como ele será compilado.*

2. Qual diretório do projeto guarda os "Recursos", como imagens, cores e textos?
    - [ ] java/
    - [ ] manifests/
    - [x] res/
    - [ ] build/
    *Explicação: 'res' vem de Resources. Tudo que não é código fonte (lógica) fica aqui.*

3. O que define a interface visual (layout) de uma tela no Android clássico?
    - [ ] Um arquivo .txt
    - [ ] Um arquivo .jpg
    - [x] Um arquivo .xml
    - [ ] Um arquivo .kt
    *Explicação: Tradicionalmente, o Android usa XML para definir a hierarquia de visualização da tela.*

4. Qual componente do sistema Android representa uma "página" ou tela interativa?
    - [ ] Service
    - [ ] Broadcast Receiver
    - [x] Activity
    - [ ] Intent
    *Explicação: Activities são os blocos fundamentais da UI do Android.*

5. Para que serve a pasta `res/values`?
    - [ ] Para guardar vídeos.
    - [ ] Para salvar o banco de dados.
    - [x] Para guardar arquivos XML de strings, cores e estilos (centralização de constantes).
    - [ ] Para guardar o código Java.
    *Explicação: Centralizar textos e cores facilita a internacionalização e a manutenção do design.*

6. Qual é a função do `ViewBinding`?
    - [ ] Conectar o app ao Wi-Fi.
    - [x] Criar uma referência segura entre o arquivo de layout (XML) e o código Kotlin/Java.
    - [ ] Fazer o download de imagens da internet.
    - [ ] Comprimir o tamanho do app.
    *Explicação: O ViewBinding evita o uso excessivo de `findViewById` e protege contra NullPointerExceptions.*

7. No Gradle, o que significa `minSdkVersion`?
    - [ ] A versão máxima que o app suporta.
    - [x] A versão mínima do sistema Android que o celular deve ter para instalar o app.
    - [ ] O tamanho mínimo em MB do aplicativo.
    - [ ] O número de desenvolvedores no projeto.
    *Explicação: Define a compatibilidade retroativa do seu aplicativo.*

8. O que acontece na pasta `res/drawable`?
    - [ ] Ficam os arquivos de texto salvos pelo usuário.
    - [ ] Ficam as músicas de fundo.
    - [x] Ficam os ícones e imagens vetoriais do app.
    - [ ] Ficam os scripts do banco de dados.
    *Explicação: Desenhos e ícones residem aqui para serem referenciados pelo layout.*

9. O componente `Intent` serve para:
    - [ ] Guardar dados permanentemente no celular.
    - [x] Solicitar uma ação de outro componente (ex: abrir uma nova tela ou a câmera).
    - [ ] Aumentar o brilho da tela.
    - [ ] Compilar o código mais rápido.
    *Explicação: Intents são as "mensagens" que o Android usa para navegar entre as telas.*

10. No iOS, qual arquivo é o equivalente funcional mais próximo ao `AndroidManifest.xml`?
    - [ ] Storyboard
    - [ ] AppConfig.swift
    - [x] Info.plist
    - [ ] AppDelegate.swift
    *Explicação: O Info.plist guarda metadados e permissões vitais para o aplicativo Apple.*
