from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User

class UserOwnsObjectMixin(UserPassesTestMixin):
    def test_func(self):
        user = User.objects.get(pk=self.kwargs['pk'])
        return self.request.user == user
