from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Task, List


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'completed', 'list']


class ListSerializer(serializers.ModelSerializer):
    taski = TaskSerializer(many=True, required=False)

    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = List
        fields = ['id', 'list_name', 'taski', 'owner']
        read_only_fields = ['taski']


class UserSerializer(serializers.HyperlinkedModelSerializer):
    list = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'list']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}
        owner = serializers.ReadOnlyField(source='owner.username')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
