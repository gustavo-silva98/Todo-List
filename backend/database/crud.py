from sqlalchemy.orm import Session
from backend.schemas.schemas import UserCreateDTO
from backend.utils.hash_password import PasswordHasher as Hasher
from backend.database.database import Usuario

class ServiceUser():

    def cria_usuario(self,db:Session, data: UserCreateDTO):
        # Insere user no BD e retorna UserResponseDTO
        novo_usuario = Usuario(
            nome = data.nome,
            email = data.email,
            senha = data
        )


    