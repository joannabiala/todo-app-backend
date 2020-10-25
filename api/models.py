from django.db import models
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class List(models.Model):
    list_name = models.CharField(max_length=100, null=False, blank=False)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='list')

    def __str__(self):
        return self.my_title()

    def my_title(self):
        return self.list_name


class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    completed = models.BooleanField(default=False, blank=True, null=False)
    list = models.ForeignKey(List, on_delete=models.CASCADE, related_name="taski")

    def __str__(self):
        return self.my_title()

    def my_title(self):
        return self.title


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
