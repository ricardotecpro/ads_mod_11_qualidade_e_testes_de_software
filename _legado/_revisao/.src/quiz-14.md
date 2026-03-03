# Quiz 14 - Testes, Qualidade e Debugging 🐞

1. Qual o nível de log (`Log.class`) recomendado para erros críticos que fazem o app travar?
    - [ ] Log.d (Debug)
    - [x] Log.e (Error)
    - [ ] Log.v (Verbose)
    - [ ] Log.i (Info)
    *Explicação: O nível Error é reservado para falhas graves, facilitando a identificação no Logcat (em vermelho).*

2. O que é um `Breakpoint`?
    - [ ] O fim do turno de trabalho do programador
    - [x] Um ponto de interrupção no código onde o Debugger para a execução para análise
    - [ ] Um erro que acontece quando o café acaba
    - [ ] Uma tecla que deleta o código
    *Explicação: Permite inspecionar o estado do app em tempo real linha por linha.*

3. Por que dizemos que o Teste Unitário deve ser a base da pirâmide de testes?
    - [ ] Porque ele é o mais caro e difícil
    - [x] Porque ele é rápido, barato de rodar e deve cobrir a maior parte da lógica
    - [ ] Porque ele é o único que o Google Play aceita
    - [ ] Porque ele testa a tela do celular
    *Explicação: Testes unitários validam a lógica de negócio rapidamente sem precisar de um emulador.*

4. Qual biblioteca é usada para Testes de UI (Interface) no Android?
    - [ ] Cappuccino
    - [x] Espresso
    - [ ] Latte
    - [ ] Starbucks
    *Explicação: O Espresso permite simular interações do usuário (cliques, digitação) e verificar se a tela mudou.*

5. O que o `try/catch` faz no código?
    - [ ] Tenta baixar o app e captura fotos
    - [x] Tenta executar um código perigoso e captura a exceção (erro) se ela ocorrer
    - [ ] Finaliza o app se houver erro
    - [ ] Oculta o código dos hackers
    *Explicação: É a forma básica de prevenção de crashes no Java e Kotlin.*

6. Qual o objetivo do `Test Driven Development (TDD)`?
    - [ ] Escrever o código primeiro e os testes meses depois
    - [x] Escrever o teste antes do código real, garantindo que o requisito foi atingido
    - [ ] Deixar os testes para a equipe de QA fazer
    - [ ] Programar sem precisar testar nada
    *Explicação: O TDD foca no ciclo Red (falha), Green (passa), Refactor (melhora).*

7. Onde ficam guardados os Testes Unitários no projeto Android Studio?
    - [ ] src/main/res
    - [x] src/test
    - [ ] src/androidTest
    - [ ] assets/tests
    *Explicação: A pasta src/test é para testes que rodam na máquina local (JVM), enquanto src/androidTest é para o emulador.*

8. O que o framework `XCTest` representa no mundo Apple (iOS)?
    - [ ] Um tipo de bateria externa
    - [x] O framework oficial para criação de testes unitários e de UI no Xcode
    - [ ] Um comando para formatar o Mac
    - [ ] O nome do emulador de iPhone
    *Explicação: É o equivalente direto às bibliotecas de teste do Android.*

9. Qual a principal função de um `Teste de Regressão`?
    - [ ] Voltar o código para a versão anterior
    - [x] Garantir que uma nova funcionalidade não quebrou o que já estava funcionando
    - [ ] Testar se o app funciona em celulares antigos
    - [ ] Apagar bugs automaticamente
    *Explicação: É essencial para manter a estabilidade enquanto o app cresce.*

10. O que significa uma "Cobertura de Teste" (Code Coverage)?
    - [ ] A cor da capa do celular
    - [x] O percentual de linhas de código que são executadas pelos testes
    - [ ] Quantos apps de teste você tem instalado
    - [ ] O alcance do Wi-Fi do escritório
    *Explicação: Indica o quão bem testado o seu código está.*