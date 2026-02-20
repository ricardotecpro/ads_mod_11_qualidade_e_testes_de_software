# Quiz 06 - Navegação e Intents 🗺️

1. No Android, o que é uma "Intent"?
    - [ ] É o plano de marketing do aplicativo.
    - [x] É um objeto de mensagem usado para solicitar uma ação de outro componente do app ou do sistema.
    - [ ] É um tipo de variável que guarda números decimais.
    - [ ] É o comando para deletar o aplicativo.
    *Explicação: Intents (Intenções) são os mensageiros que iniciam Activities, abrem câmeras, etc.*

2. Qual a diferença entre uma Intent Explícita e uma Implícita?
    - [ ] A explícita é para iOS e a implícita para Android.
    - [ ] A explícita abre o navegador e a implícita abre uma tela interna.
    - [x] A explícita define exatamente qual classe rodar; a implícita apenas declara a ação (ex: "abrir site").
    - [ ] Não há diferença técnica.
    *Explicação: Usamos explícitas para navegar dentro do próprio app e implícitas para interagir com outros apps.*

3. Como passamos um dado do tipo Texto (String) para a próxima tela?
    - [ ] intent.send("TEXTO")
    - [ ] intent.addExtra("CHAVE", "VALOR")
    - [x] intent.putExtra("CHAVE", "VALOR")
    - [ ] intent.saveData("VALOR")
    *Explicação: O método `putExtra` permite adicionar diversos tipos de dados ao "pacote" da intent.*

4. Qual comando é usado para efetivamente iniciar a nova tela após configurar a Intent?
    - [ ] go()
    - [ ] openActivity(intent)
    - [x] startActivity(intent)
    - [ ] run(intent)
    *Explicação: `startActivity` é o método padrão da classe Context/Activity para navegação.*

5. O que acontece com a Activity atual quando chamamos o método `finish()`?
    - [ ] Ela fica em segundo plano para sempre.
    - [ ] Ela é reiniciada.
    - [x] Ela é destruída e removida da "Pilha de Voltar" (Back Stack).
    - [ ] O celular desliga.
    *Explicação: `finish()` encerra o ciclo de vida da Activity atual.*

6. Como recuperamos um dado do tipo Inteiro que foi passado via Intent?
    - [ ] intent.getInt("CHAVE")
    - [x] intent.getIntExtra("CHAVE", valorPadrao)
    - [ ] intent.extraValue("CHAVE")
    - [ ] intent.loadInt("CHAVE")
    *Explicação: Para tipos primitivos, o Android exige um valor padrão caso a chave não seja encontrada.*

7. Imagine que você está na Tela A, abriu a Tela B e depois a Tela C. Se o usuário apertar o botão "Voltar" do celular na Tela C, o que acontece por padrão?
    - [ ] O app fecha totalmente.
    - [ ] Ele volta para a Tela A.
    - [x] Ele volta para a Tela B.
    - [ ] Ele abre o menu do Google.
    *Explicação: O Android mantém uma pilha (LIFO - Last In, First Out) de navegação.*

8. Qual Intent Implícita seria usada para abrir o navegador em um site específico?
    - [ ] Intent.ACTION_CALL
    - [ ] Intent.ACTION_SEND
    - [x] Intent.ACTION_VIEW
    - [ ] Intent.ACTION_NAVIGATE
    *Explicação: ACTION_VIEW indica que queremos visualizar um conteúdo (URI).*

9. Por que é importante chamar `finish()` após navegar da tela de Login para a Home?
    - [ ] Para economizar bateria.
    - [x] Para evitar que o usuário volte para a tela de Login ao apertar o botão "Voltar" após já estar logado.
    - [ ] Porque o Android só permite uma Activity aberta por vez.
    - [ ] Para apagar os dados do usuário.
    *Explicação: Gerenciar a pilha de navegação é crucial para uma boa experiência de usuário (UX).*

10. No iOS, qual é o conceito equivalente às Intents para navegação entre ViewControllers?
    - [ ] Protocols
    - [ ] Delegates
    - [x] Segues (ou Navigation Push)
    - [ ] Core Data
    *Explicação: No iOS clássico, usamos Segues para definir transições entre telas no Storyboard.*
