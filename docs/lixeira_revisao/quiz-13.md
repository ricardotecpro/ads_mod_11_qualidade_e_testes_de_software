# Quiz 13 - Hardware e Sensores 📸

--8<-- "assets/quiz.html"

<div class="quiz-container">
  <div class="quiz-question">1. No Android, o que diferencia uma permissão "Normal" de uma permissão "Perigosa"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Por segurança, o Android exige que o usuário aprove explicitamente o acesso a hardware e dados privados.">Permissões normais são pagas, perigosas são gratuitas.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Por segurança, o Android exige que o usuário aprove explicitamente o acesso a hardware e dados privados.">Permissões perigosas acessam dados sensíveis (Câmera, GPS) e precisam de aprovação do usuário em tempo de execução.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Por segurança, o Android exige que o usuário aprove explicitamente o acesso a hardware e dados privados.">Permissões normais só funcionam em tablets.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Por segurança, o Android exige que o usuário aprove explicitamente o acesso a hardware e dados privados.">Não há diferença, todas precisam de pop-up.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">2. Qual componente é recomendado pelo Google para obter a localização (GPS) do usuário de forma eficiente e com baixo consumo de bateria?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Fused Location combina dados de GPS, Wi-Fi e sensores para dar a melhor localização com o menor gasto de energia.">GPSManager</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Fused Location combina dados de GPS, Wi-Fi e sensores para dar a melhor localização com o menor gasto de energia.">SatelliteSearcher</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O Fused Location combina dados de GPS, Wi-Fi e sensores para dar a melhor localização com o menor gasto de energia.">Fused Location Provider (Google Play Services)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O Fused Location combina dados de GPS, Wi-Fi e sensores para dar a melhor localização com o menor gasto de energia.">MapLocationKit</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">3. Qual biblioteca moderna do Jetpack facilita o uso da câmera, resolvendo problemas de compatibilidade entre diferentes fabricantes?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O CameraX abstrai a complexidade do hardware da câmera, garantindo que o preview e a captura funcionem em quase qualquer celular.">CameraApp</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O CameraX abstrai a complexidade do hardware da câmera, garantindo que o preview e a captura funcionem em quase qualquer celular.">PhotoLoader</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O CameraX abstrai a complexidade do hardware da câmera, garantindo que o preview e a captura funcionem em quase qualquer celular.">CameraX</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O CameraX abstrai a complexidade do hardware da câmera, garantindo que o preview e a captura funcionem em quase qualquer celular.">OpenCamera</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">4. Qual sensor é usado para detectar a inclinação ou o balanço (shake) do celular?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O acelerômetro mede a aceleração em 3 eixos (X, Y, Z), permitindo detectar movimentos bruscos.">Termômetro</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O acelerômetro mede a aceleração em 3 eixos (X, Y, Z), permitindo detectar movimentos bruscos.">Barômetro</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O acelerômetro mede a aceleração em 3 eixos (X, Y, Z), permitindo detectar movimentos bruscos.">Acelerômetro</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O acelerômetro mede a aceleração em 3 eixos (X, Y, Z), permitindo detectar movimentos bruscos.">Sensor de Luz</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">5. Para que serve o `SensorManager` no Android?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O SensorManager é o portal de acesso a quase todos os sensores de ambiente e movimento.">Para tirar fotos.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O SensorManager é o portal de acesso a quase todos os sensores de ambiente e movimento.">Para gerenciar a bateria.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O SensorManager é o portal de acesso a quase todos os sensores de ambiente e movimento.">Para listar e registrar ouvintes (listeners) para os sensores físicos do dispositivo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O SensorManager é o portal de acesso a quase todos os sensores de ambiente e movimento.">Para aumentar o volume do toque.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">6. Qual tecnologia sem fio é ideal para conectar o app a sensores de baixo consumo, como relógios inteligentes (wearables) e sensores de saúde?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O BLE permite que dispositivos fiquem conectados por longos períodos gastando o mínimo de energia.">Bluetooth Classic</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O BLE permite que dispositivos fiquem conectados por longos períodos gastando o mínimo de energia.">BLE (Bluetooth Low Energy)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O BLE permite que dispositivos fiquem conectados por longos períodos gastando o mínimo de energia.">Infravermelho</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O BLE permite que dispositivos fiquem conectados por longos períodos gastando o mínimo de energia.">NFC</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">7. Como o app pode enviar um SMS automaticamente (com permissão do usuário)?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O SmsManager permite enviar mensagens de texto diretamente sem abrir o app de mensagens padrão.">Usando o comando `intent.sendSMS()`</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! O SmsManager permite enviar mensagens de texto diretamente sem abrir o app de mensagens padrão.">Usando a classe `SmsManager`</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O SmsManager permite enviar mensagens de texto diretamente sem abrir o app de mensagens padrão.">Chamando a API do Google Maps</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. O SmsManager permite enviar mensagens de texto diretamente sem abrir o app de mensagens padrão.">Não é possível enviar SMS por apps nativos.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">8. O que é "Geocoding"?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Útil para mostrar o nome da rua onde o usuário está baseado apenas no seu GPS.">O código secreto do Google.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Útil para mostrar o nome da rua onde o usuário está baseado apenas no seu GPS.">Um filtro de fotos.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Útil para mostrar o nome da rua onde o usuário está baseado apenas no seu GPS.">O processo de converter um endereço (rua, número) em coordenadas geográficas (lat/long) ou vice-versa.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Útil para mostrar o nome da rua onde o usuário está baseado apenas no seu GPS.">Aumentar o zoom do mapa.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">9. Qual o papel do `BiometricPrompt`?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele garante que o app use o método de biometria seguro e padronizado do celular.">Tirar uma selfie do usuário.</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! Ele garante que o app use o método de biometria seguro e padronizado do celular.">Exibir a interface padrão do sistema para autenticação via Digital ou Reconhecimento Facial.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele garante que o app use o método de biometria seguro e padronizado do celular.">Medir a pressão arterial pelo dedo.</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. Ele garante que o app use o método de biometria seguro e padronizado do celular.">Guardar as senhas do usuário no banco.</div>
  <div class="quiz-feedback"></div>
</div>

<div class="quiz-container">
  <div class="quiz-question">10. No iOS, qual é o framework responsável por acessar sensores de movimento e GPS?</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A Apple divide as responsabilidades em frameworks específicos, sendo o Core Location para GPS e Core Motion para sensores.">CoreMedia</div>
  <div class="quiz-option" data-correct="true" data-feedback="✅ Correto! A Apple divide as responsabilidades em frameworks específicos, sendo o Core Location para GPS e Core Motion para sensores.">Core Motion (e Core Location)</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A Apple divide as responsabilidades em frameworks específicos, sendo o Core Location para GPS e Core Motion para sensores.">AVKit</div>
  <div class="quiz-option" data-correct="false" data-feedback="❌ Incorreto. A Apple divide as responsabilidades em frameworks específicos, sendo o Core Location para GPS e Core Motion para sensores.">HealthKit</div>
  <div class="quiz-feedback"></div>
</div>
