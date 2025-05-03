from fastapi import FastAPI
from .utils.middleware import add_cors_middleware
from .routes import login_input 
from .lifespan.lifespan import lifespan

from dotenv import load_dotenv
load_dotenv()

app = FastAPI(title="ToDo List",lifespan=lifespan)

#inclui as rotas
app.include_router(login_input.router)

# Adiciona o middleware CORS
add_cors_middleware(app)

@app.get('/')
def root():
    return "Nós estamos construindo essa bagaça"


@app.get("/teste")
async def teste():
    return {"message": "FastAPI está funcionando com o PostgreSQL no Render!"}