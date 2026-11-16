
from pydantic import BaseModel
from typing import Literal


class Order(BaseModel):
    address: str
    foods: list[str]
    drinks: list[str]


class LLMReponse(BaseModel):

    category: Literal[
        'reclamacao',
        'elogio',
        'pedido'
    ]

    summary: str
    order: Order
    is_complete: bool

    priority: Literal[
        "baixa",
        "media",
        "alta"
    ]

    answer_to_user: str

