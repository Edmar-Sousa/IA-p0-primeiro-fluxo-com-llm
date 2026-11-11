ATTENDANT_SCHEMA = {
    'type': 'object',
    'properties': {
        'category': {
            'type': 'string',
            'enum': [
                'reclamacao',
                'elogio',
                'pedido',
            ]
        },
        'summary': {
            'type': 'string'
        },
        'order': {
            'type': 'object',
            'properties': {
                'address': { 
                    'type': 'string'
                },
                'drinks': { 
                    'type': 'array',
                    'items': { 
                        'type': 'string' 
                    }
                },
                'foods': { 
                    'type': 'array',
                    'items': { 
                        'type': 'string'
                    }
                },
            },
            'required': [
                'address', 
                'drinks', 
                'foods'
            ],
        },
        'is_complete': { 
            'type': 'boolean' 
        },
        'priority': {
            'type': 'string',
            'enum': [
                'baixa', 
                'media', 
                'alta'
            ]
        },
        'answer_to_user': {
            'type': 'string'
        }
    },
    'required': [
        'category',
        'summary',
        'priority',
        'answer_to_user',
        'is_complete'
    ]
}