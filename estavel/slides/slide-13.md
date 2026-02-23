# Aula 13 - Sensores e Hardware 📸
## Além da tela do celular

---

## Agenda 📅

1. O Mundo do Hardware <!-- .element: class="fragment" -->
2. Permissões em Tempo de Execução <!-- .element: class="fragment" -->
3. Localização (GPS) <!-- .element: class="fragment" -->
4. Câmera (CameraX) <!-- .element: class="fragment" -->
5. Acelerômetro e Giroscópio <!-- .element: class="fragment" -->

---

## 1. Sensores de Bolso 📱

- O Smartphone é um laboratório. <!-- .element: class="fragment" -->
- **Acelerômetro**: Movimento. <!-- .element: class="fragment" -->
- **GPS**: Localização. <!-- .element: class="fragment" -->
- **Microfone/Câmera**: Multimídia. <!-- .element: class="fragment" -->

---

## 2. Permissões 🔑

- **Normais**: Internet, Bluetooth (aceitas no Install). <!-- .element: class="fragment" -->
- **Perigosas**: Câmera, Contatos, GPS (pedidas no Runtime). <!-- .element: class="fragment" -->

```kotlin
requestPermissionLauncher.launch(Manifest.permission.CAMERA)
```

---

## 3. Localização (GPS) 🗺️

- **Fused Location Provider**: O jeito Google de economizar bateria. <!-- .element: class="fragment" -->
- Combina Satélite + Wi-Fi + Torres de Celular. <!-- .element: class="fragment" -->

---

## 4. Sensores de Movimento 🎢

- `SensorManager`: O portal de sensores. <!-- .element: class="fragment" -->
- **Acelerômetro**: Detecta o "Shake" (agito). <!-- .element: class="fragment" -->
- **Importante**: Desligue no `onStop` para não gastar bateria! <!-- .element: class="fragment" -->

---

## 5. CameraX 📸

- Biblioteca moderna para não sofrer com a câmera. <!-- .element: class="fragment" -->
- **Use Cases**: Preview, Tirar Foto, Analisar QR Code. <!-- .element: class="fragment" -->

---

## 6. Biometria e Bluetooth ☝️🔵

- **Biometria**: Login seguro e fácil. <!-- .element: class="fragment" -->
- **BLE**: Bluetooth de baixa energia para smartwatches. <!-- .element: class="fragment" -->

---

## 7. Melhores Práticas 🏆

- Explique ao usuário POR QUE você precisa da permissão. <!-- .element: class="fragment" -->
- Tenha um plano B se o sensor não existir no aparelho. <!-- .element: class="fragment" -->

---

## Desafio de Hardware ⚡

Qual sensor é usado para saber se o usuário está com o celular no ouvido e apagar a tela?

---

## Resumo ✅

- Permissões garantem a privacidade. <!-- .element: class="fragment" -->
- Fused Location é melhor que GPS Puro. <!-- .element: class="fragment" -->
- CameraX simplificou o mundo das fotos. <!-- .element: class="fragment" -->

---

## Próxima Aula: Testes e Debug 🐞

- Como encontrar bugs e garantir que o app não quebre. <!-- .element: class="fragment" -->

---

## Dúvidas? 📸