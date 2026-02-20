# Quiz 13 - Sensores e Hardware 📸

1. Qual a diferença entre permissões "Normais" e "Perigosas" no Android?
    - [ ] Normais são para o modo avião e Perigosas para quando a bateria está baixa
    - [x] Normais são aceitas automaticamente; Perigosas exigem que o usuário autorize em um pop-up
    - [ ] Normais são apenas para o Google e Perigosas para o desenvolvedor
    - [ ] Não existem permissões normais no Android modern
    *Explicação: Por segurança, o Android exige que o usuário dê consentimento explícito para acessar dados sensíveis como Câmera e GPS.*

2. Qual componente é responsável por gerenciar e descobrir os sensores físicos no Android?
    - [ ] HardwareManager
    - [x] SensorManager
    - [ ] AndroidPhysicsEngine
    - [ ] GoogleSensors
    *Explicação: O SensorManager permite listar e ouvir eventos de todos os sensores disponíveis no aparelho.*

3. Por que o Google recomenda o "Fused Location Provider" em vez do GPS puro?
    - [ ] Porque ele é mais caro
    - [x] Porque ele combina GPS, Wi-Fi e sensores para dar a localização com mais precisão e menos gasto de bateria
    - [ ] Porque ele funciona sem satélites
    - [ ] Porque ele só funciona em carros
    *Explicação: É uma camada inteligente que otimiza a obtenção da posição global.*

4. Qual biblioteca moderna do Jetpack facilita o uso da câmera em diferentes aparelhos?
    - [ ] CameraPro
    - [x] CameraX
    - [ ] OpenCamera
    - [ ] AndroidLens
    *Explicação: A CameraX resolve o problema da fragmentação de câmeras entre diferentes fabricantes (Samsung, Xiaomi, etc).*

5. O que faz o método `registerForActivityResult` no contexto de permissões?
    - [ ] Tira uma foto do usuário
    - [x] Cria um contrato para pedir a permissão e receber a resposta (Aceito ou Negado) de forma limpa
    - [ ] Salva a permissão no banco de dados
    - [ ] Envia um e-mail para o Google
    *Explicação: É a forma moderna recomendada pelo Google para lidar com fluxos de permissão.*

6. Para que serve o `Acelerômetro`?
    - [ ] Medir a velocidade da internet
    - [x] Detectar a aceleração e inclinação do celular (usado para girar a tela ou detectar agitos)
    - [ ] Medir a luz ambiente
    - [ ] Identificar a digital do usuário
    *Explicação: Ele mede mudanças na velocidade de movimento do aparelho nos eixos X, Y e Z.*

7. Quando você deve parar de ouvir um sensor (`unregisterListener`)?
    - [ ] Nunca, o Android faz isso sozinho
    - [x] No onStop() ou onDestroy() da Activity, para economizar bateria e memória
    - [ ] Somente quando o celular for desligado
    - [ ] Quando o usuário fechar o olho
    *Explicação: Sensores consomem muita energia. Devemos pará-los sempre que a tela não estiver visível.*

8. O que é o BLE (Bluetooth Low Energy)?
    - [ ] Um Bluetooth que não funciona direito
    - [x] Uma versão do Bluetooth otimizada para baixo consumo de energia, usada em wearables e sensores
    - [ ] O Bluetooth do iPhone
    - [ ] Uma tecnologia que substitui o Wi-Fi
    *Explicação: O BLE permite que dispositivos fiquem conectados por meses com uma única bateria de relógio.*

9. Qual a função do `GPS` no hardware do smartphone?
    - [ ] Medir a pressão atmosférica
    - [x] Receber sinais de satélites para determinar a posição exata (Latitude e Longitude)
    - [ ] Tirar fotos do espaço
    - [ ] Abrir o portão da garagem
    *Explicação: O Global Positioning System é o sensor fundamental para apps de mapas e entregas.*

10. Como o iOS chama o framework equivalente ao SensorManager do Android?
    - [ ] AppleSensors
    - [x] Core Motion
    - [ ] UIKit Motion
    - [ ] iOSPhysicalManager
    *Explicação: O Core Motion é o responsável por centralizar os dados de movimento no iPhone.*