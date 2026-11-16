import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

from dotenv import load_dotenv


from src.web.models.message import MessageRequest
from src.app.exception import EnvironmentVariablesError, AppException
from src.app.utils import check_env_vars_is_defined
from src.app.llmfactory import LLMFactory

load_dotenv()

web = FastAPI()
llm = LLMFactory.create(os.getenv('LLM_PROVIDER'))

chat_messages = []

orders = []
complaints = []
compliments = []



web.mount('/static', StaticFiles(directory='./src/web/public'), name='statics')


@web.get('/')
def home():
    return FileResponse('./src/web/templates/index.html')

@web.get('/client')
def client():
    return FileResponse('./src/web/templates/client.html')

@web.get('/store')
def client():
    return FileResponse('./src/web/templates/store.html')

@web.get('/chat/messages')
def messages():
    return JSONResponse(
        content={
            'chat': chat_messages,
        }
    )

@web.get('/dashboard')
def dashboard():
    orders_response = []
    complaints_response = []
    compliments_response = []

    for order in orders:
        orders_response.append(order.model_dump())

    for complaint in complaints:
        complaints_response.append(complaint.model_dump())

    for compliment in compliments:
        compliments_response.append(compliment.model_dump())


    return JSONResponse(
        content={
            'orders': orders_response,
            'complaints': complaints_response,
            'compliments': compliments_response,
        }
    )

@web.post('/process-message')
def processMessage(body: MessageRequest):

    try:
        answer = llm.process_question(body.message, chat_messages)

        print(f'[SYSTEM] Json de resposta: {answer}')

        chat_messages.append({ 
            'type': 'user', 
            'message': body.message,
        })

        if answer.category == 'pedido' and answer.is_complete:
            orders.append(answer)

        elif answer.category == 'elogio':
            compliments.append(answer)

        elif answer.category == 'reclamacao':
            complaints.append(answer)

        response = {
            'type': 'assistant',
            'message': answer.answer_to_user
        }

        chat_messages.append(response)
        return JSONResponse(content=response)

    except AppException as err:
        print(f'[SYSTEM] Error to processing: {str(err)}')

        return JSONResponse(
            status_code=err.code,
            content={
                'code_str': err.code_str,
                'message': err.message,
            }
        )

    except Exception as e:
        print(f'[SYSTEM] Error to precessing: {str(e)}')

        return JSONResponse(
            status_code=500,
            content={ 
                'code_str': 'INTERNAL_SERVER_ERROR',
                'message': 'Erro interno da aplicação! Contate um administrador e tente novamente mais tarde!'
            }
        )



@web.get('/health')
def health():
    try:
        check_env_vars_is_defined()
        return JSONResponse(
            content={
                'status': 'online',
                'details': 'Como posso ajuda-lo?'
            }
        )

    except EnvironmentVariablesError as err:
        print(f'[SYSTEM] Error health: {str(err)}')

        return JSONResponse(
            status_code=503, 
            content={
                'status': 'offline',
                'details': str(err)
            }
        )

    except Exception as err:
        print(f'[SYSTEM] Error health: {str(err)}')

        return JSONResponse(
            status_code=500,
            content={
                'status': 'offline',
                'details': 'Erro interno do sistema!'
            }
        )

    