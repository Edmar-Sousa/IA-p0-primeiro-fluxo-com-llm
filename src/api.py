import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse

from dotenv import load_dotenv

from src.app.app import App
from src.app.exception import EnvironmentVariablesError
from src.app.utils import check_env_vars_is_defined


load_dotenv()

web = FastAPI()
attendant = App(os.getenv('LLM_PROVIDER'))


web.mount('/static', StaticFiles(directory='./src/web/public'), name='statics')


@web.get('/')
def home():
    return FileResponse('./src/web/templates/index.html')

@web.get('/client')
def client():
    return FileResponse('./src/web/templates/client.html')


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

    