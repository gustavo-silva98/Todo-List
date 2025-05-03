import asyncpg
from backend.config import DATABASE_URL, logger

async def connect_to_db():
    conn = await asyncpg.connect(DATABASE_URL)
    logger.info('Conexão estabelecida com o banco de dados')
    print("Conexão estabelecida com o banco de dados!")
    return conn

async def close_db(conn):
    logger.info('Finalizando conexão com banco de dados')
    await conn.close()
    logger.info('Conexão finalizada com o banco de dados')
