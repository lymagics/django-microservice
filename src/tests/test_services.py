from uuid import uuid4

from django.test import SimpleTestCase

from core.domain import model
from core.errors import PostNotFound
from core.service_layer import services
from tests.config import FakeUnitOfWork


class TestServices(SimpleTestCase):
    """
    Test case for core services.
    """
    def test_post_create(self):
        uow = FakeUnitOfWork()
        self.assertEqual(0, len(uow.posts._posts))
        post = services.post_create('text', 'author', uow)
        self.assertEqual(1, len(uow.posts._posts))
        self.assertIn(post, uow.posts._posts)
        self.assertTrue(uow.commited)

    def test_post_get(self):
        uow = FakeUnitOfWork()
        new_post = uow.posts.add(model.Post(uuid4(), 'text', 'author'))
        post = services.post_get(new_post.id, uow)
        self.assertIsNotNone(post)
        self.assertEqual(post.id, new_post.id)

    def test_post_get_fail(self):
        uow = FakeUnitOfWork()
        with self.assertRaises(PostNotFound):
            services.post_get(uuid4(), uow)
