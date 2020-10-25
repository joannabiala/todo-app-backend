from rest_framework import viewsets, permissions, filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.admin import User
from rest_framework.response import Response

from api.models import Task, List
from api.permissions import IsOwnerOrReadOnly
from api.serializers import TaskSerializer, UserSerializer, ListSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    search_fields = ['title']
    filter_backends = [filters.SearchFilter]

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        task.title = request.data['title']
        task.completed = request.data['completed']
        task.save()
        serializer = TaskSerializer(task, many=False)
        return Response(serializer.data)

    # def perform_create(self, serializer):
    #     serializer.save(owner=self.request.user)
    #
    # def get_queryset(self):
    #     owner_queryset = self.queryset.filter(owner=self.request.user)
    #     return owner_queryset


class ListViewSet(viewsets.ModelViewSet):
    authentication_classes = (TokenAuthentication,)
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    queryset = List.objects.all()
    serializer_class = ListSerializer
    search_fields = ['list_name']
    filter_backends = [filters.SearchFilter]

    def update(self, request, *args, **kwargs):
        list = self.get_object()
        list.list_name = request.data['list_name']
        list.save()
        serializer = ListSerializer(list, many=False)
        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        owner_queryset = self.queryset.filter(owner=self.request.user)
        return owner_queryset


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
