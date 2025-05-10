from datetime import datetime,timedelta 
from jose import JWTError, jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from backend.config import SECRET_KEY, ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES
from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.schemas import UserInDB
from backend.database.crud import UserCRUD
from backend.security.hash_password import PasswordHasher as Hasher
from backend.database.database import Usuario,get_db



oauth_scheme = OAuth2PasswordBearer(tokenUrl='token')

def cria_token_acesso(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=int(ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({'exp': expire})
    return jwt.encode(to_encode,SECRET_KEY, ALGORITHM)

def verify_token(token: str):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code= status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
            headers={'WWW-Authenticate': "Bearer"})

async def authenticate_user(email:str,password : str,db:AsyncSession)-> Usuario | None :
    user = await UserCRUD.get_user_by_email(email=email,db=db)
    if not user or not Hasher.verify_password(password,user.senha_hash):
        return None
    return user

