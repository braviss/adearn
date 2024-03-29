from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from article.models import Article
from accounts.models import Notification



@receiver(post_save, sender=Article)
def article_status_changed(sender, instance, update_fields=None, **kwargs):
    if update_fields and 'status' in update_fields:

        message = f'Статус статьи "{instance.title}" был изменен.'

        Notification.objects.create(
            user=instance.author,
            message=message
        )


@receiver(post_delete, sender=Article)
def article_deleted(sender, instance, **kwargs):
    Notification.objects.create(
        user=instance.author,
        message=f'Статья "{instance.title}" была успешно удалена.'
    )


# @receiver(post_save, sender=Article)
# def article_status_changed(sender, instance, **kwargs):
    # if kwargs['created']:
    #     # Объект был только что создан (добавлен)
    #     message = f'Статья "{instance.title}" была успешно добавлена.'
    # else:
    #     # Объект уже существует и был изменен


    # message = f'Статус статьи "{instance.title}" был изменен.'
    #
    # Notification.objects.create(
    #     user=instance.author,
    #     message=message
    # )