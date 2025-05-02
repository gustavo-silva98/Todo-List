from pydantic import BaseModel

class LoginInput(BaseModel):
    login: str
    senha : str