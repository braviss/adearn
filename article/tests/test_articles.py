from django.test import (
    Client,
    TestCase,
)
from django.urls import reverse
from article.tests.factories import ArticleFactory


class ArticleListViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.employees = ArticleFactory.create_batch(10)
        self.url = reverse('article:article_list')

    def test_access_article_list(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_article_list_content(self):
        response = self.client.get(self.url)
        self.assertTrue('articles' in response.context)
        self.assertEqual(len(response.context['articles']), 10)