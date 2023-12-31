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

    def test_post_list(self):
        uow = FakeUnitOfWork()
        post = uow.posts.add(model.Post(uuid4(), 'text', 'author'))
        posts = services.post_list(0, 1, uow)
        self.assertEqual(1, len(posts))
        self.assertIn(post, posts)

    def test_post_update(self):
        uow = FakeUnitOfWork()
        new_post = uow.posts.add(model.Post(uuid4(), 'text', 'author'))
        post = services.post_update(new_post.id, {'text': 'abc'}, uow)
        self.assertEqual(post.id, new_post.id)
        self.assertEqual(post.text, new_post.text)

    def test_post_delete(self):
        uow = FakeUnitOfWork()
        new_post = uow.posts.add(model.Post(uuid4(), 'text', 'author'))
        services.post_delete(new_post.id, uow)
        post = uow.posts.get(new_post.id)
        self.assertIsNone(post)
