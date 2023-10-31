from core.domain import model
from core.service_layer import unit_of_work


def post_create(
    text: str, auhtor: str,
    uow: unit_of_work.AbstractUnitOfWork,
) -> model.Post:
    with uow:
        post = uow.posts.add(model.Post(text, auhtor))
        uow.commit()
    return post
