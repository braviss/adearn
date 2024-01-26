from .models import Notification


def notification_count(request):
    if request.user.is_authenticated:
        unread_notification_count = Notification.objects.filter(user=request.user, status='un').count()
    else:
        unread_notification_count = 0

    return {'unread_notification_count': unread_notification_count}


# def notification_count(request):
#     if request.user.is_authenticated:
#         notification_count = Notification.objects.filter(user=request.user).count()
#     else:
#         notification_count = 0
#
#     return {'notification_count': notification_count}
