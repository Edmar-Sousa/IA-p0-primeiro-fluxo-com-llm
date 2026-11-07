import os


def print_header(title: str):
    print('~~' * 30)
    print(f'{title:^60}')
    print('~~' * 30)
    print()


def print_order(order: dict):
    print_header('RESPOSTA PARA A LOJA')

    print(f' - Tipo: {order["category"]}')
    print(f' - Resumo: {order["summary"]}')
    print(f' - Prioridade: {order["priority"]}')
    print(f' - Endereço: {order['order']['address']}\n')
    print(' - Pedido:')

    print('--' * 30)
    for i, food in enumerate(order['order']['foods']):
        print(f'\t{i + 1}. {food}')
    print('--' * 30)

    for i, drinks in enumerate(order['order']['drinks']):
        print(f'\t{i + 1}. {drinks}')

    print('--' * 30)
    


def answer_to_client(answer: dict):
    print_header('RESPOSTA PARA O CLIENTE')
    print(f'>>> {answer["suggested_answer"]}')
    print('~~' * 30)


def answer_to_store(answer: dict):
    print_header('RESPOSTA PARA A LOJA')
    
    print(f' - tipo: {answer["category"]}')
    print(f' - resumo: {answer["summary"]}')
    print(f' - prioridade: {answer["priority"]}')
    print('~~' * 30)


def check_exists_llm_api_key():
    if 'LLM_API_KEY' not in os.environ:
        raise Exception('LLM_API_KEY not defined in the environment')