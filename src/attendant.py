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
                    Você é um assistente de atendimento em uma pizzaria.

                    Classifique as mensagens recebidas em:
                    - reclamacao
                    - elogio
                    - pedido

                    Alem disso, siga essas instruções:
                    - Não invente informações que não estejam na mensagem.
                    - Se uma informação não estiver disponível, utilize uma string vazia ou uma lista vazia.
                    - Considere um pedido completo somente quando todas as informações necessárias estiverem disponíveis.
                    - Não classifique uma reclamação como pedido apenas porque ela menciona um produto.

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
                        'order': {
                            'type': 'OBJECT',
                            'properties': {
                                'address': { 
                                    'type': 'STRING'
                                },
                                'drinks': { 
                                    'type': 'ARRAY',
                                    'items': { 'type': 'STRING' }
                                },
                                'foods': { 
                                    'type': 'ARRAY',
                                    'items': { 'type': 'STRING' }
                                },
                            },
                            'required': ['address', 'drinks', 'foods'],
                        },
                        'is_complete': { 
                            'type': 'BOOLEAN' 
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
                        'suggested_answer',
                        'is_complete'
                    ]
                }
            )
        )

        return json.loads(response.text)
