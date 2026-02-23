# Aula 03 - Modelagem de APIs RESTful 📡
## Recursos, Verbos e Contratos

---

## Agenda 📅

1. O que é REST? { .fragment }
2. Recursos e URIs { .fragment }
3. Verbos HTTP (GET, POST, PUT...) { .fragment }
4. Status Codes { .fragment }
5. JSON: A Linguagem das APIs { .fragment }
6. Boas Práticas de Design { .fragment }

---

## 1. REST: A "Língua" da Web 🌐

- Style arquitetural para sistemas distribuídos. { .fragment }
- Baseado no protocolo **HTTP**. { .fragment }
- Independência entre Client e Server. { .fragment }

---

## Princípios REST

- **Stateless**: Cada requisição é única. { .fragment }
- **Uniform Interface**: Padrões compartilhados. { .fragment }
- **Cacheable**: Melhore a performance. { .fragment }

---

## 2. Identificando Recursos 📍

- Um recurso é qualquer coisa que expomos. { .fragment }
- **URI**: O endereço do recurso. { .fragment }

### O que NÃO fazer:
`GET /obterUsuarios` ❌

### O que fazer:
`GET /usuarios` ✅ (Sempre substantivos no plural!)

---

## 3. Os Verbos HTTP 🛠️

Eles definem a intenção da chamada:

- **GET**: Buscar dados. { .fragment }
- **POST**: Criar novo dado. { .fragment }
- **PUT**: Atualizar (Trocar tudo). { .fragment }
- **PATCH**: Atualizar (Apenas um pedaço). { .fragment }
- **DELETE**: Remover dado. { .fragment }

---

## Idempotência e Segurança

| Verbo | Seguro? | Idempotente? |
| :--- | :--- | :--- |
| GET | Sim ✅ | Sim ✅ |
| POST | Não ❌ | Não ❌ |
| PUT | Não ❌ | Sim ✅ |
| DELETE | Não ❌ | Sim ✅ |

---

## 4. Status Codes: A Resposta 🚦

- **2xx**: Deu certo! (200, 201, 204). { .fragment }
- **4xx**: Você (cliente) errou algo (400, 401, 404). { .fragment }
- **5xx**: Eu (servidor) quebrei (500, 503). { .fragment }

---

## 5. O Formato JSON 🏗️

```json
{
  "nome": "Curso Backend",
  "modulo": 1,
  "ativo": true
}
```

- Leve, legível e universal. { .fragment }

---

## 6. Design de URIs Complexas

Como buscar os pedidos de um usuário específico?

`GET /usuarios/123/pedidos` ✅

- Hierarquia lógica e limpa. { .fragment }

---

## 7. Prática: Postman em Ação 💻

- Testando verbos em APIs reais. { .fragment }
- Analisando Headers e Body. { .fragment }

---

## Desafio REST ⚡

Se você quer mudar apenas o e-mail de um usuário, qual verbo deve usar: PUT ou PATCH?

---

## Resumo ✅

- REST é sobre recursos e padrões. { .fragment }
- URIs usam substantivos no plural. { .fragment }
- Status codes guiam o frontend. { .fragment }
- JSON é o padrão de facto. { .fragment }

---

## Próxima Aula: Swagger e Mocks 📝

- Documentação automática. { .fragment }
- Como trabalhar sem o backend pronto? { .fragment }

---

## Dúvidas? 📡