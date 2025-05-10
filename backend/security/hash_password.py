from passlib.context import CryptContext

class PasswordHasher():
    contexto = CryptContext(schemes=["bcrypt"])

    @staticmethod
    def hash_password(senha):
        return PasswordHasher.contexto.hash(senha)
    
    @staticmethod
    def verify_password(senha: str,hash : str):
        return PasswordHasher.contexto.verify(secret=senha,hash=hash)