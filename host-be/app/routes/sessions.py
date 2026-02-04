from fastapi import APIRouter
from app.models.session import SessionCreate, SessionResponse
from app.services.session_service import create_session

router = APIRouter(prefix="/sessions", tags=["Sessions"])


@router.post("/", response_model=SessionResponse)
def create(session: SessionCreate):
    return create_session(session.user_id)
