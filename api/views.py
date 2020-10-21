from rest_framework import viewsets, permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.admin import User
from rest_framework.response import Response

from api.models import Task
from api.permissions import IsOwnerOrReadOnly
from api.serializers import TaskSerializer, UserSerializer


class TaskViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        task.title = request.data['title']
        task.completed = request.data['completed']
        task.save()
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

