import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) 
#this is to include backend dir in sys.path so that we can import from db,main.py

from fastapi import FastAPI
from api.core.config import settings
from api.db.session import engine
from api.db.base import Base
from api.apis.base import api_router 
from fastapi.middleware.cors import CORSMiddleware

name = "Jeremiah"
age = 40


def create_tables():
    Base.metadata.create_all(bind=engine)

def include_router(app):
    app.include_router(api_router)

def start_application():
    app = FastAPI(title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION)
    create_tables()
    include_router(app)
    return app

app = start_application()

app.add_middleware(
    CORSMiddleware,
    allow_origins =['*'],
    allow_credentials = True,
    allow_methods = ['*'],
    allow_headers = ['*'],
)

@app.get('/')
def home():
    return f'Hi, {name}!'
    