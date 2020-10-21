from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        owner = serializers.ReadOnlyField(source='owner.username')
        model = Task
        fields = ['id', 'title', 'completed', 'owner']



class UserSerializer(serializers.HyperlinkedModelSerializer):
    task = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'task']
        extra_kwargs = {'password': {'required': True, 'write_only': True}}
        owner = serializers.ReadOnlyField(source='owner.username')
        read_only_fields = ['task']


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


