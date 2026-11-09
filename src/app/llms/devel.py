import os
from ollama import Client

from app.utils import read_promp_from_txt
from .schema import ATTENDANT_SCHEMA


class Devel:
    
    def __init__(self):
        self.__client = Client(
            host=os.getenv('DEVEL_ADDRESS')
        )
    

    def __get_messages__(self, message: str, history: list):
        messages = [
            {
                'role': 'system',
                'content': read_promp_from_txt()
            }
        ]

        for message in history:
            messages.append({
                'role': 'user',
                'content': message
            })
        
        messages.append({
            'role': 'user',
            'content': message,
        })

        return messages


    def process_question(self, message: str, history_questions: list = []):
        print(self.__get_messages__(message, history_questions))
        # response = self.__client.chat(
        #     model=os.getenv('DEVEL_MODEL'),
        #     messages=self.__get_messages__(message, history_questions),
        #     options={
        #         'temperature': 0.2
        #     },
        #     format=ATTENDANT_SCHEMA
        # )

        # return response.message.content

