from backend.schemas import schemas
from fastapi import APIRouter, Depends,HTTPException,status
from backend.services.user_service import UserService
from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.schemas import UserResponseDTO, LoginInput, Token
from backend.database.database import Usuario,get_db
from sqlalchemy import select
from typing import List
from fastapi.security import OAuth2PasswordRequestForm
from backend.security.security import cria_token_acesso,authenticate_user

router = APIRouter()

@router.post('/oauth-submit',response_model=Token)
async def login_return_token(form_data : OAuth2PasswordRequestForm = Depends(),db:AsyncSession = Depends(get_db)):
    user = await authenticate_user(email=form_data.username,password=form_data.password,db=db)
    print(user)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Senha incorreta ou usuário incorreto",
            headers={'WWW.Authenticate': "Bearer"}
        )
    access_token = cria_token_acesso(data={'sub': user.email})
    return {"access_token": access_token, "token_type":"bearer"}

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
