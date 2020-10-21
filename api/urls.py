from rest_framework import routers
from api import views
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'tasks', views.TaskViewSet, basename="tasks")
router.register(r'user', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

from rest_framework.authtoken import views

urlpatterns += [
    path('auth/', views.obtain_auth_token)
]
