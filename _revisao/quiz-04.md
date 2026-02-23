# Quiz 04 - Estrutura de um Aplicativo Android 🏗️

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. O que é o arquivo "build.gradle" em um projeto Android?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Gradle gerencia quais bibliotecas seu app usa e como ele será compilado.">É onde desenhamos a interface visual.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Gradle gerencia quais bibliotecas seu app usa e como ele será compilado.">É o arquivo que contém as fotos do app.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Gradle gerencia quais bibliotecas seu app usa e como ele será compilado.">É o arquivo de configuração de dependências e automação de build.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Gradle gerencia quais bibliotecas seu app usa e como ele será compilado.">É o código fonte principal em Kotlin.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual diretório do projeto guarda os "Recursos", como imagens, cores e textos?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. 'res' vem de Resources. Tudo que não é código fonte (lógica) fica aqui.">java/</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. 'res' vem de Resources. Tudo que não é código fonte (lógica) fica aqui.">manifests/</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! 'res' vem de Resources. Tudo que não é código fonte (lógica) fica aqui.">res/</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. 'res' vem de Resources. Tudo que não é código fonte (lógica) fica aqui.">build/</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. O que define a interface visual (layout) de uma tela no Android clássico?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Tradicionalmente, o Android usa XML para definir a hierarquia de visualização da tela.">Um arquivo .txt</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Tradicionalmente, o Android usa XML para definir a hierarquia de visualização da tela.">Um arquivo .jpg</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Tradicionalmente, o Android usa XML para definir a hierarquia de visualização da tela.">Um arquivo .xml</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Tradicionalmente, o Android usa XML para definir a hierarquia de visualização da tela.">Um arquivo .kt</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual componente do sistema Android representa uma "página" ou tela interativa?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Activities são os blocos fundamentais da UI do Android.">Service</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Activities são os blocos fundamentais da UI do Android.">Broadcast Receiver</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Activities são os blocos fundamentais da UI do Android.">Activity</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Activities são os blocos fundamentais da UI do Android.">Intent</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Para que serve a pasta `res/values`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Centralizar textos e cores facilita a internacionalização e a manutenção do design.">Para guardar vídeos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Centralizar textos e cores facilita a internacionalização e a manutenção do design.">Para salvar o banco de dados.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Centralizar textos e cores facilita a internacionalização e a manutenção do design.">Para guardar arquivos XML de strings, cores e estilos (centralização de constantes).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Centralizar textos e cores facilita a internacionalização e a manutenção do design.">Para guardar o código Java.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual é a função do `ViewBinding`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewBinding evita o uso excessivo de `findViewById` e protege contra NullPointerExceptions.">Conectar o app ao Wi-Fi.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O ViewBinding evita o uso excessivo de `findViewById` e protege contra NullPointerExceptions.">Criar uma referência segura entre o arquivo de layout (XML) e o código Kotlin/Java.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewBinding evita o uso excessivo de `findViewById` e protege contra NullPointerExceptions.">Fazer o download de imagens da internet.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewBinding evita o uso excessivo de `findViewById` e protege contra NullPointerExceptions.">Comprimir o tamanho do app.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. No Gradle, o que significa `minSdkVersion`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Define a compatibilidade retroativa do seu aplicativo.">A versão máxima que o app suporta.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Define a compatibilidade retroativa do seu aplicativo.">A versão mínima do sistema Android que o celular deve ter para instalar o app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Define a compatibilidade retroativa do seu aplicativo.">O tamanho mínimo em MB do aplicativo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Define a compatibilidade retroativa do seu aplicativo.">O número de desenvolvedores no projeto.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que acontece na pasta `res/drawable`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Desenhos e ícones residem aqui para serem referenciados pelo layout.">Ficam os arquivos de texto salvos pelo usuário.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Desenhos e ícones residem aqui para serem referenciados pelo layout.">Ficam as músicas de fundo.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Desenhos e ícones residem aqui para serem referenciados pelo layout.">Ficam os ícones e imagens vetoriais do app.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Desenhos e ícones residem aqui para serem referenciados pelo layout.">Ficam os scripts do banco de dados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. O componente `Intent` serve para:</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Intents são as "mensagens" que o Android usa para navegar entre as telas.">Guardar dados permanentemente no celular.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Intents são as "mensagens" que o Android usa para navegar entre as telas.">Solicitar uma ação de outro componente (ex: abrir uma nova tela ou a câmera).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Intents são as "mensagens" que o Android usa para navegar entre as telas.">Aumentar o brilho da tela.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Intents são as "mensagens" que o Android usa para navegar entre as telas.">Compilar o código mais rápido.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. No iOS, qual arquivo é o equivalente funcional mais próximo ao `AndroidManifest.xml`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Info.plist guarda metadados e permissões vitais para o aplicativo Apple.">Storyboard</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Info.plist guarda metadados e permissões vitais para o aplicativo Apple.">AppConfig.swift</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Info.plist guarda metadados e permissões vitais para o aplicativo Apple.">Info.plist</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Info.plist guarda metadados e permissões vitais para o aplicativo Apple.">AppDelegate.swift</div>
  <div class="quiz-feedback"></div>
</div>
