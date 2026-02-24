# Setup 09: Bancos de Dados para QA 🗄️

Saber manipular dados é vital para criar massas de teste e verificar a persistência.

## 1. DBeaver (Ferramenta Universal)
A melhor ferramenta para conectar em qualquer banco (SQL, NoSQL).
1.  Baixe em [dbeaver.io](https://dbeaver.io/).

## 2. SQLite (Para Estudos)
Leve e não exige instalação de servidor. Ótimo para treinar SELECT, INSERT e DELETE.

## 3. PostgreSQL / MySQL
Os bancos mais comuns no mercado. Você pode rodá-los via Docker (conforme vimos no Setup 08).

## 4. Verificação de Dados
Sempre compare o que o seu teste automatizado diz com o que está gravado no banco de dados.

## 5. Solução de Problemas ⚠️
*   **Erro de Driver**: O DBeaver baixa os drivers automaticamente, mas você precisa de internet na primeira conexão de cada tipo de banco.
*   **Query Lenta**: Verifique se o banco não está bloqueado por outra transação (Deadlock).