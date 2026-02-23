# Exercícios 03 - Modelagem REST 📡

## 🟢 Fáceis

1.  **URI Design**: Corrija as URIs abaixo para seguirem as boas práticas REST:
    *   `GET /listar_todos_usuarios`
    *   `POST /criarNovoPedido`
    *   `DELETE /remover-produto-por-id/123`
2.  **Verbos**: Qual o verbo HTTP mais adequado para atualizar a senha de um usuário? Por que?

## 🟡 Médios

3.  **Status Codes**: Escolha o código de status ideal para as situações:
    *   Usuário tentou deletar um arquivo, mas ele não tem permissão de administrador.
    *   O cadastro foi realizado com sucesso e o sistema retornou os dados do novo usuário.
    *   O servidor caiu por falta de memória.
4.  **Idempotência**: Explique por que o `POST` não é idempotente e o `GET` é.

## 🔴 Desafio

5.  **Design de Contrato**:
    Desenhe as rotas para um sistema de **E-commerce**.
    *   Como seria a URI para listar todos os itens de um carrinho específico?
    *   Como seria a URI para adicionar um item a este carrinho?
    *   Escreva o JSON que representaria um "Item de Carrinho" com: `produto_id`, `nome`, `quantidade` e `preco_unitario`.
