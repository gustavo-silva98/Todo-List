import os
from dotenv import load_dotenv
import logging

load_dotenv()

# Configuração do logging
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
    handlers=[
        logging.StreamHandler(),                # saída no console
        logging.FileHandler("logs/app.log",      # grava em logs/app.log
                            encoding="utf-8")
    ]
)

logger = logging.getLogger("backend.middleware")

DATABASE_URL = os.getenv("DB_URL","")
if not DATABASE_URL:
    raise ValueError("DATABASE_URL não está definido no .env.")

