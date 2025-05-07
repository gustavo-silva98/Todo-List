from backend.database.crud import UserCRUD
from backend.utils.hash_password import PasswordHasher as Hasher
from backend.schemas.schemas import CadastroUserInput,UserResponseDTO
from sqlalchemy.ext.asyncio import AsyncSession
from backend.database.database import Usuario


class UserService():

    @staticmethod
    async def cadastra_usuario(data:CadastroUserInput,db : AsyncSession) -> UserResponseDTO:
        hash = Hasher.hash_password(data.senha)
        usuario_para_criar = Usuario(
            nome=data.nome,
            email=data.email,
            senha_hash = hash
            )
        
        novo_usuario = await UserCRUD.cria_usuario(db,usuario_para_criar)

        return UserResponseDTO.from_orm(novo_usuario)

            
    @staticmethod
    async def delete_all_users(db: AsyncSession):
        try:
            await UserCRUD.deleta_todos_usuarios(db=db)
        
            return {'message':'Exclusão de Usuarios feita com sucesso!'}
        except Exception as e:
            return {'Erro': f"Falha ao excluir usuarios - Erro: {e}"}

        
