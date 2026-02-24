# Setup 08: Docker para QA 🐳

O Docker permite rodar ambientes inteiros (Bancos, APIs, Selenium Grid) sem sujar sua máquina local.

## 1. Docker Desktop
1.  Baixe em [docker.com/products/docker-desktop](https://www.docker.com/products/docker-desktop/).
2.  **IMPORTANTE**: No Windows, certifique-se de que o **WSL 2** está instalado e ativo.

## 2. Selenium Grid em Container
Para rodar testes em paralelo em diferentes navegadores:
```bash
docker run -d -p 4444:4444 --name selenium-grid selenium/standalone-chrome
```

## 3. Docker Compose
Use arquivos `docker-compose.yml` para subir seu app + banco de dados para testes em um único comando.

## 4. Limpeza
Para não ficar sem espaço em disco:
`docker system prune`

## 5. Solução de Problemas ⚠️
*   **Engine not running**: Verifique se o ícone da baleia está verde na barra de tarefas.
*   **Falta de RAM**: O Docker consome bastante memória. Aumente o limite nas configurações do Docker Desktop se os containers caírem.