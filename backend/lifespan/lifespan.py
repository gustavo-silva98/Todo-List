from contextlib import asynccontextmanager
from fastapi import FastAPI
from backend.database.database import cria_tabelas,engine
from backend.config import logger
from backend.database import SessionLocal
from sqlalchemy import inspect

@asynccontextmanager
async def lifespan(app: FastAPI):
    #Inicialização da app
    logger.info("Iniciando o aplicativo")
    # Executa a conexão com o BD na inicialização
    app.state.db = SessionLocal()
    await cria_tabelas()

    # Inspeciona as tabelas existentes
    async with engine.begin() as conn:
        tables = await conn.run_sync(lambda sync_conn: inspect(sync_conn).get_columns('usuarios'))
        logger.info(f"Tabelas encontradas no banco: {tables}")

    yield
    
    # Finalização do app
    await app.state.db.close()
