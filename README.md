# Primeiro Fluxo com LLM

## Problema em Questão

Muitos empreendedores da minha cidade realizam vendas e atendimentos por meio do WhatsApp. 
Nesse contexto, são comuns os atrasos na comunicação, tanto por parte dos clientes quanto 
dos estabelecimentos.

Pensando nisso, este projeto se propõe a resolver esse problema por meio da automatização 
do atendimento com LLMs (Large Language Models), fornecendo respostas instantâneas aos 
clientes.

## Usuário / Público-alvo

O público-alvo deste projeto são pequenos empreendedores, como proprietários de pizzarias, 
lojas de cosméticos, padarias, confeitarias, entre outros estabelecimentos.

Nesta implementação específica, a LLM atuará como atendente de uma pizzaria, sendo 
responsável por coletar pedidos, endereços de entrega, reclamações e elogios.

## Por que usar LLM?

A comunicação em linguagem natural, por si só, é complexa. Existem variações linguísticas, 
abreviações, erros de digitação e diversas outras particularidades. Para proporcionar 
uma experiência de atendimento próxima a uma conversa entre duas pessoas, uma 
série de heurísticas ou fluxos predefinidos pode não ser suficiente.

Interfaces baseadas em botões e mensagens que exigem respostas em formatos específicos 
nem sempre proporcionam uma experiência agradável e fluida para os clientes.

Por exemplo, mensagens como *"Responda com o número 1 para visualizar o cardápio ou 2 para sair..."* 
exigem que o usuário siga um padrão específico e limitam a conversa a 
um fluxo predefinido.

Com o uso de LLMs, podemos tornar o atendimento mais natural e flexível, extraindo 
informações das mensagens e gerando respostas contextualizadas, sem necessariamente 
prender a conversa a um fluxo rígido.

Além disso, as LLMs permitem classificar mensagens e identificar suas intenções, 
como pedidos, reclamações e elogios. Com base nessa classificação, o sistema 
pode executar ações específicas, como coletar informações de um pedido, 
encaminhar uma reclamação para um atendente ou responder a um elogio.

## Como a solução funciona?

A LLM recebe uma mensagem e a classifica em uma das seguintes categorias:

- **Pedido:** a LLM deve extrair as informações necessárias para registrar o pedido.
- **Reclamação:** uma sugestão de resposta é gerada para o usuário, e a reclamação é encaminhada ao estabelecimento.
- **Elogio:** a LLM responde ao usuário de maneira amigável e educada.

No caso dos pedidos, a LLM deve seguir algumas regras para determinar se todas 
as informações necessárias foram coletadas:

1. O pedido só é considerado completo quando contém pelo menos um alimento ou uma bebida.
2. O pedido deve conter um endereço de entrega.

Quando a LLM consegue extrair todas essas informações, o pedido é considerado 
completo e, em seguida, encaminhado ao estabelecimento.

## Uma limitação do projeto

Atualmente, o projeto precisa enviar todo o histórico de mensagens da conversa 
para a LLM durante o processo de extração de informações.

Essa abordagem pode gerar alguns problemas à medida que as conversas se tornam mais longas:

1. **Consumo de tokens:** conversas extensas fazem com que a LLM processe uma 
quantidade maior de texto, aumentando o consumo de tokens e, consequentemente, 
o custo de utilização do modelo.

2. **Latência:** o envio de um histórico maior de mensagens também aumenta a 
quantidade de dados transmitidos pela rede, podendo elevar o tempo de 
resposta do sistema.

## Instalação

A seguir, estão os passos necessários para executar o projeto localmente.

### Configuração da LLM

Este projeto utiliza um modelo de linguagem disponibilizado pelo Google. 
Para utilizá-lo, é necessário obter uma chave de API, que pode ser 
gerada no [Google AI Studio](https://aistudio.google.com/).

Após obter a chave, configure-a no arquivo `.env`, localizado na 
raiz do projeto.

O arquivo `.env.exemplo` apresenta as variáveis de ambiente que 
precisam ser definidas:

```bash
# .env.exemplo
# Definindo o provedor, valores validos são: gemini ou devel
LLM_PROVIDER=<the-provider>

# Gemini
#
# Para utilizar a LLM do google é preciso definir a API_KEY
# e o modelo
GEMINI_API_KEY=<api-key-obtida-no-google-ia-studio>
GEMINI_MODEL=gemini-3.1-flash-lite

# Devel
#
# Para utilizar a LLM fornecida na capacitação em IA.
# Ou uma LLM baseada em Ollama
DEVEL_MODEL=qwen3.5:9b-q4_K_M 
DEVEL_ADDRESS=<host-to-llm>

```

### Configuração do ambiente

É recomendado criar um ambiente virtual para o Python. Dessa forma, 
as dependências do projeto ficam isoladas da instalação principal 
do Python e de outros projetos.

```bash
# Criando o ambiente virtual
python -m venv llm-env

# Ativando o ambiente virtual

# Linux
source ./llm-env/bin/activate

# Windows (PowerShell)
./llm-env/Scripts/Activate.ps1
```

### Instalação das dependências

Após ativar o ambiente virtual, instale as dependências 
do projeto utilizando o `pip`:

```bash
pip install -r requirements.txt
```

### Execução do projeto

Para executar o projeto, utilize o seguinte comando 
na raiz do repositório:

```bash
python src/main.py
```

