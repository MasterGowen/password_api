from django.contrib import admin

from .models import *


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'subscribe')
    search_fields = ('name', 'subscribe')


@admin.register(PasswordCard)
class PasswordCardAdmin(admin.ModelAdmin):
    list_display = ('name', 'login', 'password')
    search_fields = ('name', 'login', 'password')


@admin.register(UserRegistration)
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('user', 'company', 'category', 'password_cards')
    search_fields = ('user', 'company', 'category', 'password_cards')
