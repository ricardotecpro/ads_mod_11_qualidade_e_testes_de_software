# Quiz 13 - Hardware e Sensores 📸

1. No Android, o que diferencia uma permissão "Normal" de uma permissão "Perigosa"?
    - [ ] Permissões normais são pagas, perigosas são gratuitas.
    - [x] Permissões perigosas acessam dados sensíveis (Câmera, GPS) e precisam de aprovação do usuário em tempo de execução.
    - [ ] Permissões normais só funcionam em tablets.
    - [ ] Não há diferença, todas precisam de pop-up.
    *Explicação: Por segurança, o Android exige que o usuário aprove explicitamente o acesso a hardware e dados privados.*

2. Qual componente é recomendado pelo Google para obter a localização (GPS) do usuário de forma eficiente e com baixo consumo de bateria?
    - [ ] GPSManager
    - [ ] SatelliteSearcher
    - [x] Fused Location Provider (Google Play Services)
    - [ ] MapLocationKit
    *Explicação: O Fused Location combina dados de GPS, Wi-Fi e sensores para dar a melhor localização com o menor gasto de energia.*

3. Qual biblioteca moderna do Jetpack facilita o uso da câmera, resolvendo problemas de compatibilidade entre diferentes fabricantes?
    - [ ] CameraApp
    - [ ] PhotoLoader
    - [x] CameraX
    - [ ] OpenCamera
    *Explicação: O CameraX abstrai a complexidade do hardware da câmera, garantindo que o preview e a captura funcionem em quase qualquer celular.*

4. Qual sensor é usado para detectar a inclinação ou o balanço (shake) do celular?
    - [ ] Termômetro
    - [ ] Barômetro
    - [x] Acelerômetro
    - [ ] Sensor de Luz
    *Explicação: O acelerômetro mede a aceleração em 3 eixos (X, Y, Z), permitindo detectar movimentos bruscos.*

5. Para que serve o `SensorManager` no Android?
    - [ ] Para tirar fotos.
    - [ ] Para gerenciar a bateria.
    - [x] Para listar e registrar ouvintes (listeners) para os sensores físicos do dispositivo.
    - [ ] Para aumentar o volume do toque.
    *Explicação: O SensorManager é o portal de acesso a quase todos os sensores de ambiente e movimento.*

6. Qual tecnologia sem fio é ideal para conectar o app a sensores de baixo consumo, como relógios inteligentes (wearables) e sensores de saúde?
    - [ ] Bluetooth Classic
    - [x] BLE (Bluetooth Low Energy)
    - [ ] Infravermelho
    - [ ] NFC
    *Explicação: O BLE permite que dispositivos fiquem conectados por longos períodos gastando o mínimo de energia.*

7. Como o app pode enviar um SMS automaticamente (com permissão do usuário)?
    - [ ] Usando o comando `intent.sendSMS()`
    - [x] Usando a classe `SmsManager`
    - [ ] Chamando a API do Google Maps
    - [ ] Não é possível enviar SMS por apps nativos.
    *Explicação: O SmsManager permite enviar mensagens de texto diretamente sem abrir o app de mensagens padrão.*

8. O que é "Geocoding"?
    - [ ] O código secreto do Google.
    - [ ] Um filtro de fotos.
    - [x] O processo de converter um endereço (rua, número) em coordenadas geográficas (lat/long) ou vice-versa.
    - [ ] Aumentar o zoom do mapa.
    *Explicação: Útil para mostrar o nome da rua onde o usuário está baseado apenas no seu GPS.*

9. Qual o papel do `BiometricPrompt`?
    - [ ] Tirar uma selfie do usuário.
    - [x] Exibir a interface padrão do sistema para autenticação via Digital ou Reconhecimento Facial.
    - [ ] Medir a pressão arterial pelo dedo.
    - [ ] Guardar as senhas do usuário no banco.
    *Explicação: Ele garante que o app use o método de biometria seguro e padronizado do celular.*

10. No iOS, qual é o framework responsável por acessar sensores de movimento e GPS?
    - [ ] CoreMedia
    - [x] Core Motion (e Core Location)
    - [ ] AVKit
    - [ ] HealthKit
    *Explicação: A Apple divide as responsabilidades em frameworks específicos, sendo o Core Location para GPS e Core Motion para sensores.*
