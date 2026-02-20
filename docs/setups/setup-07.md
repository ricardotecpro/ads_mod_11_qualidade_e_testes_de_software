# Setup 07: Sistemas (Rust e Go) ⚙️

## Rust 🦀
O Rust usa o gerenciador `rustup`.
1.  Acesse [rustup.rs](https://rustup.rs/).
2.  Baixe e execute o `rustup-init`.
3.  Aceite o padrão (opção 1).
4.  Reinicie o terminal e teste: `cargo --version`.
5.  **VS Code**: Instale a extensão "rust-analyzer".

## Go (Golang) 🐹
1.  Baixe em [go.dev](https://go.dev/dl/).
2.  Instale (Next, Next, Finish).
3.  Teste: `go version`.
4.  **VS Code**: Instale a extensão "Go" oficial.

## 4. Solução de Problemas Comuns ⚠️

*   **'cargo' não encontrado**: Reinicie o terminal. Se não funcionar, adicione `~/.cargo/bin` (Linux/Mac) ou `%USERPROFILE%\.cargo\bin` (Windows) ao PATH.
*   **Go Path**: Certifique-se de que a variável `GOPATH` está configurada corretamente (geralmente `C:\Users\SeuUsuario\go`).
*   **Erro de Linker (Rust)**: No Windows, pode faltar as ferramentas de build do C++. Baixe o "Build Tools for Visual Studio".