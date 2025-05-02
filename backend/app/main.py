from fastapi import FastAPI
from app.routes import login_input

app = FastAPI(title="ToDo List")

#inclui as rotas
app.include_router(login_input)

@app.get('/')
def root():
    return "Nós estamos construindo essa bagaça"
