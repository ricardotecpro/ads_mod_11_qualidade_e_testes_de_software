# Exercícios 02 - Arquitetura e Gateway 🏗️

## 🟢 Fáceis

1.  **Conceitos**: Explique o que é um API Gateway com uma analogia da vida real (ex: uma recepção de hotel).
2.  **Síncrono vs Assíncrono**: Diferencie os dois modelos de comunicação em uma frase cada.

## 🟡 Médios

3.  **Resiliência**: O que acontece com um sistema distribuído que só usa comunicação síncrona se o serviço de banco de dados ficar muito lento? Como isso afeta o usuário final?
4.  **Segurança**: Por que é melhor colocar a lógica de autenticação no API Gateway do que repetir em cada um dos 20 microsserviços?

## 🔴 Desafio

5.  **Cenário de Falha Crítica**:
    O serviço de "Notificação" (envio de e-mail e SMS) está fora do ar.
    *   Se o seu sistema for **síncrono**, o usuário conseguirá finalizar uma compra? 
    *   Como a abordagem **assíncrona** com filas resolveria esse problema, garantindo que o e-mail seja enviado quando o serviço voltar?
    *   Cite um exemplo de serviço que **precisa** ser síncrono (não pode esperar).
