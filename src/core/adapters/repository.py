import abc
from uuid import UUID

from core.domain import model
from posts import models as django_models


class AbstractRepository(abc.ABC):
    """
    Repository pattern.
    """
    def add(self, post: model.Post):
        raise NotImplementedError

    def get(self, post_id: UUID) -> model.Post:
        post = self._get(post_id)
        if post is not None:
            return model.Post(**post.dict())

    def _get(self, post_id: UUID):
        raise NotImplementedError

    def list(self, limit: int, offset: int) -> list[model.Post]:
        raise NotImplementedError

    def update(self, post_id: UUID, **payload) -> model.Post:
        raise NotImplementedError

    def delete(self, post_id: UUID):
        raise NotImplementedError


class DjangoRepository(AbstractRepository):
    """
    Django implementation of repository pattern.
    """
    def add(self, post: model.Post):
        new_post = django_models.Post(**post.dict())
        new_post.save()
        return model.Post(**new_post.dict(), post_=new_post)

    def _get(self, post_id: UUID) -> django_models.Post:
        return django_models.Post.objects.filter(id=post_id).first()

    def list(self, limit: int, offset: int) -> list[model.Post]:
        posts = django_models.Post.objects.all()[offset:limit+offset]
        return [model.Post(**post.dict()) for post in posts]

    def update(self, post_id: UUID, **payload) -> model.Post:
        post = self._get(post_id)
        for key, value in payload.items():
            setattr(post, key, value)
        post.save()
        return model.Post(**post.dict())

    def delete(self, post_id: UUID):
        post = self._get(post_id)
        post.delete()
