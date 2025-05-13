from backend.schemas import schemas
from fastapi import APIRouter, Depends,HTTPException,status
from backend.services.user_service import UserService
from backend.services.auth_service import AuthService
from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.schemas import UserResponseDTO,Token
from backend.database.database import Usuario,get_db
from sqlalchemy import select
from typing import List
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post('/token',response_model=Token)
async def login_return_token(form_data : OAuth2PasswordRequestForm = Depends(),db:AsyncSession = Depends(get_db)):
    
    return await AuthService.authenticate_and_get_token(db=db,email=form_data.username, password=form_data.password)

@router.post('/submit')
async def read_submit(user: schemas.LoginInput):
    print(f"Você recebeu: {user.login} - Senha: {user.senha}")
    return {"mensagem": f"Você recebeu o user {user.login}"}

@router.post('/cadastro')
async def cadastro_user(user: schemas.CadastroUserInput,db : AsyncSession = Depends(get_db)):

    return await UserService.cadastra_usuario(data=user,db=db)

@router.get("/",response_model=List[UserResponseDTO],summary="Lista todos os usuários cadastrados")
async def listar_usuarios(db: AsyncSession = Depends(get_db)):
    # 1) Executa um SELECT * FROM usuarios
    result = await db.execute(select(Usuario))
    usuarios = result.scalars().all()

    # 2) Retorna a lista de modelos Pydantic
    return usuarios

@router.delete('/limpar-usuarios')
async def delete_all_rows(db: AsyncSession = Depends(get_db)):

    return await UserService.delete_all_users(db=db)

@router.post('/select-user/{email}')
async def select_user_by_email(email:str, db:AsyncSession = Depends(get_db)):
    
    result = await db.execute(select(Usuario).where(Usuario.email == email)) 
    usuarios = result.scalars().all()
    return usuarios
