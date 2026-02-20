# Quiz 03 - Introdução ao Kotlin Moderno ⚡

1. Por que o Kotlin é considerado uma linguagem "segura" (Safe) em relação ao Java?
    - [ ] Porque ele vem com antivírus embutido.
    - [x] Por causa do Null Safety, que impede NullPointerExceptions em tempo de compilação.
    - [ ] Porque ele criptografa todas as variáveis automaticamente.
    - [ ] Porque só roda em computadores da NASA.
    *Explicação: O Kotlin diferencia tipos que podem ser nulos de tipos que não podem, evitando o erro mais comum do Java.*

2. Como declaramos uma constante (valor que não muda) em Kotlin?
    - [ ] const x = 10
    - [ ] var x = 10
    - [x] val x = 10
    - [ ] let x = 10
    *Explicação: 'val' (value) define uma referência imutável, enquanto 'var' define uma variável.*

3. Qual o símbolo usado para indicar que uma variável pode aceitar valores nulos em Kotlin?
    - [ ] !
    - [ ] #
    - [x] ?
    - [ ] @
    *Explicação: String? aceita texto ou null. Uma String comum sem a interrogação nunca aceitará null.*

4. Como funciona a Interpolação de Strings no Kotlin?
    - [ ] "Olá " + nome
    - [ ] "Olá {nome}"
    - [x] "Olá $nome"
    - [ ] "Olá %nome"
    *Explicação: Usamos o símbolo $ seguido do nome da variável dentro das aspas do texto.*

5. O que faz o operador Elvis (`?:`) em Kotlin?
    - [ ] Cria um topete no código.
    - [ ] Compara se dois valores são iguais.
    - [x] Define um valor padrão caso o valor da esquerda seja nulo.
    - [ ] Deleta uma variável da memória.
    *Explicação: x ?: "Padrão" significa: use x, mas se x for nulo, use "Padrão".*

6. Como declaramos uma função simples em Kotlin?
    - [ ] function soma(a, b) { ... }
    - [ ] void soma(int a, int b) { ... }
    - [x] fun soma(a: Int, b: Int): Int { ... }
    - [ ] def soma(a, b):
    *Explicação: 'fun' é a palavra-chave para funções, com o tipo de retorno vindo após os parênteses.*

7. No Kotlin, precisamos colocar ponto e vírgula (;) ao final de cada linha?
    - [ ] Sim, é obrigatório como no Java.
    - [ ] Sim, mas só se for um App profissional.
    - [x] Não, é opcional e raramente usado.
    - [ ] Apenas se a linha for muito longa.
    *Explicação: O Kotlin elimina a necessidade do ponto e vírgula, resultando em um código mais limpo.*

8. O que é uma "Data Class" em Kotlin?
    - [ ] Uma classe para gerenciar datas e calendários.
    - [x] Uma classe concisa cujo propósito principal é apenas guardar dados (gera getters/setters automaticamente).
    - [ ] Uma classe que só funciona em feriados.
    - [ ] Uma classe de banco de dados SQL.
    *Explicação: Data classes reduzem drasticamente o "boilerplate code" necessário em Java para classes de modelo.*

9. Como o Kotlin lida com a interoperabilidade com o Java?
    - [ ] Eles não conseguem rodar no mesmo projeto.
    - [ ] Você precisa traduzir todo o Java para Kotlin primeiro.
    - [x] É 100% interoperável: você pode chamar código Java no Kotlin e vice-versa no mesmo projeto.
    - [ ] O Kotlin só aceita bibliotecas novas.
    *Explicação: Essa é uma das maiores vantagens do Kotlin, permitindo migrações graduais de projetos Java.*

10. Se eu tenho `val lista = listOf(1, 2, 3)`, o que acontece se eu tentar fazer `lista.add(4)`?
    - [ ] O número 4 é adicionado normalmente.
    - [x] Ocorre um erro de compilação, pois `listOf` cria uma lista imutável.
    - [ ] O programa crasha ao rodar.
    - [ ] A lista é resetada.
    *Explicação: Para listas que podem mudar, devemos usar `mutableListOf()`.*
