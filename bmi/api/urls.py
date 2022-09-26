from django.urls import path,include
from bmi.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('', views.userewSet, basename='user')

urlpatterns = [
    path('', include(router.urls)),
    
]
