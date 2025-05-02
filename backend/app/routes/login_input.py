from app.schemas.schemas import LoginInput
from fastapi import APIRouter

router = APIRouter()

@router.post('/submit')
async def read_submit(user: LoginInput):
    print(f"Você recebeu: {user.login} - Senha: {user.senha}")
    return {"mensagem": f"Você recebeu o user {user.login}"}
