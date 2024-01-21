from django.views.generic import (
    ListView,
)

from article.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'

