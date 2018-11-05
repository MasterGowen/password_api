from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'companies', views.CompanyViewSet)
router.register(r'categories', views.CategoryViewSet)
router.register(r'password_cards', views.PasswordCardViewSet)
router.register(r'user_registrations', views.UserRegistrationViewSet)

urlpatterns = [
    path('admin', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
