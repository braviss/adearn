from django.contrib.messages import get_messages
from django.test import (
    Client,
    TestCase,
)
from django.urls import reverse

from article.models import Article
from article.tests.factories import ArticleFactory


class ArticleListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.employees = ArticleFactory.create_batch(10)
        self.url = reverse('article:article_list')

    def test_access_employee_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)