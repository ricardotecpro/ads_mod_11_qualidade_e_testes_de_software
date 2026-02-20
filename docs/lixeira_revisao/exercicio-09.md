# Exercícios 09 - Listas Eficientes (RecyclerView) 📋

## 🟢 Fáceis

1.  **Conceito**: Por que o `RecyclerView` é mais eficiente que um `ListView` antigo ou um `LinearLayout` dentro de um `ScrollView`?
2.  **Componentes**: Qual a função do `LayoutManager` no RecyclerView?

## 🟡 Médios

3.  **Adapter**:
    O método `onBindViewHolder` é chamado muitas vezes. O que acontece se você colocar uma lógica pesada (ex: baixar uma imagem da internet de forma síncrona) dentro dele?
4.  **ViewHolder**:
    Para que serve a classe `ViewHolder`? Por que não devemos fazer `findViewById` direto no `onBindViewHolder`?

## 🔴 Desafio

5.  **Múltiplos Tipos de View**:
    Imagine um chat (WhatsApp). Mensagens enviadas ficam na direita (verde), recebidas na esquerda (branco).
    *   Como você implementaria isso no RecyclerView? (Dica: pesquise sobre `getItemViewType`).