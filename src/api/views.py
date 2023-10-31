from pathlib import Path

import yaml
from ninja import NinjaAPI

api = NinjaAPI()

oas_file = Path(__file__).parent / '../../oas.yaml'
oas_docs = yaml.safe_load(oas_file.read_text())
api.get_openapi_schema = lambda: oas_docs


@api.get('/ping')
def ping(request):
    return {'msg': 'pong'}
