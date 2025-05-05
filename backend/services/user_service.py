from passlib.context import CryptContext

password_context = CryptContext(schemes=["bcrypt"])

senha_teste = 'teste'

hash = password_context.hash(senha_teste)

print(password_context.verify('teste',hash))
