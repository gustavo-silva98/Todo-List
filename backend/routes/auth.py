from backend.schemas import schemas
from fastapi import APIRouter, Depends
from backend.database.database import get_db
from backend.services.user_service import UserService
from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.schemas import UserResponseDTO
from backend.database.database import Usuario,get_db
from sqlalchemy import select
from typing import List

router = APIRouter()

@router.post('/submit')
async def read_submit(user: schemas.LoginInput):
    print(f"Você recebeu: {user.login} - Senha: {user.senha}")
    return {"mensagem": f"Você recebeu o user {user.login}"}

@router.post('/cadastro')
async def cadastro_user(user: schemas.CadastroUserInput,db : AsyncSession = Depends(get_db)):

        return await UserService.cadastra_usuario(data=user,db=db)


@router.get(
    "/",
    response_model=List[UserResponseDTO],
    summary="Lista todos os usuários cadastrados"
)
async def listar_usuarios(db: AsyncSession = Depends(get_db)):
    # 1) Executa um SELECT * FROM usuarios
    result = await db.execute(select(Usuario))
    usuarios = result.scalars().all()

    # 2) Retorna a lista de modelos Pydantic
    return usuarios