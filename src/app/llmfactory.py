
from .llms.gemini import Gemini
from .llms.testellm import TesteLLM


class LLMFactory:
    
    @staticmethod
    def create(llm: str):
        llms = {
            'gemini': Gemini,
            'mock': TesteLLM
        }

        instance = llms.get(llm)

        if instance is None:
            raise ValueError('Tipo desconhecido')

        return instance()
