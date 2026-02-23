# Quiz 02 - Arquitetura e Gateway 🏗️

1. O que acontece na comunicação síncrona (Sync)?
    - [ ] O serviço envia a mensagem e esquece
    - [x] O serviço envia a requisição e aguarda a resposta para continuar
    - [ ] A comunicação só ocorre via rádio
    - [ ] O banco de dados é desligado
    *Explicação: No modelo síncrono, a execução fica bloqueada até que o destino retorne o dado.*

2. Qual o principal perigo da comunicação síncrona em excesso?
    - [ ] O código fica muito curto
    - [x] Cascateamento de falhas (um serviço lento trava todos os outros)
    - [ ] Economia exagerada de memória
    - [ ] O sistema fica rápido demais
    *Explicação: Se um serviço na cadeia falhar ou demorar, todos os serviços "acima" dele também sofrerão.*

3. Qual a função do API Gateway?
    - [ ] Armazenar as senhas dos desenvolvedores
    - [x] Atuar como ponto único de entrada para roteamento e segurança
    - [ ] Substituir o roteador Wi-Fi da empresa
    - [ ] Processar scripts de interface visual
    *Explicação: O Gateway centraliza preocupações transversais como autenticação, log e roteamento.*

4. O que é "Rate Limiting"?
    - [ ] Aumentar a velocidade da internet
    - [x] Limitar a quantidade de requisições que um cliente pode fazer em um tempo
    - [ ] Cobrar por cada clique no botão
    - [ ] Diminuir a fonte do texto
    *Explicação: Rate limiting protege o sistema contra abusos ou ataques de negação de serviço (DoS).*

5. No Service Discovery, como os serviços são localizados?
    - [ ] Por endereços IP fixos escritos no código
    - [x] Via um registro dinâmico que mantém os endereços atualizados
    - [ ] Através de busca no Google
    - [ ] Usando GPS
    *Explicação: Em ambientes elásticos (Docker/K8s), os IPs mudam sempre, exigindo um "Discovery" dinâmico.*

6. Qual o papel do "Load Balancer"?
    - [ ] Medir o peso dos servidores físicos
    - [x] Distribuir a carga de trabalho entre várias instâncias do mesmo serviço
    - [ ] Equilibrar o gasto de energia
    - [ ] Organizar as pastas do projeto
    *Explicação: Ele garante que nenhuma instância fique sobrecarregada enquanto outras estão ociosas.*

7. O que caracteriza a comunicação Assíncrona (Async)?
    - [ ] Uso obrigatório de cabos de fibra ótica
    - [x] O uso de mensageria (filas) onde o chamador não espera a resposta imediata
    - [ ] Comunicação em tempo real por vídeo
    - [ ] Bloqueio total do banco de dados
    *Explicação: É ideal para processos longos ou para aumentar a resiliência do sistema.*

8. O que é um "Circuit Breaker" (Disjuntor)?
    - [ ] Um fusível físico no servidor
    - [x] Um padrão que interrompe chamadas para um serviço falho para evitar sobrecarga
    - [ ] Um hacker que invade sistemas
    - [ ] O botão de desligar do computador
    *Explicação: Ele protege o sistema impedindo que requisições inúteis sejam feitas a um serviço que já se sabe estar fora do ar.*

9. Qual destas é uma responsabilidade típica de um Gateway?
    - [ ] Desenhar o logo da empresa
    - [ ] Compilar código C++
    - [x] Agregação de respostas e Autenticação
    - [ ] Formatar o HD do servidor
    *Explicação: O Gateway pode unir dados de 3 serviços diferentes e entregar um único JSON ao frontend.*

10. Qual ferramenta é comumente usada para implementar Service Discovery?
    - [ ] Microsoft Word
    - [x] Netflix Eureka / Consul
    - [ ] Adobe Photoshop
    - [ ] WhatsApp
    *Explicação: Eureka e Consul são soluções populares para gerenciar a agenda de serviços em microsserviços.*
