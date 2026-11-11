import os

from dotenv import load_dotenv
from google.genai.errors import APIError

from src.app.utils import check_env_vars_is_defined
from src.app.exception import EnvironmentVariablesError

from src.app.llmfactory import LLMFactory
from src.app.exception import AppException, AppInputError
from src.app.utils import print_header, print_order, answer_to_client, answer_to_store

load_dotenv()

llm = LLMFactory.create(os.getenv('LLM_PROVIDER'))
chat_messages = []


def get_user_input():
    try:
        question = input('>>> ').strip()

        if len(question) == 0:
            raise AppInputError('Envie uma mensagem valida! Tente novamente!')

        return question
    
    except KeyboardInterrupt:
        raise AppInputError('\nTchau! Até mais!')

def complete_order(answer: dict):
    order = answer.copy()

    while not order['is_complete']:
        print(f'<<< {order['answer_to_user']}')

        question = input('>>> ')
        chat_messages.append(question)
        order = llm.process_question(question, chat_messages)

    return order


def ask_to_llm(question: str):
    answer = llm.process_question(question)
    chat_messages.append(question)
    
    if answer['category'] == 'pedido':
        order = complete_order(answer)
        print_order(order)
    
    elif answer['category'] == 'elogio':
        answer_to_store(answer)
    
    else:
        answer_to_client(answer)


def process_user_messages():
    
    print_header('BEM VINDO')
    print('<<< Sou seu assistente virtual de atendimento ao cliente...\nPressione CTRL + C para sair\n')

    while True:
        print('<<< Como posso ajuda-lo?')

        try:
            question = get_user_input()
            ask_to_llm(question)

        except AppException as e:
            print(e)
            break

        except APIError as e:
            print(
                "Perdoe-nos, mas ocorreu um erro no nosso sistema! "
                "Tente novamente em alguns instantes."
            )
            break

        except Exception as e:
            print("Perdoe-nos, mas ocorreu um erro inesperado!")
            break


def main() -> None:

    try:
        check_env_vars_is_defined()
        process_user_messages()

    except EnvironmentVariablesError as err:
        print(f'{str(err)}: {err.var_name}')


if __name__ == '__main__':
    main()