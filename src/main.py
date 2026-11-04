import os

from attendant import Attendant
from dotenv import load_dotenv

from utils import print_header, answer_to_client, answer_to_store


def idle():
    attendant = Attendant()

    print_header('BEM VINDO')
    print('<<< Sou seu assistente virtual de atendimento ao cliente...\nPressione CTRL + C para sair\n')

    while True:
        print('<<< Como posso ajuda-lo?')
        question = input('>>> ')

        answer = attendant.process_question(question)
        print(answer)

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