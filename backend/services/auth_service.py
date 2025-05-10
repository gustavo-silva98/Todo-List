from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException,status

from backend.security.security import authenticate_user,cria_token_acesso


class AuthService:
    
    @staticmethod
    async def authenticate_and_get_token(db: AsyncSession, email : str, password:str):
        user = await authenticate_user(email=email,password=password,db=db)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Senha incorreta ou usuário incorreto",
                headers={'WWW.Authenticate': "Bearer"}
            )
        access_token = cria_token_acesso(data={'sub': user.email})
        return {"access_token": access_token, "token_type":"bearer"}