from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import login_input 
from dotenv import load_dotenv
from app.database import database

load_dotenv()


app = FastAPI(title="ToDo List")

#inclui as rotas
app.include_router(login_input.router)

# Configuração do CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # ou especifique a origem: ["http://localhost:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get('/')
def root():
    return "Nós estamos construindo essa bagaça"

@app.on_event("startup")
async def startup():
    conn = await database.connect_to_db()
    print("Conexão estabelecida com o banco de dados!")
    await conn.close()  # Fechar a conexão após o teste de conexão

@app.get("/teste")
async def teste():
    return {"message": "FastAPI está funcionando com o PostgreSQL no Render!"}