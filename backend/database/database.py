import asyncpg
from backend.config import DATABASE_URL

async def connect_to_db():
    conn = await asyncpg.connect(DATABASE_URL)
    return conn

