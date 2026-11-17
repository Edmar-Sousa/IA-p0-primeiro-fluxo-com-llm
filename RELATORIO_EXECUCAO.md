
# Relatorio de execução


## Evolução por nível

- **Básico:** Foi construído o fluxo principal da aplicação, incluindo a integração com a LLM e a interação com o usuário por meio da linha de comando.

- **Intermediário:** Foram implementadas validações das entradas do usuário, tratamento de erros e adição de testes unitários. Também foram realizadas algumas refatorações para permitir o uso de configurações compartilhadas entre as duas LLMs.

- **Avançado:** Foi realizada a integração com a LLM da Devel, além da refatoração para permitir a utilização da Gemini ou da Devel com base nas configurações definidas no arquivo `.env`. Também foi desenvolvida uma aplicação web, complementando a aplicação de linha de comando que já existia. Posteriormente, foram realizadas melhorias no prompt e no parser, que passou a converter as respostas da LLM em uma classe de dados. Por fim, foram feitas melhorias na interface web para torná-la mais agradável.

## Principais decisões tomadas

### 1. Classificação das mensagens em pedido, reclamação ou elogio

- **Decisão tomada:** Foi instruída a LLM a considerar uma mensagem como um pedido quando ela contiver, no mínimo, um alimento (por exemplo, uma pizza) e um endereço de entrega.
- **Alternativa considerada:** Restringir a aplicação exclusivamente ao processamento de pedidos, desconsiderando mensagens de reclamação ou elogio.
- **Justificativa:** Como se trata de um primeiro protótipo, decidi confiar na capacidade de classificação da IA e utilizar as três categorias de mensagens, tornando a aplicação mais abrangente.

### 2. Armazenamento das mensagens para manter o contexto

- **Decisão tomada:** Foi utilizado um array em memória para armazenar as mensagens e manter o contexto da conversa.
- **Alternativa considerada:** Utilizar bancos de dados relacionais ou não relacionais, como PostgreSQL ou MongoDB, ou algum outro mecanismo de armazenamento persistente.
- **Justificativa:** A solução escolhida mantém a simplicidade do projeto. Como consequência, os dados são perdidos quando a aplicação é encerrada, e o armazenamento atende apenas a um único chat.

## Testes e resultados

| Teste | Entrada ou situação | Resultado esperado | Resultado obtido |
|---|---|---|---|
| Mensagens em partes | Classificação e extração do pedido com base no contexto de várias mensagens. | Identificar corretamente as informações do pedido e retornar o resultado em JSON. | Funcionou bem. O resultado foi retornado em JSON. |
| Mensagem completa | Um pedido contendo comida, bebida e endereço. | Identificar e extrair todas as informações do pedido. | Funcionou bem. A LLM conseguiu interpretar o pedido. |
| Mensagem de reclamação | Uma mensagem relatando um problema com o produto. | Classificar a mensagem como reclamação. | Funcionou bem. A LLM conseguiu classificar a mensagem corretamente. |
| Mensagem de elogio | Uma mensagem elogiando o produto. | Classificar a mensagem como elogio. | Funcionou bem. A LLM conseguiu classificar a mensagem corretamente. |

## Falhas e limitações

A LLM pode classificar uma mensagem como um pedido e, em seguida, algumas mensagens enviadas pelo usuário podem causar a duplicação desse pedido.

Esse comportamento foi identificado por meio do painel de pedidos da aplicação, no qual foi possível visualizar pedidos duplicados.

Como tentativa de correção, o prompt foi ajustado para melhorar a classificação das mensagens e a extração das informações, reduzindo a ocorrência desse problema.

## Uso de IA no desenvolvimento

### ChatGPT

Utilizado para realizar consultas, esclarecer dúvidas e auxiliar no refinamento do prompt do sistema.

## Reflexão final

O principal aprendizado foi integrar uma LLM a um sistema web para realizar a classificação de mensagens.

Para isso, foi necessário definir um prompt adequado, implementar validações, tratar possíveis erros e realizar a integração com a API.

Acredito que desenvolvi bastante minhas habilidades em desenvolvimento de software, pois esse projeto apresentou desafios diferentes dos encontrados no desenvolvimento CRUD clássico. Nesse contexto, é necessário tratar e validar as informações recebidas pela IA para garantir a consistência dos dados utilizados pela aplicação.