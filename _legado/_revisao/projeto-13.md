# Projeto 13 - Detector de Agito (Shake) 🎢

**Objetivo**: Acessar o hardware do dispositivo (Acelerômetro).

## O Desafio
Crie um app que detecta quando o usuário balança o celular:
1.  Obtenha o `SensorManager` e o sensor `TYPE_ACCELEROMETER`.
2.  Calcule a aceleração total (vetor resultante de X, Y e Z).
3.  Defina um limite (Ex: > 12m/s²).
4.  Quando o limite for atingido, toque um som curto ou faça o celular vibrar (`Vibrator`).
5.  Mude a cor de fundo da tela para uma cor aleatória.

## Nota
Teste esse projeto em um celular real se possível, pois emuladores nem sempre simulam o acelerômetro corretamente! 📱