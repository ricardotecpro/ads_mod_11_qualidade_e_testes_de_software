# Projeto 02 - Modelagem de Fluxo de Gateway 🏗️

**Objetivo**: Entender o roteamento e a agregação de dados em um Gateway.

## O Desafio
Imagine que você tem dois serviços:
- **Serviço A (User)**: Retorna `{ "id": 1, "nome": "Ricardo" }`
- **Serviço B (Orders)**: Retorna `[ { "id": 101, "valor": 50.0 }, { "id": 102, "valor": 30.0 } ]`

1.  Desenhe um diagrama (pode ser no Mermaid ou papel) onde um **API Gateway** recebe uma chamada em `/dashboard/1` e busca os dados nos dois serviços.
2.  Escreva o JSON final que o Gateway entregaria para o Frontend, unindo as informações do usuário e seus pedidos.
3.  Pesquisa: Liste 3 ferramentas famosas de API Gateway de mercado (ex: Kong, AWS API Gateway, etc).

## O que entregar?
- O diagrama de fluxo.
- O JSON de resposta agregada.
- A lista de ferramentas pesquisadas.