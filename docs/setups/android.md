# Setup do Ambiente: Android Studio 📱

Para quem deseja explorar testes mobile (Appium), o Android Studio é essencial.

## 1. Instalação
Baixe em [developer.android.com/studio](https://developer.android.com/studio).

## 2. Componentes Necessários (SDK)
No "SDK Manager", certifique-se de instalar:
- Uma versão estável do **Android SDK** (ex: Android 13.0).
- **Android SDK Platform-Tools**.
- **Android Emulator**.

## 3. Criando um Emulador (AVD)
- Vá em "Device Manager".
- Clique em "Create Device".
- Escolha um modelo (ex: Pixel 6).
- Baixe a imagem do sistema e finalize.

## 4. Variáveis de Ambiente (PATH)
Adicione o caminho da pasta `platform-tools` às variáveis de ambiente do seu sistema para conseguir usar o comando `adb`.

---
> [!WARNING]
> Emuladores Android consomem muita memória RAM (mínimo de 8GB recomendado no PC).
