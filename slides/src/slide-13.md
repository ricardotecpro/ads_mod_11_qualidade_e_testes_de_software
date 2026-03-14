# Automação de Testes Web 🤖
## Aula 13 - Playwright e Selenium

---

## Por que automatizar a Web? 🕸️

- Validar a jornada do usuário final
- Reduzir o tempo de testes de regressão repetitivos
- Garantir que fluxos críticos (Logout, Checkout) nunca quebrem

---

## Ferramentas Modernas 🛠️

### Playwright
- Veloz, estável e multiplataforma
- Auto-waiting nativo
- Trace Viewer para debug visual

### Selenium
- O padrão da indústria
- Grande comunidade e suporte a várias linguagens

---

## Localizando Elementos 📍

### Estratégias (Locators):
1.  **ID**: O mais estável
2.  **Test ID**: `data-testid="login"`
3.  **Role**: `getByRole('button')`
4.  **CSS/XPath**: Evite se puder!

---

## Page Object Model (POM) 🏗️

- Trate cada página como um objeto
- Separe os seletores da lógica do teste
- Se a UI mudar, você só altera em um lugar!

---

## Assertions Automáticas ✅

- O robô não apenas clica, ele **valida**
- `expect(page).toHaveURL('/home')`
- `expect(locator).toBeVisible()`

---

## Fim da Aula 13 🏁
### Próximo passo: Testes de API com Postman!
