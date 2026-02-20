# Exercícios 08 - Persistência de Dados 💾

## 🟢 Fáceis

1.  **Escolha**: Para salvar apenas "Som ligado/desligado", qual a opção mais adequada: SQLite, SharedPreferences ou Arquivo de Texto?
2.  **Room**: O que é uma `@Entity` no Room?

## 🟡 Médios

3.  **Threads**:
    Por que o Android proíbe acesso ao banco de dados na Main Thread? O que acontece se tentarmos fazer isso?
4.  **DAO**:
    O que significa a sigla DAO e qual sua função no Room?

## 🔴 Desafio

5.  **Migração**:
    Você lançou o app com a tabela `Usuario(id, nome)`.
    Na versão 2.0, você precisa adicionar o campo `idade`.
    *   O que acontece se você rodar o app novo em um celular que tem o banco antigo, sem configurar uma "Migration"?
    *   Como o Room lida com controle de versão do banco?