from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from core import views

router = routers.DefaultRouter()
# router.register(r'user', views.UserViewSet)
# router.register(r'group', views.GroupViewSet)
router.register(r'company', views.CompanyViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'card', views.PasswordCardViewSet)
router.register(r'user', views.UserRegistrationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
