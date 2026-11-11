import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

from dotenv import load_dotenv


from src.web.models.message import MessageRequest
from src.app.exception import EnvironmentVariablesError
from src.app.utils import check_env_vars_is_defined
from src.app.llmfactory import LLMFactory

load_dotenv()

web = FastAPI()
llm = LLMFactory.create(os.getenv('LLM_PROVIDER'))

chat_messages = []
user_messages = []

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
    return JSONResponse(
        content={
            'orders': orders,
            'complaints': complaints,
            'compliments': compliments,
        }
    )

@web.post('/process-message')
def processMessage(body: MessageRequest):

    try:
        answer = llm.process_question(body.message, user_messages)

        chat_messages.append({ 'type': 'user', 'content': body.message })
        user_messages.append(body.message)

        if answer['category'] == 'pedido' and answer['is_complete']:
            orders.append(answer)

        elif answer['category'] == 'elogio':
            compliments.append(answer)

        elif answer['category'] == 'reclamacao':
            complaints.append(answer)

        response = { 
            'type': 'system', 
            'content': answer['answer_to_user']
        }

        chat_messages.append(response)
        return JSONResponse(content=response)

    except Exception as e:
        return JSONResponse(
            status_code=503,
            content={ 
                'status': 'offline',
                'details': 'Perdoe-nos, mas ocorreu um erro inesperado!'
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
        return JSONResponse(
            status_code=503, 
            content={
                'status': 'offline',
                'details': str(err)
            }
        )

    except Exception:
        return JSONResponse(
            status_code=500,
            content={
                'status': 'offline',
                'details': 'Erro interno do sistema!'
            }
        )

    