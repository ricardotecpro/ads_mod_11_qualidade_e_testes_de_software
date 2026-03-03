# Quiz 06 - Navegação entre Telas 🗺️

1. O que representa uma `Intent` no mundo Android?
    - [ ] Uma variável que guarda senhas
    - [x] Uma mensagem/intenção enviada ao sistema para realizar uma ação
    - [ ] O nome do processo de compilação
    - [ ] Um tipo de bateria de longa duração
    *Explicação: Intents são usadas para iniciar Activities, Serviços ou enviar Broadcasts.*

2. Quando usamos uma Intent **Explícita**?
    - [ ] Para abrir o navegador em um site qualquer
    - [x] Quando sabemos exatamente qual classe (Activity) queremos abrir internamente
    - [ ] Para tirar uma foto usando qualquer app de câmera disponível
    - [ ] Quando o usuário clica em um link de e-mail
    *Explicação: Intents explícitas apontam diretamente para um componente do seu próprio aplicativo.*

3. Como passamos um dado do tipo String para a próxima tela?
    - [ ] intent.saveValue("chave", "valor")
    - [x] intent.putExtra("chave", "valor")
    - [ ] intent.sendData("valor")
    - [ ] intent.addString("valor")
    *Explicação: O método putExtra adiciona pares chave-valor ao "pacote" (Bundle) da Intent.*

4. Qual o equivalente no iOS ao `startActivity(intent)`?
    - [ ] AppDelegate.start()
    - [x] pushViewController() ou performSegue()
    - [ ] viewDidLoad()
    - [ ] openURL()
    *Explicação: São os métodos usados para empurrar uma nova tela para a pilha de navegação do iOS.*

5. O que é o `Back Stack` (Pilha de Voltar)?
    - [ ] Um erro que acontece quando o Java para de funcionar
    - [x] A estrutura de pilha que organiza a ordem das Activities abertas
    - [ ] O local onde o Google guarda os backups dos apps
    - [ ] Uma lista de bugs que precisam ser corrigidos
    *Explicação: O Android coloca cada nova Activity no topo da pilha. Ao voltar, a do topo é removida.*

6. Para que serve o método `finish()`?
    - [ ] Para encerrar o app inteiro e desligar o celular
    - [x] Para encerrar a Activity atual e removê-la da pilha
    - [ ] Para salvar os dados no banco de dados automaticamente
    - [ ] Para baixar uma atualização da Play Store
    *Explicação: finish() retira a tela atual da memória e volta para a tela anterior (se houver).*

7. Como recuperamos um dado enviado via Intent na Activity de destino?
    - [ ] getExtra("chave")
    - [x] intent.getStringExtra("chave")
    - [ ] findExtra("chave")
    - [ ] getFromIntent("chave")
    *Explicação: Usamos métodos específicos baseados no tipo do dado enviado (String, Int, Boolean, etc).*

8. Qual o objetivo de uma Intent **Implícita**?
    - [ ] Abrir uma tela secreta do app
    - [x] Pedir ao sistema que realize uma ação sem especificar qual app deve fazê-la
    - [ ] Aumentar a velocidade de navegação
    - [ ] Esconder o código do programador
    *Explicação: Ex: "Quero abrir este link". O Android mostra as opções de navegadores instalados.*

9. O que acontece com a Activity A quando ela abre a Activity B?
    - [ ] Ela continua no estado Resumed
    - [x] Ela entra no estado onPause e depois onStop (ficando em background)
    - [ ] Ela é destruída imediatamente para economizar memória
    - [ ] Ela fica invisível mas continua recebendo toques
    *Explicação: A Activity anterior perde o foco e fica pausada/parada enquanto a nova tela está na frente.*

10. Como evitamos que o usuário volte para a tela de Login após já ter logado?
    - [ ] Bloqueando o botão físico de voltar
    - [x] Chamando o método finish() logo após o startActivity() da Home
    - [ ] Reiniciando o celular
    - [ ] Desinstalando o app
    *Explicação: Ao finalizar a Activity de Login, ela sai da pilha e não pode ser acessada pelo botão voltar.*