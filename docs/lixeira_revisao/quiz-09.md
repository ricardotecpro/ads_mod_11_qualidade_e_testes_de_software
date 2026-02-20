# Quiz 09 - Listas Eficientes (RecyclerView) 📋

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. Qual a principal vantagem do RecyclerView em relação à antiga ListView?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A reciclagem evita a criação desnecessária de milhares de objetos de layout, mantendo o app fluido.">Ele gasta mais bateria.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A reciclagem evita a criação desnecessária de milhares de objetos de layout, mantendo o app fluido.">Ele recicla as Views que saíram da tela para exibir novos dados, economizando memória e processamento.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A reciclagem evita a criação desnecessária de milhares de objetos de layout, mantendo o app fluido.">Ele só funciona com listas de no máximo 10 itens.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A reciclagem evita a criação desnecessária de milhares de objetos de layout, mantendo o app fluido.">Ele obriga o uso de imagens em 4K.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. No RecyclerView, para que serve o "Adapter"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Adapter decide qual dado vai em qual posição da lista e como ele deve ser exibido.">Para conectar o celular na tomada.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Adapter decide qual dado vai em qual posição da lista e como ele deve ser exibido.">Para definir se a lista é vertical ou horizontal.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Adapter decide qual dado vai em qual posição da lista e como ele deve ser exibido.">Para atuar como o intermediário entre os dados (lista) e as Views (layout).</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Adapter decide qual dado vai em qual posição da lista e como ele deve ser exibido.">Para salvar os dados no banco de dados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual a função do "ViewHolder"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewHolder funciona como uma "gaveta" que já tem tudo organizado, acelerando a atualização dos itens.">Guardar os dados em cache no disco.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O ViewHolder funciona como uma "gaveta" que já tem tudo organizado, acelerando a atualização dos itens.">Guardar as referências dos componentes visuais (TextView, ImageView) para evitar chamadas lentas ao `findViewById`.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewHolder funciona como uma "gaveta" que já tem tudo organizado, acelerando a atualização dos itens.">Definir a cor de fundo da lista.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O ViewHolder funciona como uma "gaveta" que já tem tudo organizado, acelerando a atualização dos itens.">Fazer o download de imagens.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual componente define se a lista será uma coluna única, uma grade (grid) ou um carrossel horizontal?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O LayoutManager é o responsável pela estratégia de organização espacial dos itens.">Adapter</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O LayoutManager é o responsável pela estratégia de organização espacial dos itens.">ViewHolder</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O LayoutManager é o responsável pela estratégia de organização espacial dos itens.">LayoutManager</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O LayoutManager é o responsável pela estratégia de organização espacial dos itens.">ItemDecoration</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. O que acontece se chamarmos o método `notifyDataSetChanged()` no Adapter?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Embora funcional, o `notifyDataSetChanged` é ineficiente para listas grandes, pois força o redesenho de tudo.">Ele deleta a lista.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Embora funcional, o `notifyDataSetChanged` é ineficiente para listas grandes, pois força o redesenho de tudo.">Ele avisa ao RecyclerView que os dados mudaram e toda a lista precisa ser redesenhada.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Embora funcional, o `notifyDataSetChanged` é ineficiente para listas grandes, pois força o redesenho de tudo.">Ele atualiza apenas o item que foi clicado.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Embora funcional, o `notifyDataSetChanged` é ineficiente para listas grandes, pois força o redesenho de tudo.">Ele fecha o aplicativo.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual é a ferramenta moderna do Jetpack que compara duas listas e atualiza apenas o que mudou (com animações)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O DiffUtil calcula a diferença exata entre listas, tornando as atualizações muito mais performáticas.">FastUpdate</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O DiffUtil calcula a diferença exata entre listas, tornando as atualizações muito mais performáticas.">ListCompare</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O DiffUtil calcula a diferença exata entre listas, tornando as atualizações muito mais performáticas.">DiffUtil (usado no ListAdapter)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O DiffUtil calcula a diferença exata entre listas, tornando as atualizações muito mais performáticas.">QuickChange</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Como o RecyclerView se comporta quando um item sai da tela pelo topo durante a rolagem?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Esse é o conceito central de "Reciclagem" que dá nome ao componente.">O item é destruído para sempre.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Esse é o conceito central de "Reciclagem" que dá nome ao componente.">O item fica escondido atrás da barra de status.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Esse é o conceito central de "Reciclagem" que dá nome ao componente.">O item vai para uma "piscina de reciclagem" para ser reutilizado no fundo da lista.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Esse é o conceito central de "Reciclagem" que dá nome ao componente.">O app para de carregar dados.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. No desenvolvimento Android nativo, qual classe devemos estender para criar nosso próprio Adapter?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Usamos o Generics para indicar qual ViewHolder nosso Adapter vai gerenciar.">BaseAdapter</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Usamos o Generics para indicar qual ViewHolder nosso Adapter vai gerenciar.">ListAdapter (antigo)</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Usamos o Generics para indicar qual ViewHolder nosso Adapter vai gerenciar.">RecyclerView.Adapter<ViewHolder></div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Usamos o Generics para indicar qual ViewHolder nosso Adapter vai gerenciar.">ViewAdapter</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual o método do Adapter é chamado toda vez que um item novo precisa ser exibido e uma View precisa ser "vinculada" ao dado?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. "Bind" significa vincular/ligar. É aqui que fazemos `holder.textView.text = data.name`.">onCreateViewHolder</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! "Bind" significa vincular/ligar. É aqui que fazemos `holder.textView.text = data.name`.">onBindViewHolder</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. "Bind" significa vincular/ligar. É aqui que fazemos `holder.textView.text = data.name`.">getItemCount</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. "Bind" significa vincular/ligar. É aqui que fazemos `holder.textView.text = data.name`.">onViewAttached</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. No iOS, qual é o componente equivalente ao RecyclerView?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. UITableView é o padrão para listas simples e UICollectionView para grades e layouts complexos.">UIScrollView</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! UITableView é o padrão para listas simples e UICollectionView para grades e layouts complexos.">UITableView (ou UICollectionView)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. UITableView é o padrão para listas simples e UICollectionView para grades e layouts complexos.">UIPickerView</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. UITableView é o padrão para listas simples e UICollectionView para grades e layouts complexos.">UIStackView</div>
  <div class="quiz-feedback"></div>
</div>
