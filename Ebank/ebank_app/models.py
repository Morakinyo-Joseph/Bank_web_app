from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from django.conf import settings


class UserInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    account_number = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=11)
    date_created = models.DateTimeField(default=datetime.now, blank=True)
    date_created_with_time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.user.username



