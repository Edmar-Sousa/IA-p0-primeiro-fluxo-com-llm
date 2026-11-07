
from llms.gemini import Gemini


class LLMFactory:
    
    @staticmethod
    def create(llm: str):
        llms = {
            'gemini': Gemini
        }

        instance = llms.get(llm)

        if instance is None:
            raise ValueError('Tipo desconhecido')

        return instance()
