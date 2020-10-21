from django.db import models
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class Task(models.Model):
    title = models.CharField(max_length=200, null=False, blank=False)
    completed = models.BooleanField(default=False, blank=True, null=False)
    owner = models.ForeignKey('auth.User', related_name='task', on_delete=models.CASCADE)

    def __str__(self):
        return self.my_title()

    def my_title(self):
        return self.title


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
