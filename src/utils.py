def print_header(title: str):
    print('~~' * 30)
    print(f'{title:^60}')
    print('~~' * 30)
    print()


def answer_to_client(answer: dict):
    print_header('RESPOSTA PARA O CLIENTE')
    print(f'>>> {answer["suggested_answer"]}')
    print('~~' * 30)


def answer_to_store(answer: dict):
    print_header('RESPOSTA PARA A LOJA')
    
    print(f' - tipo: {answer["category"]}')
    print(f' - resumo: {answer["summary"]}')
    print(f' - prioridade: {answer["priority"]}')
    print('~~' * 20)