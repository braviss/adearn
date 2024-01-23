import calendar
from datetime import date

from django import forms
from django.forms import ChoiceField

from article.models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'body', 'category', 'image')


