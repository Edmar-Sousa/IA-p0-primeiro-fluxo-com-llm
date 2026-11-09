import os
from ollama import Client


class Devel:
    
    def __init__(self):
        self.__client = Client(
            host=os.getenv('DEVEL_ADDRESS')
        )


    def process_question(self, message: str, history_questions: list = []):

        response = self.__client.chat(
            model=os.getenv('DEVEL_MODEL'),
            messages=[
                {
                    "role": "user",
                    "content": "Olá! Você é um atendente de pizzaria. Cumprimente o cliente."
                }
            ]
        )

        return response.message.content

