from app.schemas.schemas import LoginInput
from fastapi import APIRouter

router = APIRouter()

@router.post('/submit')
async def read_submit(user: LoginInput,senha:LoginInput):
    print(f"Você recebeu: {user.login} - Senha: {senha}")
    return {"mensagem": f"Você recebeu o user {user.login}"}
