import os
from ollama import Client


class Devel:
    
    def __init__(self):
        self.__client = Client(
            host=os.getenv('LLM_HOST_ADDRESS')
        )


    def process_question(self, message: str, history_questions: list = []):

        response = self.__client.chat(
            model="qwen3.5:9b-q4_K_M",
            messages=[
                {
                    "role": "user",
                    "content": "Olá! Você é um atendente de pizzaria. Cumprimente o cliente."
                }
            ]
        )

        return response.message.content

