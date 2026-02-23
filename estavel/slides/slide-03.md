# Aula 03 - Modelagem de APIs RESTful 📡
## Recursos, Verbos e Contratos

---

## Agenda 📅

1. O que é REST? <!-- .element: class="fragment" -->
2. Recursos e URIs <!-- .element: class="fragment" -->
3. Verbos HTTP (GET, POST, PUT...) <!-- .element: class="fragment" -->
4. Status Codes <!-- .element: class="fragment" -->
5. JSON: A Linguagem das APIs <!-- .element: class="fragment" -->
6. Boas Práticas de Design <!-- .element: class="fragment" -->

---

## 1. REST: A "Língua" da Web 🌐

- Style arquitetural para sistemas distribuídos. <!-- .element: class="fragment" -->
- Baseado no protocolo **HTTP**. <!-- .element: class="fragment" -->
- Independência entre Client e Server. <!-- .element: class="fragment" -->

---

## Princípios REST

- **Stateless**: Cada requisição é única. <!-- .element: class="fragment" -->
- **Uniform Interface**: Padrões compartilhados. <!-- .element: class="fragment" -->
- **Cacheable**: Melhore a performance. <!-- .element: class="fragment" -->

---

## 2. Identificando Recursos 📍

- Um recurso é qualquer coisa que expomos. <!-- .element: class="fragment" -->
- **URI**: O endereço do recurso. <!-- .element: class="fragment" -->

### O que NÃO fazer:
`GET /obterUsuarios` ❌

### O que fazer:
`GET /usuarios` ✅ (Sempre substantivos no plural!)

---

## 3. Os Verbos HTTP 🛠️

Eles definem a intenção da chamada:

- **GET**: Buscar dados. <!-- .element: class="fragment" -->
- **POST**: Criar novo dado. <!-- .element: class="fragment" -->
- **PUT**: Atualizar (Trocar tudo). <!-- .element: class="fragment" -->
- **PATCH**: Atualizar (Apenas um pedaço). <!-- .element: class="fragment" -->
- **DELETE**: Remover dado. <!-- .element: class="fragment" -->

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

- **2xx**: Deu certo! (200, 201, 204). <!-- .element: class="fragment" -->
- **4xx**: Você (cliente) errou algo (400, 401, 404). <!-- .element: class="fragment" -->
- **5xx**: Eu (servidor) quebrei (500, 503). <!-- .element: class="fragment" -->

---

## 5. O Formato JSON 🏗️

```json
{
  "nome": "Curso Backend",
  "modulo": 1,
  "ativo": true
}
```

- Leve, legível e universal. <!-- .element: class="fragment" -->

---

## 6. Design de URIs Complexas

Como buscar os pedidos de um usuário específico?

`GET /usuarios/123/pedidos` ✅

- Hierarquia lógica e limpa. <!-- .element: class="fragment" -->

---

## 7. Prática: Postman em Ação 💻

- Testando verbos em APIs reais. <!-- .element: class="fragment" -->
- Analisando Headers e Body. <!-- .element: class="fragment" -->

---

## Desafio REST ⚡

Se você quer mudar apenas o e-mail de um usuário, qual verbo deve usar: PUT ou PATCH?

---

## Resumo ✅

- REST é sobre recursos e padrões. <!-- .element: class="fragment" -->
- URIs usam substantivos no plural. <!-- .element: class="fragment" -->
- Status codes guiam o frontend. <!-- .element: class="fragment" -->
- JSON é o padrão de facto. <!-- .element: class="fragment" -->

---

## Próxima Aula: Swagger e Mocks 📝

- Documentação automática. <!-- .element: class="fragment" -->
- Como trabalhar sem o backend pronto? <!-- .element: class="fragment" -->

---

## Dúvidas? 📡