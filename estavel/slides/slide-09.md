# Aula 09 - Listas Eficientes (RecyclerView) 📋
## Performance em listas infinitas

---

## Agenda 📅

1. O Problema da ListView 🐢 <!-- .element: class="fragment" -->
2. O Conceito de Reciclagem ♻️ <!-- .element: class="fragment" -->
3. ViewHolder e Adapter <!-- .element: class="fragment" -->
4. LayoutManagers <!-- .element: class="fragment" -->
5. Cliques e Interação <!-- .element: class="fragment" -->

---

## 1. Por que Reciclar? 🤔

- Criar mil layouts trava o celular. <!-- .element: class="fragment" -->
- O RecyclerView reaproveita a carcaça da View. <!-- .element: class="fragment" -->
- **Fato**: Apenas o que cabe na tela existe de verdade. <!-- .element: class="fragment" -->

---

## 2. A Reciclagem Visual ♻️

```mermaid
graph TD
    A[Saindo da tela] --> B((Piscina de Views))
    B --> C[Entrando na tela]
    C --> D[ViewHolder preenche novos dados]
```

---

## 3. Os 3 Componentes Reais ⚙️

1.  **LayoutManager**: "Como eu organizo?" (Lista/Grade) <!-- .element: class="fragment" -->
2.  **Adapter**: "Quais dados eu coloco?" <!-- .element: class="fragment" -->
3.  **ViewHolder**: "Onde eu guardo as referências?" <!-- .element: class="fragment" -->

---

## 4. O Adapter na Prática ⚔️

```kotlin
override fun onBindViewHolder(holder: ViewHolder, position: Int) {
    val item = lista[position]
    holder.txtNome.text = item.nome
}
```

---

## 5. LayoutManagers: Formatos 🤸

- **LinearLayoutManager**: Lista vertical. <!-- .element: class="fragment" -->
- **GridLayoutManager**: Grade (estilo galeria). <!-- .element: class="fragment" -->
- **Staggered**: Grade irregular (estilo Pinterest). <!-- .element: class="fragment" -->

---

## 6. Cliques no Item 👆

- Passe uma lambda (callback) para o Adapter. <!-- .element: class="fragment" -->
- Use a posição (`position`) do item clicado. <!-- .element: class="fragment" -->

---

## 7. Melhores Práticas 🏆

- Use **ListAdapter** + **DiffUtil**. <!-- .element: class="fragment" -->
- Evite lógica pesada dentro do `onBind`. <!-- .element: class="fragment" -->
- Ícones de placeholders para imagens. <!-- .element: class="fragment" -->

---

## Desafio de Lista ⚡

Qual o comando no iOS que faz o mesmo que a reciclagem do Android?

---

## Resumo ✅

- RecyclerView = Performance. <!-- .element: class="fragment" -->
- Adapter liga dado e visual. <!-- .element: class="fragment" -->
- ViewHolder evita o `findViewById` excessivo. <!-- .element: class="fragment" -->

---

## Próxima Aula: API REST 🌍

- Trazendo dados da nuvem. <!-- .element: class="fragment" -->
- Retrofit e JSON. <!-- .element: class="fragment" -->

---

## Dúvidas? 📋