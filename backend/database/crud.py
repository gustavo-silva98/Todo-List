from sqlalchemy.ext.asyncio import AsyncSession
from backend.schemas.schemas import UserCreateDTO
from backend.utils.hash_password import PasswordHasher as Hasher
from backend.database.database import Usuario
from sqlalchemy import delete

class UserCRUD():

    @staticmethod
    async def cria_usuario(db:AsyncSession, data: Usuario):
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

    @staticmethod
    async def deleta_todos_usuarios(db: AsyncSession):
        
        try:
            await db.execute(delete(Usuario))
            await db.commit()

            return {'message':'Exclusão de Usuarios feita com sucesso!'}
        except Exception as e:
            return {'Erro': f"Falha ao excluir usuarios - Erro: {e}"}