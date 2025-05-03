# backend/main.py
from fastapi import FastAPI
from backend.config import logger
from backend.lifespan.lifespan import lifespan
from backend.routes.auth import router as auth_router
from backend.utils.middleware import add_cors_middleware,LoggingMiddleware

app = FastAPI(title="ToDo List",lifespan=lifespan)

# Adiciona o middleware CORS e Middleware de logging
add_cors_middleware(app)
#app.add_middleware(LoggingMiddleware)

#inclui as rotas
app.include_router(auth_router,prefix="/auth",tags=['auth'])

@app.get('/')
def root():
    return "Nós estamos construindo essa bagaça"


@app.get("/teste")
async def teste():
    return {"message": "FastAPI está funcionando com o PostgreSQL no Render!"}