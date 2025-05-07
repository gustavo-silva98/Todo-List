from pydantic import BaseModel,Field, EmailStr, model_validator

# Disclaimer:
# Erros de validação de formato vem direto do Pydantic
# Validação de regras de negócio ficam no userService

class LoginInput(BaseModel):
    login: EmailStr
    senha : str = Field(..., min_length=6, max_length=20)

class CadastroUserInput(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50)
    email : EmailStr
    senha : str = Field(..., min_length=6, max_length=20)
    confirmar_senha : str = Field(..., min_length=6, max_length=20)

    @model_validator(mode='after')
    def valida_senhas(self):
        if self.senha!= self.confirmar_senha:
            raise ValueError("Senhas não coincidem")
        return self
        

class UserCreateDTO(BaseModel):
    nome: str = Field(..., min_length=3, max_length=50)
    email : EmailStr
    senha : str = Field(..., min_length=6)


class UserResponseDTO(BaseModel):
    id: int
    nome: str
    email: EmailStr
    model_config = {
        "from_attributes": True
    }




