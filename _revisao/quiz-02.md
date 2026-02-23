# Quiz 02 - Fundamentos de Java para Android ☕

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Por que o Java ainda é importante para o desenvolvimento Android, mesmo com a existência do Kotlin?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ecossistema Android tem mais de uma década de código Java robusto que todo desenvolvedor precisa saber navegar.">Porque o Kotlin vai deixar de existir em 2025.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ecossistema Android tem mais de uma década de código Java robusto que todo desenvolvedor precisa saber navegar.">Porque o Java é mais rápido que o Kotlin.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O ecossistema Android tem mais de uma década de código Java robusto que todo desenvolvedor precisa saber navegar.">Porque a maior parte do sistema Android e de bibliotecas legadas foi escrita em Java.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ecossistema Android tem mais de uma década de código Java robusto que todo desenvolvedor precisa saber navegar.">Porque o Google proibiu o uso de Kotlin em apps profissionais.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Em Java, qual é a sintaxe correta para declarar uma variável de texto?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Java clássico, usamos o tipo explícito com a primeira letra maiúscula (String é uma Classe).">text nome = "Android";</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Java clássico, usamos o tipo explícito com a primeira letra maiúscula (String é uma Classe).">var nome : String = "Android";</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! No Java clássico, usamos o tipo explícito com a primeira letra maiúscula (String é uma Classe).">String nome = "Android";</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. No Java clássico, usamos o tipo explícito com a primeira letra maiúscula (String é uma Classe).">string nome = 'Android';</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. O que acontece se você tentar rodar o código `int x = null;` em Java?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Tipos primitivos como int, double e boolean não podem ser nulos no Java.">O valor de x será 0.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Tipos primitivos como int, double e boolean não podem ser nulos no Java.">Ocorrerá um erro de compilação, pois tipos primitivos (int) não aceitam null.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Tipos primitivos como int, double e boolean não podem ser nulos no Java.">O programa rodará normalmente.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Tipos primitivos como int, double e boolean não podem ser nulos no Java.">O valor de x será indefinido.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual o comando usado para imprimir uma mensagem no console/Logcat em Java?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. System.out.println é o comando padrão de saída do Java SE.">print("Olá");</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. System.out.println é o comando padrão de saída do Java SE.">echo "Olá";</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! System.out.println é o comando padrão de saída do Java SE.">System.out.println("Olá");</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. System.out.println é o comando padrão de saída do Java SE.">console.log("Olá");</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que define uma Classe em Java?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Classes definem os atributos e comportamentos que os objetos criados a partir delas terão.">É apenas um arquivo de texto qualquer.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Classes definem os atributos e comportamentos que os objetos criados a partir delas terão.">É um molde ou planta para criar objetos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Classes definem os atributos e comportamentos que os objetos criados a partir delas terão.">É um comando de repetição.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Classes definem os atributos e comportamentos que os objetos criados a partir delas terão.">É um sinônimo de variável.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual modificador de acesso torna um atributo visível apenas dentro da própria classe?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Private garante o encapsulamento, protegendo os dados de acessos externos indevidos.">public</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Private garante o encapsulamento, protegendo os dados de acessos externos indevidos.">protected</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Private garante o encapsulamento, protegendo os dados de acessos externos indevidos.">private</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Private garante o encapsulamento, protegendo os dados de acessos externos indevidos.">static</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Em Android, o que é uma "Activity"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Quase toda tela que você vê em um app Android é uma subclasse de Activity.">Uma rotina de exercícios físicos.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Quase toda tela que você vê em um app Android é uma subclasse de Activity.">Uma classe que representa uma tela do aplicativo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Quase toda tela que você vê em um app Android é uma subclasse de Activity.">O banco de dados do celular.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Quase toda tela que você vê em um app Android é uma subclasse de Activity.">Uma conexão com a internet.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. Qual o método principal que o Android chama quando uma Activity é iniciada?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O onCreate é onde definimos o layout e inicializamos a lógica da nossa tela.">main()</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O onCreate é onde definimos o layout e inicializamos a lógica da nossa tela.">start()</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O onCreate é onde definimos o layout e inicializamos a lógica da nossa tela.">onCreate()</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O onCreate é onde definimos o layout e inicializamos a lógica da nossa tela.">onStop()</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Para que serve o comando `extends` em Java?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Herança permite reutilizar código. Ex: MainActivity extends Activity.">Para aumentar o tamanho da tela.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Herança permite reutilizar código. Ex: MainActivity extends Activity.">Para realizar Herança, fazendo uma classe herdar características de outra.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Herança permite reutilizar código. Ex: MainActivity extends Activity.">Para importar uma biblioteca.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Herança permite reutilizar código. Ex: MainActivity extends Activity.">Para deletar um objeto.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. O que significa "Compilar" um código Java?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O compilador Java (javac) gera os arquivos .class ou .dex que o Android consegue ler.">Traduzir o código para Português.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O compilador Java (javac) gera os arquivos .class ou .dex que o Android consegue ler.">Enviar o app para a loja oficial.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O compilador Java (javac) gera os arquivos .class ou .dex que o Android consegue ler.">Transformar o código escrito por humanos em Bytecode (entendido pela Máquina Virtual).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O compilador Java (javac) gera os arquivos .class ou .dex que o Android consegue ler.">Deletar os comentários do programa.</div>
  <div class="quiz-feedback"></div>
</div>
