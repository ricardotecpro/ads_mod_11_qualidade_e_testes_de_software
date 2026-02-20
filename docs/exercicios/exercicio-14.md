# Exercícios: Aula 14 - Testes de API 📡

## 🟢 Básico

1.  **Métodos HTTP**: Relacione o Verbo HTTP com sua ação:
    - GET -> ?
    - POST -> ?
    - DELETE -> ?
    - PUT -> ?
2.  **Status Codes**: O que significa quando uma API retorna o status **404 Not Found**?

## 🟡 Intermediário

3.  **Autenticação**: Como funciona o teste de uma API que exige um **Token JWT**? Onde esse token deve ser enviado na requisição?
4.  **Payload JSON**: Em um método **POST**, qual a função do "Body" (Corpo) da requisição? Dê um exemplo simples de um JSON de criação de usuário.

## 🔴 Desafio

5.  **Cenário de Erro**: Você está testando uma API de transferência bancária.
    - O sistema deve retornar **200 OK** se houver saldo.
    - O sistema deve retornar **400 Bad Request** se o saldo for insuficiente.
    - **Escreva como você estruturaria** um teste no Postman para garantir que o sistema não permita transferências sem saldo, validando o Status Code e a mensagem de erro no JSON de resposta.
