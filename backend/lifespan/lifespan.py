from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.database import database

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Executa a conexão com o banco de dados na inicialização do aplicativo
    conn = await database.connect_to_db()
    print("Conexão estabelecida com o banco de dados!")
    # Yield para """aguardar""" o aplicativo rodar
    yield
    # Executa a desconexão com o banco de dados na finalização do aplicativo
    await conn.close()
    print("Conexão com o banco de dados fechada!")