from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.schemas import UserCreateDTO
from backend.utils.hash_password import PasswordHasher as Hasher
from backend.database.database import Usuario

class UserCRUD():

    @staticmethod
    async def cria_usuario(db:AsyncSession, data: Usuario):
        print(data)
        # Insere user no BD e retorna UserResponseDTO
        novo_usuario = Usuario(
            nome = data.nome,
            email = data.email,
            senha_hash = data.senha_hash
        )

        db.add(novo_usuario)

        await db.commit()
        await db.refresh(novo_usuario)

        return novo_usuario

