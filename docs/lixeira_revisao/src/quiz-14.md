# Quiz 14 - Testes, Qualidade e Debugging 🐞

1. Qual a principal diferença entre um Teste Unitário e um Teste de UI no Android?
    - [ ] Testes de UI são mais rápidos.
    - [x] Testes Unitários testam lógica rápida na JVM (computador); Testes de UI rodam no emulador/celular clicando na tela.
    - [ ] Testes Unitários só funcionam com Java.
    - [ ] Não há diferença, são o mesmo arquivo.
    *Explicação: Testes Unitários são a base da pirâmide (rápidos e baratos), enquanto testes de UI (Espresso) são mais lentos e complexos.*

2. Para que serve o "Logcat" no Android Studio?
    - [ ] Para desenhar ícones.
    - [x] Para visualizar mensagens de sistema, erros e logs personalizados que ajudam a encontrar bugs.
    - [ ] Para salvar o app na nuvem.
    - [ ] Para aumentar a velocidade da internet.
    *Explicação: É o console de saída onde o desenvolvedor monitora toda a saúde do app em tempo real.*

3. Qual o nível de log (`Log.x`) deve ser usado para indicar um erro crítico que faz o app parar de funcionar conforme esperado?
    - [ ] Log.v (Verbose)
    - [ ] Log.d (Debug)
    - [ ] Log.i (Info)
    - [x] Log.e (Error)
    *Explicação: O Log.e aparece em vermelho no Logcat e ajuda a identificar falhas graves rapidamente.*

4. O que é um "Breakpoint" no processo de Debugging?
    - [ ] Uma tecla que quebrou.
    - [x] Um ponto de interrupção no código onde a execução para para o desenvolvedor analisar o valor das variáveis.
    - [ ] O final do programa.
    - [ ] Um erro de compilação.
    *Explicação: Breakpoints permitem a inspeção "ao vivo" do estado do app linha por linha.*

5. Qual biblioteca é o padrão para realizar testes de interface (UI) no Android?
    - [ ] JUnit
    - [ ] Mockito
    - [x] Espresso
    - [ ] Retrofit
    *Explicação: O Espresso permite encontrar elementos na tela (`withId`) e realizar ações (`click()`, `typeText()`).*

6. O que o framework JUnit faz?
    - [ ] Desenha layouts.
    - [x] Fornece a estrutura para escrever e rodar testes unitários (anotações como `@Test`).
    - [ ] Faz o build do app.
    - [ ] Envia o app para a loja.
    *Explicação: O JUnit é o framework de testes mais popular do mundo Java/Kotlin.*

7. Por que devemos usar `try/catch` em operações de rede?
    - [ ] Para o código ficar mais longo.
    - [x] Para evitar que o app feche (Crash) caso a internet falhe ou o servidor retorne erro.
    - [ ] Para o download ser mais rápido.
    - [ ] Porque é obrigatório em todas as funções.
    *Explicação: O tratamento de exceções garante que o app continue rodando mesmo diante de imprevistos externos.*

8. O que significa "Refatorar" um código?
    - [ ] Adicionar novas funcionalidades.
    - [x] Reorganizar e limpar o código existente para melhorar a qualidade, sem mudar o que ele faz para o usuário.
    - [ ] Apagar todo o projeto e começar do zero.
    - [ ] Traduzir o app.
    *Explicação: Refatorar é essencial para manter a saúde do projeto a longo prazo.*

9. Qual é a ferramenta de testes automatizados da Apple para o iOS?
    - [ ] Espresso iOS
    - [ ] AppleTest
    - [x] XCTest
    - [ ] SwiftUnit
    *Explicação: O XCTest é o framework nativo da Apple para testes unitários, de performance e de UI.*

10. Qual a porcentagem ideal de cobertura de testes unitários recomendada pela "Pirâmide de Testes"?
    - [ ] 0% (não precisa testar).
    - [ ] 10% (testar só o login).
    - [x] Cerca de 70% (deve ser a maior parte dos seus testes).
    - [ ] 100% (testar cada linha exaustivamente).
    *Explicação: Testes unitários são a fundação por serem rápidos, estáveis e fáceis de manter.*
