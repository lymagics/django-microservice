from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class Post(BaseModel):
    text: str
    author: str


class PostIn(Post):
    pass


class PostOut(Post):
    id: UUID
    created_at: datetime
    updated_at: datetime


class PostUpdate(Post):
    pass
