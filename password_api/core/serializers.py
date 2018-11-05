from django.contrib.auth.models import Group
from rest_framework import serializers
from django.contrib.auth import get_user_model

from .models import *

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class CompanySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Company
        fields = ('name', 'subscribe')


class PasswordCardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PasswordCard
        fields = ('name', 'login', 'password')


class UserRegistrationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserRegistration
        fields = ('user', 'company', 'category', 'password_cards')
