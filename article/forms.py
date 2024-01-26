import calendar
from datetime import date

from django import forms
from django.forms import ChoiceField
from tinymce.widgets import TinyMCE
from article.models import Article


class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = ('title', 'body', 'category', 'image')
        widgets = {'body': TinyMCE(attrs={'cols': 80, 'rows': 30})}


