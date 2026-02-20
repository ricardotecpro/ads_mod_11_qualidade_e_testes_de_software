# Projeto 09 - Agenda de Contatos (RecyclerView) 📋

**Objetivo**: Implementar uma lista dinâmica e performática.

## O Desafio
Crie uma agenda de contatos:
1.  **Layout do Item**: Crie `item_contato.xml` com Nome e Telefone.
2.  **Adapter**: Crie um `RecyclerView.Adapter` que receba uma lista de objetos `Contato`.
3.  **MainActivity**: Configure o RecyclerView com um `LinearLayoutManager`.
4.  **Ação**: Ao clicar em um contato, mostre um `Toast` com o telefone dele.

## Diferencial ✨
Tente usar o **ListAdapter** com **DiffUtil** para que a lista se atualize com animações suaves ao remover um contato.