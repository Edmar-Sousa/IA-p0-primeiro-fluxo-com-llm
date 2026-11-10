import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

from dotenv import load_dotenv

from src.app.app import App


load_dotenv()

web = FastAPI()
attendant = App(os.getenv('LLM_PROVIDER'))


web.mount('/static', StaticFiles(directory='./src/web/public'), name='statics')


@web.get('/')
def home():
    return FileResponse('./src/web/templates/index.html')


@web.get('/health')
def health():
    return {}
