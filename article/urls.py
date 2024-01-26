from django.urls import path, include

from article import views


urlpatterns = [
    path('', views.ArticleListView.as_view(), name='article_list'),
    path('<slug:slug>/', views.ArticleDetailView.as_view(), name='article_detail'),
    path('create', views.ArticleCreateView.as_view(), name='article_create'),

]

