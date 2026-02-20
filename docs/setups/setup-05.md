# Setup 05: .NET (C# e F#) 🔷

## 1. .NET SDK
Necessário para rodar C# e F#.
1.  Baixe o **.NET 8.0 SDK (LTS)** em [dotnet.microsoft.com](https://dotnet.microsoft.com/download).
2.  Instale.
3.  Teste: `dotnet --version`.

## 2. Visual Studio Community
A IDE mais completa para Windows.
1.  Baixe em [visualstudio.microsoft.com](https://visualstudio.microsoft.com/vs/community/).
2.  No instalador, selecione a carga de trabalho: **"Desenvolvimento para desktop com .NET"**.

## 3. VS Code + C# Dev Kit
Para uma experiência mais leve:
1.  Instale a extensão "C# Dev Kit" da Microsoft.

## 4. Solução de Problemas Comuns ⚠️

*   **'dotnet' não encontrado**: Reinicie o computador após instalar o SDK.
*   **Erro de Certificado HTTPS**: Na primeira execução, rode `dotnet dev-certs https --trust` para confiar no certificado local.
*   **OmniSharp Error**: Se o VS Code reclamar, verifique se instalou o **C# Dev Kit** e se o SDK é compatível.