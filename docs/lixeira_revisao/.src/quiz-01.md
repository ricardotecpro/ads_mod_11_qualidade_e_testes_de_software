# Quiz 01 - Introdução a Microsserviços 🌐

1. Qual a principal característica de uma arquitetura Monolítica?
    - [ ] É composta por vários serviços independentes
    - [x] O sistema é um único bloco de código onde tudo está acoplado
    - [ ] É escrita apenas em JavaScript
    - [ ] Não utiliza banco de dados
    *Explicação: No monólito, todas as funcionalidades residem em um único processo e base de código.*

2. Qual vantagem é mais associada aos Microsserviços?
    - [ ] Simplicidade de deploy inicial
    - [ ] Baixo custo de infraestrutura
    - [x] Escalabilidade granular e isolamento de falhas
    - [ ] Facilidade em depurar logs centralizados
    *Explicação: Microsserviços permitem escalar apenas a parte do sistema que precisa de mais fôlego (ex: pagamentos).*

3. O que é "Escalabilidade Horizontal"?
    - [ ] Aumentar a memória RAM de um único servidor
    - [x] Adicionar mais máquinas ou instâncias para dividir a carga
    - [ ] Trocar o banco de dados SQL por NoSQL
    - [ ] Aumentar o tamanho das tabelas
    *Explicação: É o ato de adicionar mais "trabalhadores" ao sistema ao invés de aumentar o poder de um só (vertical).*

4. Qual o papel de uma API (Application Programming Interface)?
    - [ ] Criar o design da interface do usuário
    - [x] Permitir a comunicação e troca de dados entre sistemas
    - [ ] Servir como o sistema operacional do servidor
    - [ ] Substituir o banco de dados
    *Explicação: APIs são os contratos de comunicação entre o backend e seus clientes ou outros serviços.*

5. Sobre Microsserviços, o que significa ser "Poliglota"?
    - [ ] Falar várias línguas humanas
    - [x] A liberdade de usar diferentes linguagens/tecnologias para cada serviço
    - [ ] Rodar apenas em servidores internacionais
    - [ ] Usar apenas tradução automática nas rotas
    *Explicação: Um serviço pode ser em Node.js e outro em Java, dependendo da necessidade técnica.*

6. Qual destas ferramentas é usada para testar requisições para uma API sem precisar de frontend?
    - [ ] Photoshop
    - [x] Postman / Insomnia
    - [ ] Excel
    - [ ] Docker
    *Explicação: Clients HTTP como o Postman permitem enviar verbos como GET, POST, etc., e ver a resposta direta.*

7. O que acontece se um módulo de um monólito tiver um "Memory Leak" crítico?
    - [ ] Apenas aquele módulo para de funcionar
    - [ ] O banco de dados se apaga automaticamente
    - [x] Provavelmente todo o sistema ficará instável ou sairá do ar
    - [ ] O sistema migra sozinho para microsserviços
    *Explicação: Como tudo roda no mesmo processo, falhas críticas afetam o bloco inteiro.*

8. Qual o formato de dados mais comum usado hoje para comunicação entre serviços?
    - [ ] XML
    - [x] JSON
    - [ ] CSV
    - [ ] TXT
    *Explicação: O JSON é leve, legível por humanos e o padrão de facto para APIs REST.*

9. Por que Microsserviços são considerados mais complexos operacionalmente?
    - [ ] Porque exigem mais linhas de código
    - [x] Devido à necessidade de monitorar muitos serviços, redes e consistência distribuída
    - [ ] Porque só funcionam com Linux
    - [ ] Porque requerem hardware da NASA
    *Explicação: Manter 50 serviços conversando entre si exige muito mais automação e observabilidade.*

10. Qual ferramenta ajuda a garantir que o ambiente de desenvolvimento seja idêntico ao de produção?
    - [ ] Git
    - [ ] Postman
    - [ ] VS Code
    - [x] Docker (Containerização)
    *Explicação: O Docker isola o serviço e suas dependências em um container que roda igual em qualquer lugar.*