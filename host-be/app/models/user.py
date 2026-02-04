from pydantic import BaseModel
from typing import List, Optional

# New user 
class UserCreate(BaseModel): 
    name: str
    level: Optional[str] = None
    preferences: List[str] = []

# User response
class UserResponse(BaseModel):
    id: int
    name: str
    level: Optional[str]
    preferences: List[str]
