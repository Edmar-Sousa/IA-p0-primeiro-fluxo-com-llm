import os
import json
import time

from google import genai
from google.genai import types
from google.genai.types import HttpOptions
from google.genai.errors import APIError

from src.app.exception import AppLLMServiceUnavailable, AppErrorLLM
from src.app.models.response import LLMReponse
from src.app.utils import read_promp_from_txt
from .schema import ATTENDANT_SCHEMA


class Gemini:

    def __init__(self):
        self._client = genai.Client(
            http_options=HttpOptions(api_version='v1'), 
            api_key=os.getenv('GEMINI_API_KEY')
        )


    def __get_llm_promp__(self, history_questions: list):
        promp = read_promp_from_txt()
        history = '\nEssas são as mensagens anteriores:\n'

        for question in history_questions:
            history += f"- {question['type']}: {question['message']}\n"


        return promp + history


    def process_question(self, message: str, history_questions: list = []) -> LLMReponse:

        try:
            response = self._client.models.generate_content(
                model=os.getenv('GEMINI_MODEL'),
                contents=message,
                config=types.GenerateContentConfig(
                    system_instruction=self.__get_llm_promp__(history_questions),
                    response_mime_type='application/json',
                    response_schema=ATTENDANT_SCHEMA
                )
            )

            return LLMReponse.model_validate_json(response.text)

        except APIError as e:

            if e.code == 503:
                raise AppLLMServiceUnavailable('Descupe! Mas nossa LLM não esta disponivel no momento!')

            raise AppErrorLLM('Descupe! Ocorreu um erro no nosso agente de atendimento!')

