from django.db import models
from django.contrib.auth import get_user_model


class Category(models.Model):
    name = models.CharField("Наименование", blank=False, null=False, max_length=1024)


class Company(models.Model):
    subscribe = models.CharField("Подписка", blank=True, null=True, max_length=512)
    name = models.CharField("Наименование", blank=False, null=False, max_length=1024)


class PasswordCard(models.Model):
    name = models.CharField("Наименование", blank=True, null=True, max_length=1024)
    login = models.CharField("Логин", blank=False, null=False, max_length=1024)
    password = models.CharField("Пароль", blank=False, null=False, max_length=1024)

    class Meta:
        unique_together = ("login", "password")

    def __str__(self):
        if self.name:
            return self.name
        else:
            return self.login


class UserRegistration(models.Model):
    user = models.ForeignKey(get_user_model(), blank=False, on_delete=models.DO_NOTHING)
    company = models.ForeignKey("Company", blank=False, on_delete=models.DO_NOTHING)
    category = models.ForeignKey("Category", blank=False, on_delete=models.DO_NOTHING)
    password_cards = models.ManyToManyField("PasswordCard")
