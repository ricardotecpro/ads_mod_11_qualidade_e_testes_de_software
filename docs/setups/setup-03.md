# Setup 03: Ferramentas de Apoio 🛠️

Além da IDE, você precisará de ferramentas para gerenciar código e testar dados.

## 1. Git e GitHub
Essencial para versionamento.
*   **Download**: [git-scm.com](https://git-scm.com/).
*   **Configuração Inicial**:
    ```bash
    git config --global user.name "Seu Nome"
    git config --global user.email "seu@email.com"
    ```

## 2. Postman ou Insomnia
Para testar as APIs REST antes de escrever código Kotlin/Swift.
*   **Postman**: [postman.com](https://www.postman.com/).
*   **Insomnia**: [insomnia.rest](https://insomnia.rest/).

## 3. Vysor (Opcional)
Para espelhar a tela do seu celular real no computador (via cabo USB).
*   **Acesso**: [vysor.io](https://www.vysor.io/).

## 4. ADB (Android Debug Bridge)
Já vem com o Android Studio, mas é útil no PATH do sistema.
*   Permite instalar APKs via terminal: `adb install app.apk`.
*   Permite ver logs detalhados: `adb logcat`.

## 5. Flipper (Meta)
Uma ferramenta avançada para debugar bancos de dados SQLite e chamadas de rede direto na interface visual.
*   **Acesso**: [fbflipper.com](https://fbflipper.com/).