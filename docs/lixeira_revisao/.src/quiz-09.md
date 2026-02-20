# Quiz 09 - Listas Eficientes (RecyclerView) 📋

1. Qual a principal vantagem do `RecyclerView` em relação à antiga `ListView`?
    - [ ] Ele exibe imagens coloridas automaticamente
    - [x] Ele recicla as Views dos itens que saíram da tela, economizando memória
    - [ ] Ele não precisa de código Kotlin para funcionar
    - [ ] Ele aumenta o tamanho da tela do celular
    *Explicação: A reciclagem permite exibir listas infinitas criando apenas um pequeno número de Views na memória.*

2. Para que serve o `LayoutManager` no RecyclerView?
    - [ ] Para salvar os dados no banco
    - [x] Para definir como os itens serão organizados (Lista, Grade, Carrossel)
    - [ ] Para traduzir o app
    - [ ] Para mudar a cor dos botões
    *Explicação: Ele é o responsável por decidir se a lista será vertical, horizontal ou em grade.*

3. Qual a função do `Adapter`?
    - [ ] Ligar o carregador na tomada
    - [x] Agir como uma ponte entre os dados (lista) e as Views do RecyclerView
    - [ ] Gerar arquivos PDF
    - [ ] Criptografar as fotos
    *Explicação: O Adapter pega a informação da lista e "injeta" nos componentes visuais do layout do item.*

4. O que o `ViewHolder` faz?
    - [ ] Segura o celular para o usuário
    - [x] Armazena as referências dos componentes visuais de um item para evitar buscas repetitivas (findViewById)
    - [ ] Exclui itens duplicados da lista
    - [ ] Conecta o app ao Wi-Fi
    *Explicação: Ele funciona como uma "gaveta" que guarda os botões e textos de cada linha da lista.*

5. Qual método do Adapter é responsável por preencher os dados em uma View específica?
    - [ ] onCreateViewHolder
    - [x] onBindViewHolder
    - [ ] getItemCount
    - [ ] notifyDataSetChanged
    *Explicação: É no onBind que o "casamento" entre o objeto da lista e a View acontece.*

6. O que representa o método `getItemCount()`?
    - [ ] O tamanho de cada letra do texto
    - [x] O número total de itens que a lista deve exibir
    - [ ] Quantas vezes o usuário clicou na tela
    - [ ] A porcentagem de bateria do celular
    *Explicação: O RecyclerView usa esse valor para saber o limite da rolagem.*

7. Como o iOS chama o conceito de reciclagem de células?
    - [ ] RecycleView
    - [x] dequeueReusableCell
    - [ ] cellReuser
    - [ ] SwiftList
    *Explicação: No UITableView/UICollectionView do iOS, também reciclamos células para manter a performance.*

8. O que acontece se chamarmos `notifyDataSetChanged()`?
    - [ ] O app fecha
    - [x] O RecyclerView redesenha todos os itens da lista
    - [ ] Ele apaga a lista do banco de dados
    - [ ] Ele envia uma notificação para o usuário
    *Explicação: É uma forma bruta de avisar que os dados mudaram e a lista precisa ser atualizada.*

9. Qual a vantagem de usar o `DiffUtil` ou `ListAdapter`?
    - [ ] O código fica em negrito
    - [x] Ele calcula apenas o que mudou na lista e gera animações automáticas de inserção/remoção
    - [ ] Ele permite usar o RecyclerView sem internet
    - [ ] Ele traduz a lista para espanhol
    *Explicação: É muito mais eficiente e elegante do que redesenhar a lista inteira.*

10. Como implementamos cliques nos itens do RecyclerView?
    - [ ] O RecyclerView já vem com clique automático em tudo
    - [x] Geralmente definindo um OnClickListener dentro do ViewHolder ou via lambda no Adapter
    - [ ] Usando um sensor de movimento
    - [ ] Gritando com o celular
    *Explicação: Como o RecyclerView é muito flexível, precisamos definir manualmente onde e como o clique será detectado.*