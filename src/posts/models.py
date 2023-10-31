from uuid import uuid4

from django.db import models


class Post(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True)
    text = models.CharField(max_length=180)
    author = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def dict(self) -> dict:
        return {
            'id': self.id,
            'text': self.text,
            'author': self.author,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    def __str__(self) -> str:
        return self.text[:50]
