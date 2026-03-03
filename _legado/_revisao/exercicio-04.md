# Exercícios 04 - Estrutura App Android 🏗️

## 🟢 Fáceis

1.  **Manifesto**: Para que serve o arquivo `AndroidManifest.xml`? Cite duas coisas definidas nele.
2.  **Recursos**: Em qual pasta devemos colocar as imagens do nosso aplicativo? E os textos?

## 🟡 Médios

3.  **Ciclo de Vida (Ordem)**:
    Coloque os métodos na ordem correta de execução quando o app é aberto pela primeira vez:
    `onResume`, `onCreate`, `onStart`.
4.  **XML vs Code**:
    Por que o Android separa o Layout (XML) da Lógica (Kotlin)? Cite uma vantagem dessa abordagem (ex: tradução, manutenção, designers).

## 🔴 Desafio

5.  **Debug de Lifecycle**:
    Um desenvolvedor novato colocou um código pesado (download de imagem) dentro do método `onResume()`.
    *   O que acontece com o app se o usuário ficar bloqueando e desbloqueando a tela várias vezes seguidas?
    *   Qual seria o lugar (ou componente) mais adequado para fazer esse download apenas uma vez? (Pode chutar: ViewModel, onCreate, WorkManager...)
