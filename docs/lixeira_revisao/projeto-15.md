# Projeto 15 - Gerando o App Bundle 📦

**Objetivo**: Preparar o aplicativo para o lançamento real.

## O Desafio
Desta vez o desafio é técnico e de configuração:
1.  Crie uma **Keystore** (.jks) protegida por senha.
2.  Configure o `signingConfigs` no seu `build.gradle` para usar essa chave.
3.  Habilite o **R8/ProGuard** (`minifyEnabled true`).
4.  Vá em `Build > Generate Signed Bundle / APK`.
5.  Gere o arquivo `.aab`.

## Reflexão
Qual o tamanho final do seu `.aab` comparado ao `.apk` gerado anteriormente? Observe a diferença! ⚖️