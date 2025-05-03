import os
from dotenv import load_dotenv
import asyncpg

load_dotenv()
DATABASE_URL = os.getenv("DB_URL")

async def connect_to_db():
    conn = await asyncpg.connect(DATABASE_URL)
    return conn

