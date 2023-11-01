from uuid import UUID
from core.adapters import repository
from core.domain import model
from core.service_layer import unit_of_work


class FakeRepository(repository.AbstractRepository):
    """
    Fake implementation of repository pattern.
    """
    def __init__(self, posts):
        self._posts = set(posts)

    def add(self, post: model.Post) -> model.Post:
        self._posts.add(post)
        return post

    def _get(self, post_id: UUID) -> model.Post:
        for post in self._posts:
            if post.id == post_id:
                return post
    
    def list(self, limit: int, offset: int) -> list[model.Post]:
        query_set = list(self._posts)
        return query_set[limit:limit+offset]
    
    def update(self, post_id: UUID, **payload) -> model.Post:
        post = self._get(post_id)
        for key, value in payload.items():
            setattr(post, key, value)
        return post

    def delete(self, post_id: UUID):
        post = self._get(post_id)
        if post is not None:
            self._posts.remove(post)


class FakeUnitOfWork(unit_of_work.AbstractUnitOfWork):
    """
    Fake implementation of unit of work.
    """
    def __init__(self) -> None:
        self.posts = FakeRepository([])
        self.commited = False

    def commit(self):
        self.commited = True

    def rollback(self):
        pass
