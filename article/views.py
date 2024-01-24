from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
)
from django.db.models import Q
from django.contrib import messages

from article.forms import ArticleForm
from article.models import Article


class ArticleListView(LoginRequiredMixin, ListView):
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


class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'article_detail.html'


class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'article_form.html'
    success_url = reverse_lazy('article:article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


    # def form_valid(self, form):
    #     response = super().form_valid(form)
    #     messages.success(self.request, 'Працівника успішно створено.')
    #     return response
    #
    # def form_invalid(self, form):
    #     messages.error(self.request, 'Виникла помилка при створенні працівника.')
    #     return super().form_invalid(form)



