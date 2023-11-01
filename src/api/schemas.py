from datetime import datetime
from uuid import UUID

from ninja import Schema


class Post(Schema):
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


class Error(Schema):
    detail: str | list[str]
