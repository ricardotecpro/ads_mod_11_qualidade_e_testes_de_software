# Quiz 09 - Listas Eficientes (RecyclerView) 📋

1. Qual a principal vantagem do RecyclerView em relação à antiga ListView?
    - [ ] Ele gasta mais bateria.
    - [x] Ele recicla as Views que saíram da tela para exibir novos dados, economizando memória e processamento.
    - [ ] Ele só funciona com listas de no máximo 10 itens.
    - [ ] Ele obriga o uso de imagens em 4K.
    *Explicação: A reciclagem evita a criação desnecessária de milhares de objetos de layout, mantendo o app fluido.*

2. No RecyclerView, para que serve o "Adapter"?
    - [ ] Para conectar o celular na tomada.
    - [ ] Para definir se a lista é vertical ou horizontal.
    - [x] Para atuar como o intermediário entre os dados (lista) e as Views (layout).
    - [ ] Para salvar os dados no banco de dados.
    *Explicação: O Adapter decide qual dado vai em qual posição da lista e como ele deve ser exibido.*

3. Qual a função do "ViewHolder"?
    - [ ] Guardar os dados em cache no disco.
    - [x] Guardar as referências dos componentes visuais (TextView, ImageView) para evitar chamadas lentas ao `findViewById`.
    - [ ] Definir a cor de fundo da lista.
    - [ ] Fazer o download de imagens.
    *Explicação: O ViewHolder funciona como uma "gaveta" que já tem tudo organizado, acelerando a atualização dos itens.*

4. Qual componente define se a lista será uma coluna única, uma grade (grid) ou um carrossel horizontal?
    - [ ] Adapter
    - [ ] ViewHolder
    - [x] LayoutManager
    - [ ] ItemDecoration
    *Explicação: O LayoutManager é o responsável pela estratégia de organização espacial dos itens.*

5. O que acontece se chamarmos o método `notifyDataSetChanged()` no Adapter?
    - [ ] Ele deleta a lista.
    - [x] Ele avisa ao RecyclerView que os dados mudaram e toda a lista precisa ser redesenhada.
    - [ ] Ele atualiza apenas o item que foi clicado.
    - [ ] Ele fecha o aplicativo.
    *Explicação: Embora funcional, o `notifyDataSetChanged` é ineficiente para listas grandes, pois força o redesenho de tudo.*

6. Qual é a ferramenta moderna do Jetpack que compara duas listas e atualiza apenas o que mudou (com animações)?
    - [ ] FastUpdate
    - [ ] ListCompare
    - [x] DiffUtil (usado no ListAdapter)
    - [ ] QuickChange
    *Explicação: O DiffUtil calcula a diferença exata entre listas, tornando as atualizações muito mais performáticas.*

7. Como o RecyclerView se comporta quando um item sai da tela pelo topo durante a rolagem?
    - [ ] O item é destruído para sempre.
    - [ ] O item fica escondido atrás da barra de status.
    - [x] O item vai para uma "piscina de reciclagem" para ser reutilizado no fundo da lista.
    - [ ] O app para de carregar dados.
    *Explicação: Esse é o conceito central de "Reciclagem" que dá nome ao componente.*

8. No desenvolvimento Android nativo, qual classe devemos estender para criar nosso próprio Adapter?
    - [ ] BaseAdapter
    - [ ] ListAdapter (antigo)
    - [x] RecyclerView.Adapter<ViewHolder>
    - [ ] ViewAdapter
    *Explicação: Usamos o Generics para indicar qual ViewHolder nosso Adapter vai gerenciar.*

9. Qual o método do Adapter é chamado toda vez que um item novo precisa ser exibido e uma View precisa ser "vinculada" ao dado?
    - [ ] onCreateViewHolder
    - [x] onBindViewHolder
    - [ ] getItemCount
    - [ ] onViewAttached
    *Explicação: "Bind" significa vincular/ligar. É aqui que fazemos `holder.textView.text = data.name`.*

10. No iOS, qual é o componente equivalente ao RecyclerView?
    - [ ] UIScrollView
    - [x] UITableView (ou UICollectionView)
    - [ ] UIPickerView
    - [ ] UIStackView
    *Explicação: UITableView é o padrão para listas simples e UICollectionView para grades e layouts complexos.*
