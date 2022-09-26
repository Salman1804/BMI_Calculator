from django.urls import path,include
from singup.api import views
from rest_framework.routers import DefaultRouter
from .views import ChangePasswordView


router = DefaultRouter()
router.register('abc', views.myViewSet, basename='member')

urlpatterns = [
    path('', include(router.urls)),
    path('change-password/', ChangePasswordView.as_view(), name='change-password'),
]
