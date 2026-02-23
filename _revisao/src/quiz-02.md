# Quiz 02 - Fundamentos de Java para Android ☕

1. Por que o Java ainda é importante para o desenvolvimento Android, mesmo com a existência do Kotlin?
    - [ ] Porque o Kotlin vai deixar de existir em 2025.
    - [ ] Porque o Java é mais rápido que o Kotlin.
    - [x] Porque a maior parte do sistema Android e de bibliotecas legadas foi escrita em Java.
    - [ ] Porque o Google proibiu o uso de Kotlin em apps profissionais.
    *Explicação: O ecossistema Android tem mais de uma década de código Java robusto que todo desenvolvedor precisa saber navegar.*

2. Em Java, qual é a sintaxe correta para declarar uma variável de texto?
    - [ ] text nome = "Android";
    - [ ] var nome : String = "Android";
    - [x] String nome = "Android";
    - [ ] string nome = 'Android';
    *Explicação: No Java clássico, usamos o tipo explícito com a primeira letra maiúscula (String é uma Classe).*

3. O que acontece se você tentar rodar o código `int x = null;` em Java?
    - [ ] O valor de x será 0.
    - [x] Ocorrerá um erro de compilação, pois tipos primitivos (int) não aceitam null.
    - [ ] O programa rodará normalmente.
    - [ ] O valor de x será indefinido.
    *Explicação: Tipos primitivos como int, double e boolean não podem ser nulos no Java.*

4. Qual o comando usado para imprimir uma mensagem no console/Logcat em Java?
    - [ ] print("Olá");
    - [ ] echo "Olá";
    - [x] System.out.println("Olá");
    - [ ] console.log("Olá");
    *Explicação: System.out.println é o comando padrão de saída do Java SE.*

5. O que define uma Classe em Java?
    - [ ] É apenas um arquivo de texto qualquer.
    - [x] É um molde ou planta para criar objetos.
    - [ ] É um comando de repetição.
    - [ ] É um sinônimo de variável.
    *Explicação: Classes definem os atributos e comportamentos que os objetos criados a partir delas terão.*

6. Qual modificador de acesso torna um atributo visível apenas dentro da própria classe?
    - [ ] public
    - [ ] protected
    - [x] private
    - [ ] static
    *Explicação: Private garante o encapsulamento, protegendo os dados de acessos externos indevidos.*

7. Em Android, o que é uma "Activity"?
    - [ ] Uma rotina de exercícios físicos.
    - [x] Uma classe que representa uma tela do aplicativo.
    - [ ] O banco de dados do celular.
    - [ ] Uma conexão com a internet.
    *Explicação: Quase toda tela que você vê em um app Android é uma subclasse de Activity.*

8. Qual o método principal que o Android chama quando uma Activity é iniciada?
    - [ ] main()
    - [ ] start()
    - [x] onCreate()
    - [ ] onStop()
    *Explicação: O onCreate é onde definimos o layout e inicializamos a lógica da nossa tela.*

9. Para que serve o comando `extends` em Java?
    - [ ] Para aumentar o tamanho da tela.
    - [x] Para realizar Herança, fazendo uma classe herdar características de outra.
    - [ ] Para importar uma biblioteca.
    - [ ] Para deletar um objeto.
    *Explicação: Herança permite reutilizar código. Ex: MainActivity extends Activity.*

10. O que significa "Compilar" um código Java?
    - [ ] Traduzir o código para Português.
    - [ ] Enviar o app para a loja oficial.
    - [x] Transformar o código escrito por humanos em Bytecode (entendido pela Máquina Virtual).
    - [ ] Deletar os comentários do programa.
    *Explicação: O compilador Java (javac) gera os arquivos .class ou .dex que o Android consegue ler.*
