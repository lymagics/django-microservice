from django.test import SimpleTestCase

from core.domain import model
from core.service_layer import services
from tests.config import FakeUnitOfWork


class TestServices(SimpleTestCase):
    def test_post_create(self):
        uow = FakeUnitOfWork()
        self.assertEqual(0, len(uow.posts._posts))
        post = services.post_create(
            'text', 'author', uow,
        )
        self.assertEqual(1, len(uow.posts._posts))
        self.assertIn(post, uow.posts._posts)
        self.assertTrue(uow.commited)
