import os
import requests
import json

from src.app.exception import AppLLMResponseNotJSON, AppLLMTimeOut, AppLLMServiceUnavailable
from src.app.utils import read_promp_from_txt
from .schema import ATTENDANT_SCHEMA


class Devel:
    
    def __init__(self):
        self.__url = os.getenv('DEVEL_ADDRESS')
        self.__model = os.getenv('DEVEL_MODEL')



    def __get_llm_promp__(self):
        return read_promp_from_txt()
    

    def __get_messages__(self, message: str, history: list):
        messages = [
            {
                'role': 'system',
                'content': self.__get_llm_promp__()
            }
        ]

        for msg in history:
            messages.append({
                'role': msg['type'],
                'content': msg['message']
            })
        
        messages.append({
            'role': 'user',
            'content': message,
        })

        return messages


    def __parse_response_to_json__(self, response: requests.Response):
        try:
            body = response.json()
            return json.loads(body['message']['content'])

        except requests.exceptions.JSONDecodeError as err:
            print(f'[SYSTEM] Error to parse json response {str(err)}')
            raise AppLLMResponseNotJSON('Erro interno! Nosso BOT de atendimento deu problema! Por favor tente novamente mais tarde!')


    def __ask_to_llm__(self, message: str, history_questions: list = []):
        try:
            response = requests.post(
                f'{self.__url}/api/chat',
                json={
                    'model': self.__model,
                    'messages': self.__get_messages__(message, history_questions),
                    'format': ATTENDANT_SCHEMA,
                    'stream': False,

                    'options': {
                        'temperature': 0
                    }
                },
                verify=False,
                timeout=(5, 120)
            )

            if response.status_code == 503:
                raise AppLLMServiceUnavailable('Descupe! Mas nossa LLM não esta disponivel no momento!')

            print(f'[SYSTEM] A LLM respondeu: {response.status_code}')
            return response

        except requests.exceptions.Timeout as err:
            print(f'[SYSTEM] Timeout request error: {str(err)}')
            raise AppLLMTimeOut('Nosso agente demorou muito para responder! Tente novamente!')


    def process_question(self, message: str, history_questions: list = []):
        response = self.__ask_to_llm__(message, history_questions)
        return self.__parse_response_to_json__(response)

