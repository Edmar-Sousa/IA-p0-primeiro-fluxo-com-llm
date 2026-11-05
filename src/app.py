from attendant import Attendant
from utils import print_header


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
    

    def process_user_message(self):
        print_header('BEM VINDO')
        print('<<< Sou seu assistente virtual de atendimento ao cliente...\nPressione CTRL + C para sair\n')

        while True:
            print('<<< Como posso ajuda-lo?')
            question = input('>>> ')

            answer = self.__attendant.process_question(question)
            self.__history_questions.append(question)
            
            if answer['category'] == 'pedido' and not answer['is_complete']:
                order = self.__complete_order__(answer)
                print(order)
