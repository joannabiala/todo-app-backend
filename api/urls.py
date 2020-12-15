from rest_framework import routers
from api import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename="tasks")
router.register(r'user', views.UserViewSet, basename="user")
router.register(r'list', views.ListViewSet, basename="list")
router.register(r'registration', views.RegistrationViewSet, basename='registration')

urlpatterns = [
    path('', include(router.urls)),
]
