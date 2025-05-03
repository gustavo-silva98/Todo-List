from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.database.database import connect_to_db,close_db
from backend.config import logger

@asynccontextmanager
async def lifespan(app: FastAPI):
    #Inicialização da app
    logger.info("Iniciando o aplicativo")
    # Executa a conexão com o BD na inicialização
    app.state.db = await connect_to_db()
    yield
    
    # Finalização do app
    await close_db(app.state.db)
