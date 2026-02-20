# Setup 09: PHP e Servidor Local 🐘

Como o PHP roda no servidor, precisamos simular um servidor no nosso computador.

## 1. XAMPP (Tudo em Um)
O pacote mais fácil. Inclui Apache (Servidor), MySQL (Banco) e PHP.
1.  Baixe em [apachefriends.org](https://www.apachefriends.org/pt_br/index.html).
2.  Instale e abra o **XAMPP Control Panel**.
3.  Clique em **Start** no Apache e MySQL.
4.  Seus arquivos devem ficar na pasta `C:\xampp\htdocs`.

## 2. Composer (Gerenciador de Pacotes)
Essencial para usar bibliotecas modernas e frameworks como Laravel.
1.  Baixe em [getcomposer.org](https://getcomposer.org/).
2.  Instale. Ele deve encontrar seu PHP automaticamente.

## 3. Laravel (Opcional)
Para criar projetos profissionais:
```bash
composer global require laravel/installer
laravel new meu-projeto
```

## 4. Solução de Problemas Comuns ⚠️

*   **Apache não inicia (Port 80 busy)**: Skype ou IIS podem estar usando a porta 80. No XAMPP, vá em Config -> httpd.conf e mude `Listen 80` para `Listen 8080`.
*   **MySQL não conecta**: Verifique se o serviço está verde no XAMPP.
*   **Erro de DLL**: Pode faltar o "Visual C++ Redistributable" no seu Windows. Atualize-o.