from datetime import datetime
from uuid import UUID


class Post:
    def __init__(
        self,
        id: UUID,
        text: str,
        author: str,
        created_at: datetime = None,
        updated_at: datetime = None,
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
        if self._post is not None:
            return self._post.id
        return self._id

    @property
    def created_at(self) -> datetime:
        if self._post is not None:
            return self._post.created_at
        return self._created_at

    @property
    def updated_at(self) -> datetime:
        if self._post is not None:
            return self._post.updated_at
        return self._updated_at

    def dict(self) -> dict:
        return {
            'id': self.id,
            'text': self.text,
            'author': self.author,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }
