# Setup 01: Android Studio 🤖

O Android Studio é a IDE oficial para o desenvolvimento Android.

## 1. Requisitos de Sistema
*   **RAM**: Mínimo 8GB (Sugerido 16GB+).
*   **Espaço**: Mínimo 10GB para IDE + SDKs.
*   **Processador**: Intel Core i5 ou equivalente.

## 2. Instalação
1.  Acesse o site oficial: [developer.android.com/studio](https://developer.android.com/studio).
2.  Baixe a versão mais recente para o seu Sistema Operacional.
3.  Execute o instalador e escolha a opção "Standard" na configuração inicial.

## 3. Configurando o SDK
*   Após a instalação, vá em **Settings > Languages & Frameworks > Android SDK**.
*   Certifique-se de que a versão mais recente do Android (estável) esteja instalada.
*   Na aba **SDK Tools**, instale o "Android Emulator" e o "Intel x86 Emulator Accelerator (HAXM)" se estiver no Windows com Intel.

## 4. Criando um Emulador (AVD)
1.  Abra o **Device Manager**.
2.  Clique em **Create Device**.
3.  Escolha um dispositivo (ex: Pixel 7).
4.  Selecione uma imagem de sistema (ex: Level 34 - Android 14).
5.  Finalize e clique no "Play" para iniciar o celular virtual.

## 5. Solução de Problemas ⚠️
*   **VT-x is disabled**: Você precisa habilitar a virtualização na BIOS do seu computador.
*   **Studio muito lento**: Adicione a pasta do projeto e as pastas do Android SDK nas exclusões do seu Antivírus.