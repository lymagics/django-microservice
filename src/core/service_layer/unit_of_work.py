import abc

from django.db import transaction
from core.adapters import repository


class AbstractUnitOfWork(abc.ABC):
    """
    Unit Of Work pattern.
    """
    posts: repository.AbstractRepository

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    def commit(self):
        raise NotImplementedError

    def rollback(self):
        raise NotImplementedError


class DjangoUnitOfWork(AbstractUnitOfWork):
    """
    Django implementation of unit of work pattern.
    """
    def __enter__(self):
        self.posts = repository.DjangoRepository()
        transaction.set_autocommit(False)
        return super().__enter__()

    def __exit__(self, *args):
        super().__exit__()
        transaction.set_autocommit(True)

    def commit(self):
        transaction.commit()

    def rollback(self):
        transaction.rollback()
