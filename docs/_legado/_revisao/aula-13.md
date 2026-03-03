# Aula 13 - Sensores e Hardware �

!!! tip "Objetivo"
    **Objetivo**: Aprender a acessar os recursos físicos do dispositivo, como Câmera, GPS (Localização) e Sensores de Movimento (Acelerômetro), entendendo o sistema de permissões em tempo de execução.

---

## 1. O Mundo do Hardware �

Diferente da Web, o App Nativo tem acesso direto aos sensores do celular.
Os principais são:
*   **Movimento**: Acelerômetro, Giroscópio.
*   **Posição**: GPS, Magnetômetro (Bússola).
*   **Ambiente**: Luz, Barômetro (Pressão), Temperatura.
*   **Interface**: Câmera, Microfone, Biometria (Digital/Rosto).

---

## 2. Permissões (Permissions) 🔑

No Android, as permissões são divididas em duas categorias:

1.  **Normais**: Não oferecem risco à privacidade (ex: Bluetooth, Internet). Definidas apenas no `AndroidManifest.xml`.
2.  **Perigosas**: Acessam dados sensíveis (ex: Câmera, GPS, Contatos). Precisam ser pedidas ao usuário **em tempo de execução** (pop-up).

### Solicitando Permissão (Moderno)

```kotlin
val requestPermissionLauncher = registerForActivityResult(
    ActivityResultContracts.RequestPermission()
) { isGranted: Boolean ->
    if (isGranted) {
        // Permissão concedida! Abrir câmera...
    } else {
        // Permissão negada... explicar por que precisa.
    }
}

// Chamar quando precisar
requestPermissionLauncher.launch(Manifest.permission.CAMERA)
```

---

## 3. Localização e GPS 🗺️

Para obter a localização, usamos o **Fused Location Provider** (parte do Google Play Services). Ele é mais inteligente e economiza bateria.

```kotlin
val fusedLocationClient = LocationServices.getFusedLocationProviderClient(this)

fusedLocationClient.lastLocation.addOnSuccessListener { location : Location? ->
    // Got last known location. In some rare situations this can be null.
    location?.let {
        val lat = it.latitude
        val long = it.longitude
    }
}
```

---

## 4. Sensores de Movimento 🎢

O Android usa o `SensorManager` para escutar dados do acelerômetro, por exemplo.

```kotlin
val sensorManager = getSystemService(Context.SENSOR_SERVICE) as SensorManager
val sensor = sensorManager.getDefaultSensor(Sensor.TYPE_ACCELEROMETER)

val listener = object : SensorEventListener {
    override fun onSensorChanged(event: SensorEvent?) {
        val x = event?.values?.get(0) // Inclinação X
        // ...
    }
    override fun onAccuracyChanged(s: Sensor?, a: Int) {}
}

sensorManager.registerListener(listener, sensor, SensorManager.SENSOR_DELAY_NORMAL)
```

---

## 5. Câmera (CameraX) 📸

O Google criou a biblioteca **CameraX** para facilitar o uso da câmera, que era muito complexo antigamente. Ela lida com as diferenças entre fabricantes automaticamente.

Principais casos de uso:
1.  **Preview**: Ver a imagem na tela.
2.  **Image Capture**: Tirar foto e salvar.
3.  **Image Analysis**: Ler QR Code ou detectar rostos em tempo real.

---

## 6. Bluetooth e Dispositivos Embarcados 🔵

Muitas vezes o app precisa falar com um Arduino, ESP32 ou fone de ouvido.
*   **Bluetooth Classic**: Para áudio e transferência de arquivos grande.
*   **BLE (Bluetooth Low Energy)**: Para sensores e wearables. Economiza muita bateria.

```kotlin
// Exemplo simplificado de scan
val bluetoothAdapter: BluetoothAdapter? = BluetoothAdapter.getDefaultAdapter()
bluetoothAdapter?.startDiscovery() 
```

---

## 7. Telefonia e SMS 📞

O Android permite que seu app interaja com as funções de telefone.
*   **Fazer Chamadas**: Precisa de permissão `CALL_PHONE`.
*   **Enviar SMS**: Use `SmsManager`.

```kotlin
val smsManager: SmsManager = SmsManager.getDefault()
smsManager.sendTextMessage("numero", null, "Olá Mundo!", null, null)
```

---

## 8. Mapas e Orientação 🗺️

Além de saber a latitude, podemos mostrar isso visualmente.
*   **Google Maps SDK**: A biblioteca padrão para exibir mapas, desenhar rotas e colocar marcadores.
*   **Geocoding**: Transformar coordenadas (lat/long) em endereços reais (Rua X, nº 10).

---

## 9. Biometria (Impressão Digital) ☝️

O `BiometricPrompt` exibe aquela janela padrão do sistema para o usuário colocar o dedo ou olhar para a câmera.

### 🆚 Comparação: Core Motion e CameraControl (iOS)
No iOS, o framework `Core Motion` lida com sensores, e a `AVFoundation` lida com a Câmera. O sistema de permissões do iOS é ainda mais rígido desde o início.

---

## 7. Desafio: O Detector de Balanço shake
Crie um app que:
1.  Escute o acelerômetro.
2.  Se o valor de aceleração passar de um limite (usuário balançou o celular), mude a cor de fundo da tela para uma cor aleatória.
3.  Imprima no Logcat: "Balanço detectado!".

---

**Próxima Aula**: Como garantir que seu código não quebre? [Testes e Debugging](./aula-14.md) 🐞