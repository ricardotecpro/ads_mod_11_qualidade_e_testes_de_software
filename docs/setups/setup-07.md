# Setup 07: Git & GitHub 🐙

Versionamento de código é o que separa um testador manual de um QA Automation profissional.

## 1. Instalando o Git
1.  Baixe em [git-scm.com](https://git-scm.com/).
2.  Configure sua identidade:
    ```bash
    git config --global user.name "Seu Nome"
    git config --global user.email "seu@email.com"
    ```

## 2. GitHub Acadêmico
Crie uma conta no GitHub para hospedar seus repositórios de estudo e portfólio de automação.

## 3. GitHub Desktop (Opcional)
Se preferir uma interface visual ao invés do terminal:
1.  Baixe em [desktop.github.com](https://desktop.github.com/).

## 4. Workflow de QA
Sempre crie branches para novos testes:
`git checkout -b feature/testes-login`

## 5. Solução de Problemas ⚠️
*   **Erro de Autenticação**: Use o **GitHub CLI** ou configure chaves SSH para não precisar digitar senha a todo momento.
*   **Conflitos**: Se o "Merge" falhar, use o VS Code para resolver os conflitos de linha por linha.