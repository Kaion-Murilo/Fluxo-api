from pydantic import BaseModel

class User(BaseModel):
    id:int 
    name:str
    email:str
    password_hash:str
    role:str
    created_at:str
    

class UserCriarAtualizar(BaseModel):
    nome: str
    email: str
    password_hash:str
    role:str
    updated_at:str
    
