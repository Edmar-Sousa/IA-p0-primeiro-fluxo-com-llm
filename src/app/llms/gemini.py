import os
import json

from google import genai
from google.genai import types
from google.genai.types import HttpOptions

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
        history = "\nEssas são as repostas anteriores do usuario:\n"

        for question in history_questions:
            history += f"- {question}\n"

        return promp + history


    def process_question(self, message: str, history_questions: list = []):

        response = self._client.models.generate_content(
            model=os.getenv('GEMINI_MODEL'),
            contents=message,
            config=types.GenerateContentConfig(
                system_instruction=self.__get_llm_promp__(history_questions),
                response_mime_type='application/json',
                response_schema=ATTENDANT_SCHEMA
            )
        )

        return json.loads(response.text)
