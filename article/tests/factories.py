import factory
from factory import fuzzy

from article.models import (
    Article,
    Category,
    Tag,
)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')

class TagFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tag

    name = factory.Sequence(lambda n: f'Tag{n}')

class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker('sentence', nb_words=4)
    body = factory.Faker('text')
    status = fuzzy.FuzzyChoice([choice[0] for choice in Article.STATUS_ARTICLE_CHOICES])
    created_at = factory.Faker('date_time_this_year', tzinfo=None, before_now=True, after_now=False)
    category = factory.SubFactory(CategoryFactory)
    tags = factory.RelatedFactoryList(TagFactory, factory_related_name='article', size=3)