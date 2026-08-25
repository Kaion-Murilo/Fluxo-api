from app.models.User import User
from fastapi import APIRouter

router = APIRouter(
    prefix="/Users"
)
@router.get("/")
async def list_users():
    """
    Listar todos los usuarios
    """
    return await User.listar_usuarios()
