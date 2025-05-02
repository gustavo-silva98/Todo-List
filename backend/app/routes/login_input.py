from app.schemas import schemas
from fastapi import APIRouter

router = APIRouter()

@router.post('/submit')
async def read_submit(user: schemas.LoginInput):
    print(f"Você recebeu: {user.login} - Senha: {user.senha}")
    return {"mensagem": f"Você recebeu o user {user.login}"}

@router.post('/cadastro')
async def cadastro_user(user: schemas.CadastroUserInput):
    print(f"Você recebeu: {user.nome} - Email {user.email} - Senha: {user.senha}")
    return {"mensagem": f"Você recebeu o user {user.nome}"}
