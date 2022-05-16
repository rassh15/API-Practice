from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
# Create your models here.
User = get_user_model()

class Todo(models.Model):
    tid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=50)
    desc = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete = models.CASCADE)

    def __str__(self) -> str:
        return f"{self.title}"