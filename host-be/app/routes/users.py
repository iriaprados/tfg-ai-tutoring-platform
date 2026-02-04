from fastapi import APIRouter
from app.models.user import UserCreate, UserResponse
from app.services.user_service import create_user, get_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/", response_model=UserResponse)
def create(user: UserCreate):
    return create_user(user)


@router.get("/{user_id}", response_model=UserResponse)
def get(user_id: int):
    user = get_user(user_id)
    if not user:
        return {"error": "Usuario no encontrado"}
    return user
