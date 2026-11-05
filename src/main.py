import os

from attendant import Attendant
from dotenv import load_dotenv

from utils import print_header, answer_to_client, answer_to_store


def complete_order(answer: dict, history_question: list):
    attendant = Attendant()
    order = answer.copy()

    while order['is_complete']:
        print(f'<<< {order['suggested_answer']}')
        question = input('>>> ')
        order = attendant.process_question(question, history_question)

    return order


def idle():
    attendant = Attendant()
    history_questions = []

    print_header('BEM VINDO')
    print('<<< Sou seu assistente virtual de atendimento ao cliente...\nPressione CTRL + C para sair\n')

    while True:
        print('<<< Como posso ajuda-lo?')
        question = input('>>> ')

        answer = attendant.process_question(question)
        history_questions.append(question)
        
        if answer['category'] == 'pedido' and not answer['is_complete']:
            order = complete_order(answer, history_questions)
            print(order)

        # try:

        #     # answer_to_client(answer)
        #     # answer_to_store(answer)

        # except:
        #     break



def check_exists_llm_api_key():
    if 'LLM_API_KEY' not in os.environ:
        raise Exception('LLM_API_KEY not defined in the environment')


def main() -> None:
    load_dotenv()
    check_exists_llm_api_key()
    idle()


if __name__ == '__main__':
    main()