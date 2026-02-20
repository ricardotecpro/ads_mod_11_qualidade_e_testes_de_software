# Exercícios: Aula 05 - Melhores Práticas ✨

## 🟢 Básico

1.  **Nomenclatura**: Refatore os nomes das variáveis abaixo seguindo os princípios do Clean Code:
    - `d`: data de vencimento do boleto.
    - `u_ativo`: booleano que indica se o usuário está logado.
    - `lista1`: lista contendo nomes de arquivos de log.
2.  **Funções**: Segundo o Clean Code, qual a regra de ouro sobre o que uma função deve fazer e qual deve ser o seu tamanho ideal?

## 🟡 Intermediário

3.  **DRY vs WET**: Explique por que o princípio **DRY (Don't Repeat Yourself)** é um forte aliado dos testes automatizados. O que acontece com a manutenção dos testes quando o código é "WET" (Write Everything Twice)?
4.  **Refatoração**: Imagine um código que possui 1000 linhas em um único método. Quais seriam as duas primeiras técnicas de refatoração (ex: extrair método) que você aplicaria para facilitar a criação de testes unitários?

## 🔴 Desafio

5.  **Revisão de Código (Code Review)**: Você recebeu para revisar um código onde todas as validações de banco de dados estão misturadas com a lógica de interface (HTML/JS). Escreva um breve comentário (feedback) para o desenvolvedor explicando por que essa falta de **Separação de Preocupações** prejudica a testabilidade do sistema.
