from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import login_input 

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
