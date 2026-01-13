from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostCreate(BaseModel):
    content: str
    parent_id: Optional[int] = None

class PostOut(BaseModel):
    id: int
    content: str
    created_at: datetime
    author_id: int
    author_username: Optional[str] = None
    parent_id: Optional[int] = None
    like_count: int = 0
    class Config:
        orm_mode = True

class LikeOut(BaseModel):
    id: int
    user_id: int
    post_id: int
    created_at: datetime
    class Config:
        orm_mode = True
