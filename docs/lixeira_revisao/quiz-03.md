# Quiz 03 - Introdução ao Kotlin Moderno ⚡

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Por que o Kotlin é considerado uma linguagem "segura" (Safe) em relação ao Java?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Kotlin diferencia tipos que podem ser nulos de tipos que não podem, evitando o erro mais comum do Java.">Porque ele vem com antivírus embutido.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Kotlin diferencia tipos que podem ser nulos de tipos que não podem, evitando o erro mais comum do Java.">Por causa do Null Safety, que impede NullPointerExceptions em tempo de compilação.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Kotlin diferencia tipos que podem ser nulos de tipos que não podem, evitando o erro mais comum do Java.">Porque ele criptografa todas as variáveis automaticamente.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Kotlin diferencia tipos que podem ser nulos de tipos que não podem, evitando o erro mais comum do Java.">Porque só roda em computadores da NASA.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Como declaramos uma constante (valor que não muda) em Kotlin?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. 'val' (value) define uma referência imutável, enquanto 'var' define uma variável.">const x = 10</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. 'val' (value) define uma referência imutável, enquanto 'var' define uma variável.">var x = 10</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! 'val' (value) define uma referência imutável, enquanto 'var' define uma variável.">val x = 10</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. 'val' (value) define uma referência imutável, enquanto 'var' define uma variável.">let x = 10</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual o símbolo usado para indicar que uma variável pode aceitar valores nulos em Kotlin?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. String? aceita texto ou null. Uma String comum sem a interrogação nunca aceitará null.">!</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. String? aceita texto ou null. Uma String comum sem a interrogação nunca aceitará null.">#</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! String? aceita texto ou null. Uma String comum sem a interrogação nunca aceitará null.">?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. String? aceita texto ou null. Uma String comum sem a interrogação nunca aceitará null.">@</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Como funciona a Interpolação de Strings no Kotlin?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Usamos o símbolo $ seguido do nome da variável dentro das aspas do texto.">"Olá " + nome</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Usamos o símbolo $ seguido do nome da variável dentro das aspas do texto.">"Olá {nome}"</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Usamos o símbolo $ seguido do nome da variável dentro das aspas do texto.">"Olá $nome"</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Usamos o símbolo $ seguido do nome da variável dentro das aspas do texto.">"Olá %nome"</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que faz o operador Elvis (`?:`) em Kotlin?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. x ?: "Padrão" significa: use x, mas se x for nulo, use "Padrão".">Cria um topete no código.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. x ?: "Padrão" significa: use x, mas se x for nulo, use "Padrão".">Compara se dois valores são iguais.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! x ?: "Padrão" significa: use x, mas se x for nulo, use "Padrão".">Define um valor padrão caso o valor da esquerda seja nulo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. x ?: "Padrão" significa: use x, mas se x for nulo, use "Padrão".">Deleta uma variável da memória.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Como declaramos uma função simples em Kotlin?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. 'fun' é a palavra-chave para funções, com o tipo de retorno vindo após os parênteses.">function soma(a, b) { ... }</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. 'fun' é a palavra-chave para funções, com o tipo de retorno vindo após os parênteses.">void soma(int a, int b) { ... }</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! 'fun' é a palavra-chave para funções, com o tipo de retorno vindo após os parênteses.">fun soma(a: Int, b: Int): Int { ... }</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. 'fun' é a palavra-chave para funções, com o tipo de retorno vindo após os parênteses.">def soma(a, b):</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. No Kotlin, precisamos colocar ponto e vírgula (;) ao final de cada linha?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Kotlin elimina a necessidade do ponto e vírgula, resultando em um código mais limpo.">Sim, é obrigatório como no Java.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Kotlin elimina a necessidade do ponto e vírgula, resultando em um código mais limpo.">Sim, mas só se for um App profissional.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Kotlin elimina a necessidade do ponto e vírgula, resultando em um código mais limpo.">Não, é opcional e raramente usado.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Kotlin elimina a necessidade do ponto e vírgula, resultando em um código mais limpo.">Apenas se a linha for muito longa.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que é uma "Data Class" em Kotlin?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Data classes reduzem drasticamente o "boilerplate code" necessário em Java para classes de modelo.">Uma classe para gerenciar datas e calendários.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Data classes reduzem drasticamente o "boilerplate code" necessário em Java para classes de modelo.">Uma classe concisa cujo propósito principal é apenas guardar dados (gera getters/setters automaticamente).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Data classes reduzem drasticamente o "boilerplate code" necessário em Java para classes de modelo.">Uma classe que só funciona em feriados.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Data classes reduzem drasticamente o "boilerplate code" necessário em Java para classes de modelo.">Uma classe de banco de dados SQL.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Como o Kotlin lida com a interoperabilidade com o Java?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Essa é uma das maiores vantagens do Kotlin, permitindo migrações graduais de projetos Java.">Eles não conseguem rodar no mesmo projeto.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Essa é uma das maiores vantagens do Kotlin, permitindo migrações graduais de projetos Java.">Você precisa traduzir todo o Java para Kotlin primeiro.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Essa é uma das maiores vantagens do Kotlin, permitindo migrações graduais de projetos Java.">É 100% interoperável: você pode chamar código Java no Kotlin e vice-versa no mesmo projeto.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Essa é uma das maiores vantagens do Kotlin, permitindo migrações graduais de projetos Java.">O Kotlin só aceita bibliotecas novas.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. Se eu tenho `val lista = listOf(1, 2, 3)`, o que acontece se eu tentar fazer `lista.add(4)`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Para listas que podem mudar, devemos usar `mutableListOf()`.">O número 4 é adicionado normalmente.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Para listas que podem mudar, devemos usar `mutableListOf()`.">Ocorre um erro de compilação, pois `listOf` cria uma lista imutável.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Para listas que podem mudar, devemos usar `mutableListOf()`.">O programa crasha ao rodar.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Para listas que podem mudar, devemos usar `mutableListOf()`.">A lista é resetada.</div>
  <div class="quiz-feedback"></div>
</div>
