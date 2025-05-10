import os
from dotenv import load_dotenv
import logging
from pathlib import Path
from pydantic_settings import BaseSettings

# Acessa o diretório raiz
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv()

# Declara variáveis de ambiente
DATABASE_URL = os.getenv('DB_URL',"")
if not DATABASE_URL:
    raise RuntimeError ("DATABASE_URL não está no .env")

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM')
ACCESS_TOKEN_EXPIRE_MINUTES  = os.getenv('ACCESS_TOKEN_EXPIRE_MINUTES')


# Configura o logging
LOG_DIR = BASE_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler(LOG_DIR/'app.log',encoding='UTF-8')
    ]
)

logger = logging.getLogger("backend")

class Settings(BaseSettings):
    SECRET_KEY : str
    ALGORITHM : str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES : int = 30

    class Config:
        env_file = ".env"

#settings = Settings()
