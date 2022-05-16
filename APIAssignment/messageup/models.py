from pyexpat import model
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Message(models.Model):
    msg = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self):
        return self.msg