# Setup 02: Xcode (iOS Foundation) 🍎

O Xcode é a ferramenta necessária para compilar e testar apps iOS.

> [!IMPORTANT]
> O Xcode requer um computador **Mac** (macOS).

## 1. Instalação
1.  Abra a **App Store** no seu Mac.
2.  Pesquise por **Xcode**.
3.  Clique em Obter/Instalar.
4.  Após o download, abra o Xcode para carregar os componentes adicionais do macOS.

## 2. Configurando Simuladores
1.  Vá em **Settings > Platforms**.
2.  Verifique se o componente "iOS" está baixado.
3.  Se não estiver, clique em "GET" para baixar a versão mais estável.

## 3. Comandos de Linha (CLI)
Para que ferramentas de automação funcionem, você precisa instalar os Command Line Tools:
```bash
xcode-select --install
```

## 4. Opcional: CocoaPods
Muitos projetos iOS antigos ainda usam CocoaPods para dependências:
```bash
sudo gem install cocoapods
```

## 5. Solução de Problemas ⚠️
*   **Espaço em Disco**: O Xcode é muito grande. Garanta pelo menos 40GB de espaço livre para ele e os simuladores.
*   **Build Lento**: Use simuladores de modelos mais simples (ex: iPhone SE) para poupar memória RAM se necessário.