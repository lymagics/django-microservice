from uuid import UUID

from core.domain import model
from core.errors import PostNotFound
from core.service_layer import unit_of_work


def post_create(
    text: str, auhtor: str,
    uow: unit_of_work.AbstractUnitOfWork,
) -> model.Post:
    with uow:
        post = uow.posts.add(model.Post(None, text, auhtor))
        uow.commit()
    return post


def post_get(
    post_id: UUID, 
    uow: unit_of_work.AbstractUnitOfWork,
) -> model.Post:
    with uow:
        post = uow.posts.get(post_id)
    if post is None:
        error = 'Post not found.'
        raise PostNotFound(error)
    return post


def post_list(
    limit: int,
    offset: int,
    uow: unit_of_work.AbstractUnitOfWork,
) -> list[model.Post]:
    with uow:
        return uow.posts.list(limit, offset)


def post_update(
    post_id: UUID,
    data: dict,
    uow: unit_of_work.AbstractUnitOfWork,
) -> model.Post:
    with uow:
        post = uow.posts.get(post_id)
        if post is None:
            error = 'Post not found.'
            raise PostNotFound(error)
        post = uow.posts.update(post_id, **data)
        uow.commit()
    return post


def post_delete(
    post_id: UUID,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        post = uow.posts.get(post_id)
        if post is None:
            error = 'Post not found.'
            raise PostNotFound(error)
        uow.posts.delete(post_id)
        uow.commit()
