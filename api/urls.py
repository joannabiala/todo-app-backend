from rest_framework import routers
from api import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename="tasks")
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]


