from django.views.generic import (
    ListView,
    DetailView,
)
from django.db.models import Q
from article.models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'
    ordering = ['-created_at']
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.GET.get('search', '')

        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(created_at__icontains=search) |
                Q(status__icontains=search),
            )
        return queryset


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

