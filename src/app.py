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


    def process_user_message(self):
        print_header('BEM VINDO')
        print('<<< Sou seu assistente virtual de atendimento ao cliente...\nPressione CTRL + C para sair\n')

        while True:
            print('<<< Como posso ajuda-lo?')
            question = input('>>> ')
            self.__ask_to_llm__(question)
