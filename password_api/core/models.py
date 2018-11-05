from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractUser

class Category(models.Model):
    name = models.CharField("Наименование", blank=False, null=False, max_length=1024)


class User(AbstractUser):
    category = models.ForeignKey("Category", blank=True, on_delete=models.CASCADE)
