from google.genai.errors import APIError


from exception import AppException, AppInputError
from attendant import Attendant
from utils import print_header, print_order, answer_to_client, answer_to_store


class App:

    def __init__(self):
        self.__attendant = Attendant()
        self.__history_questions = []


    def __complete_order__(self, answer: dict):
        order = answer.copy()

        while not order['is_complete']:
            print(f'<<< {order['suggested_answer']}')

            question = input('>>> ')
            self.__history_questions.append(question)
            order = self.__attendant.process_question(question, self.__history_questions)

        return order
    

    def __ask_to_llm__(self, question: str):
        answer = self.__attendant.process_question(question)
        self.__history_questions.append(question)
        
        if answer['category'] == 'pedido':
            order = self.__complete_order__(answer)
            print_order(order)
        
        elif answer['category'] == 'elogio':
            answer_to_store(answer)
        
        else:
            answer_to_client(answer)


    def __get_user_input__(self):
        question = input('>>> ')

        if len(question) == 0:
            raise AppInputError('Envie uma mensagem valida! Tente novamente!')

        return question


    def process_user_message(self):
        print_header('BEM VINDO')
        print('<<< Sou seu assistente virtual de atendimento ao cliente...\nPressione CTRL + C para sair\n')

        while True:
            print('<<< Como posso ajuda-lo?')

            try:
                question = self.__get_user_input__()
                self.__ask_to_llm__(question)

            except KeyboardInterrupt:
                print("\nTchau! Até mais!")
                break

            except AppException as e:
                print(e)

            except APIError as e:
                print(
                    "Perdoe-nos, mas ocorreu um erro no nosso sistema! "
                    "Tente novamente em alguns instantes."
                )

            except Exception as e:
                print("Perdoe-nos, mas ocorreu um erro inesperado!")
