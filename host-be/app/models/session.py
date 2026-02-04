from pydantic import BaseModel

class SessionCreate(BaseModel):
    user_id: int

class SessionResponse(BaseModel):
    session_id: int
    user_id: int
