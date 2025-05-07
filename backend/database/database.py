import asyncpg
from backend.config import DATABASE_URL, logger
from sqlalchemy import Column, String, Integer
from backend.database import Base,engine
from fastapi import Request
from sqlalchemy.ext.asyncio import AsyncSession


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer,primary_key=True)
    nome = Column(String,nullable=False)
    email = Column(String, unique=True,nullable=False)
    senha_hash = Column(String,nullable=False)


async def cria_tabelas():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def connect_to_db():
    conn = await asyncpg.connect(DATABASE_URL)
    logger.info('Conexão estabelecida com o banco de dados')
    print("Conexão estabelecida com o banco de dados!")
    return conn

async def close_db(conn):
    logger.info('Finalizando conexão com banco de dados')
    await conn.close()
    logger.info('Conexão finalizada com o banco de dados')


async def get_db(request: Request) -> AsyncSession:
    """
    Pega a mesma sessão criada no lifespan (app.state.db).
    """
    return request.app.state.db
