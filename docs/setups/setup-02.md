# Setup 02: Testes de API (Postman & Insomnia) 📡

Para testar o backend e os endpoints do sistema, precisamos de clientes de API robustos.

## 1. Postman
O Postman é a ferramenta mais completa para gestão de coleções de API e automação de testes contratuais.

*   **Download**: [postman.com/downloads](https://www.postman.com/downloads/).
*   **Principais Funções**: 
    - Criação de Ambientes (Environments).
    - Scripts de testes em JavaScript.
    - Runner de coleções.

## 2. Insomnia
Uma alternativa leve e focada em design, excelente para testes rápidos e suporte nativo a GraphQL e gRPC.

*   **Download**: [insomnia.rest/download](https://insomnia.rest/download).

## 3. Newman (CLI para Postman)
Para rodar seus testes do Postman em pipelines de CI/CD:
```bash
npm install -g newman
```

## 4. Dica de Produtividade 🚀
Sempre documente o `base_url` em uma variável de ambiente no Postman. Assim, você alterna entre `http://localhost:3000` (desenvolvimento) e `https://api.empresa.com` (produção) com apenas um clique.

## 5. Solução de Problemas ⚠️
*   **Erro de SSL**: Se estiver testando em ambiente local com HTTPS sem certificado válido, desabilite a "SSL Certificate Verification" nas configurações da ferramenta.
*   **CORS**: Alguns navegadores barram requisições, mas ferramentas como Postman e Insomnia ignoram regras de CORS, facilitando os testes.