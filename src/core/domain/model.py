from datetime import datetime
from uuid import UUID


class Post:
    def __init__(
        self,
        id: UUID,
        text: str,
        author: str,
        created_at: datetime,
        updated_at: datetime,
        post_=None,
    ):
        self._id = id
        self._created_at = created_at
        self._updated_at = updated_at
        self._post = post_
        self.text = text
        self.author = author

    @property
    def id(self) -> UUID:
        return self._id or self._post.id
    
    @property
    def created_at(self) -> datetime:
        return self._created_at or self._post.created_at
    
    @property
    def updated_at(self) -> datetime:
        return self._updated_at or self._post.updated_at
    
    def dict(self) -> dict:
        return {
            'id': self.id,
            'text': self.text,
            'author': self.author,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
