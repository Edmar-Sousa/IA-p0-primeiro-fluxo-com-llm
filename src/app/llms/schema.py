
ATTENDANT_SCHEMA = {
    "type": "object",
    "properties": {
        "category": {
            "type": "string",
            "enum": ["reclamacao", "elogio", "pedido"],
            "description": "Intenção principal da mensagem."
        },
        "summary": {
            "type": "string",
            "description": "Resumo objetivo da situação."
        },
        "order": {
            "type": "object",
            "properties": {
                "address": {
                    "type": "string",
                    "description": "Endereço de entrega informado."
                },
                "drinks": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Somente bebidas solicitadas."
                },
                "foods": {
                    "type": "array",
                    "items": {"type": "string"},
                    "description": "Somente alimentos solicitados."
                }
            },
            "required": ["address", "drinks", "foods"],
        },
        "is_complete": {
            "type": "boolean",
            "description": "Indica se o pedido atual possui todas as informações obrigatórias."
        },
        "priority": {
            "type": "string",
            "enum": ["baixa", "media", "alta"]
        },
        "answer_to_user": {
            "type": "string",
            "description": "Resposta natural que deve ser enviada ao cliente."
        }
    },
    "required": [
        "category",
        "summary",
        "order",
        "is_complete",
        "priority",
        "answer_to_user"
    ],
}
