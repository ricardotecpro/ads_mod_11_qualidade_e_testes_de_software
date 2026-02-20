# Projeto 08 - Lista de Compras (Room) 💾

**Objetivo**: Persistir dados localmente usando SQLite (Room).

## O Desafio
Crie um app para salvar itens de uma lista de compras:
1.  **Entity**: `Item(id, nome)`.
2.  **DAO**: Métodos para Inserir e Listar todos os itens.
3.  **Interface**: Campo de texto para o nome do item e botão "Adicionar".
4.  Exiba os itens salvos em um `TextView` simples (concatenados) — na próxima aula usaremos listas reais!

## Atenção ⚠️
Lembre-se de rodar a inserção no banco dentro de uma coroutine (`lifecycleScope.launch` ou `viewModelScope.launch`) para não travar a UI Thread.