# Aula 13 - Sensores e Hardware 📸
## Além da tela do celular

---

## Agenda 📅

1. O Mundo do Hardware { .fragment }
2. Permissões em Tempo de Execução { .fragment }
3. Localização (GPS) { .fragment }
4. Câmera (CameraX) { .fragment }
5. Acelerômetro e Giroscópio { .fragment }

---

## 1. Sensores de Bolso 📱

- O Smartphone é um laboratório. { .fragment }
- **Acelerômetro**: Movimento. { .fragment }
- **GPS**: Localização. { .fragment }
- **Microfone/Câmera**: Multimídia. { .fragment }

---

## 2. Permissões 🔑

- **Normais**: Internet, Bluetooth (aceitas no Install). { .fragment }
- **Perigosas**: Câmera, Contatos, GPS (pedidas no Runtime). { .fragment }

```kotlin
requestPermissionLauncher.launch(Manifest.permission.CAMERA)
```

---

## 3. Localização (GPS) 🗺️

- **Fused Location Provider**: O jeito Google de economizar bateria. { .fragment }
- Combina Satélite + Wi-Fi + Torres de Celular. { .fragment }

---

## 4. Sensores de Movimento 🎢

- `SensorManager`: O portal de sensores. { .fragment }
- **Acelerômetro**: Detecta o "Shake" (agito). { .fragment }
- **Importante**: Desligue no `onStop` para não gastar bateria! { .fragment }

---

## 5. CameraX 📸

- Biblioteca moderna para não sofrer com a câmera. { .fragment }
- **Use Cases**: Preview, Tirar Foto, Analisar QR Code. { .fragment }

---

## 6. Biometria e Bluetooth ☝️🔵

- **Biometria**: Login seguro e fácil. { .fragment }
- **BLE**: Bluetooth de baixa energia para smartwatches. { .fragment }

---

## 7. Melhores Práticas 🏆

- Explique ao usuário POR QUE você precisa da permissão. { .fragment }
- Tenha um plano B se o sensor não existir no aparelho. { .fragment }

---

## Desafio de Hardware ⚡

Qual sensor é usado para saber se o usuário está com o celular no ouvido e apagar a tela?

---

## Resumo ✅

- Permissões garantem a privacidade. { .fragment }
- Fused Location é melhor que GPS Puro. { .fragment }
- CameraX simplificou o mundo das fotos. { .fragment }

---

## Próxima Aula: Testes e Debug 🐞

- Como encontrar bugs e garantir que o app não quebre. { .fragment }

---

## Dúvidas? 📸