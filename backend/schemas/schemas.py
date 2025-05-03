from pydantic import BaseModel,Field, EmailStr

class LoginInput(BaseModel):
    login: str = EmailStr
    senha : str = Field(..., min_length=6, max_length=20)

class CadastroUserInput(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50)
    email : str = EmailStr
    senha : str = Field(..., min_length=6, max_length=20)
    confirmar_senha : str = Field(..., min_length=6, max_length=20)
    
