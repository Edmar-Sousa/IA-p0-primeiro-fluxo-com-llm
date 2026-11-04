import os
import json

from google import genai
from google.genai import types
from google.genai.types import HttpOptions



class Attendant:

    def __init__(self):
        self._client = genai.Client(
            http_options=HttpOptions(api_version='v1'), 
            api_key=os.getenv('LLM_API_KEY')
        )
    

    def process_question(self, message: str):
        response = self._client.models.generate_content(
            model='gemini-3.1-flash-lite',
            contents=message,
            config=types.GenerateContentConfig(
                system_instruction="""
                    Você é um assistente de atendimento.

                    Classifique as mensagens recebidas em:
                    - reclamacao
                    - elogio
                    - pedido

                    Retorne os resultados em formato JSON.
                """,
                response_mime_type='application/json',
                response_schema={
                    'type': 'OBJECT',
                    'properties': {
                        'category': {
                            'type': 'STRING',
                            'enum': [
                                'reclamacao',
                                'elogio',
                                'pedido',
                            ]
                        },
                        'summary': {
                            'type': 'STRING'
                        },
                        'priority': {
                            'type': 'STRING',
                            'enum': ['baixa', 'media', 'alta']
                        },
                        'suggested_answer': {
                            'type': 'STRING'
                        }
                    },
                    'required': [
                        'category',
                        'summary',
                        'priority',
                        'suggested_answer'
                    ]
                }
            )
        )

        return json.loads(response.text)
