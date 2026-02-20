# Projeto 06 - Navegação entre Telas 🗺️

**Objetivo**: Entender o fluxo de navegação e passagem de parâmetros.

## O Desafio
Crie duas telas:
1.  **Tela Principal**: Campo para digitar o nome de um usuário e botão "Próximo".
2.  **Tela de Boas-Vindas**: Deve receber o nome via Intent e exibir: "Bem-vindo, [Nome]!".
3.  Adicione um botão "Sair" na segunda tela que chama o método `finish()` para retornar à primeira.

## O que observar?
- A String é passada via `putExtra`.
- O app não deve crashar se o nome estiver vazio.