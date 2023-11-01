from pathlib import Path
from uuid import UUID

import yaml
from ninja import NinjaAPI

from api import schemas
from core.errors import PostNotFound
from core.service_layer import services, unit_of_work

api = NinjaAPI()

oas_file = Path(__file__).parent / '../../oas.yaml'
oas_docs = yaml.safe_load(oas_file.read_text())
api.get_openapi_schema = lambda: oas_docs


@api.post('/posts', response=schemas.PostOut)
def post_create(request, data: schemas.PostIn):
    return services.post_create(
        data.text, data.author,
        unit_of_work.DjangoUnitOfWork(),
    )


@api.get('/posts', response=list[schemas.PostOut])
def post_list(request, limit: int = 10, offset: int = 0):
    return services.post_list(
        limit, offset,
        unit_of_work.DjangoUnitOfWork(),
    )


@api.get(
    '/posts/{post_id}',
    response={200: schemas.PostOut, 404: schemas.Error}
)
def post_get(request, post_id: UUID):
    try:
        return services.post_get(
            post_id, unit_of_work.DjangoUnitOfWork(),
        )
    except PostNotFound as e:
        detail = {'detail': str(e)}
        return 404, detail


@api.put(
    '/posts/{post_id}',
    response={200: schemas.PostOut, 404: schemas.Error}
)
def post_update(request, post_id: UUID, data: schemas.PostUpdate):
    try:
        return services.post_update(
            post_id, data.dict(exclude_unset=True),
            unit_of_work.DjangoUnitOfWork(),
        )
    except PostNotFound as e:
        detail = {'detail': str(e)}
        return 404, detail
