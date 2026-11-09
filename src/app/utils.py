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


def check_exists_env_var(var_name: str):
    if var_name not in os.environ:
        raise Exception(f'var {var_name} not defined in the environment.')


def check_enviroment_to_gemini():
    check_exists_env_var('GEMINI_API_KEY')
    check_exists_env_var('GEMINI_MODEL')


def check_enviroment_to_devel():
    check_exists_env_var('DEVEL_ADDRESS')
    check_exists_env_var('DEVEL_MODEL')


def check_env_vars_is_defined():
    check_exists_env_var('LLM_PROVIDER')
    llm_provider = os.getenv('LLM_PROVIDER')

    if llm_provider == 'gemini':
        check_enviroment_to_gemini()

    elif llm_provider == 'devel':
        check_enviroment_to_devel()
    
    else:
        raise Exception('The LLM_PROVIDER dont\'s valid')