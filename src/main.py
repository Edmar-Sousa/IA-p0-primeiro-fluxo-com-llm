import os

from attendant import Attendant
from dotenv import load_dotenv


def idle():
    attendant = Attendant()

    print('~~' * 20)
    print(f'{"BEM VINDO":^40}')
    print('~~' * 20)
    print('<<< Sou seu assistente virtual de atendimento ao cliente...\nPressione CTRL + C para sair')

    while True:
        print('<<< Como posso ajuda-lo?')
        question = input('>>> ')

        answer = attendant.process_question(question)

        print('~~' * 20)
        print(f'{"RESPOSTA PARA O CLIENTE":^40}')
        print('~~' * 20)
        print(f'>>> {answer["suggested_answer"]}')
        print('~~' * 20)

        print('~~' * 20)
        print(f'{"RESPOSTA PARA A LOJA":^40}')
        print('~~' * 20)
        print(f' - tipo: {answer["category"]}')
        print(f' - resumo: {answer["summary"]}')
        print(f' - prioridade: {answer["priority"]}')
        print('~~' * 20)



def check_exists_llm_api_key():
    if 'LLM_API_KEY' not in os.environ:
        raise Exception('LLM_API_KEY not defined in the environment')


def main() -> None:
    load_dotenv()
    check_exists_llm_api_key()
    idle()


if __name__ == '__main__':
    main()