from pydantic import BaseModel,Field, EmailStr, root_validator

# Disclaimer:
# Erros de validação de formato vem direto do Pydantic
# Validação de regras de negócio ficam no userService

class LoginInput(BaseModel):
    login: str = EmailStr
    senha : str = Field(..., min_length=6, max_length=20)

class CadastroUserInput(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50)
    email : str = EmailStr
    senha : str = Field(..., min_length=6, max_length=20)
    confirmar_senha : str = Field(..., min_length=6, max_length=20)

    @root_validator(pre=True)
    def valida_senhas(cls,values):
        if values.get('senha') != values.get('confirmar_senha'):
            raise ValueError("Senhas não coincidem")
        return values
        

class UserCreateDTO(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50)
    email : str = EmailStr
    senha : str = Field(..., min_length=6)


class UserResponseDTO(BaseModel):
    id: int
    nome: str
    email: EmailStr
    model_config = {
        "from_attributes": True
    }




