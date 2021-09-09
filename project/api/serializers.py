from rest_framework import serializers
from project.models import Project

class ProjectSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    active = serializers.BooleanField()

    def create(self, validated_data):
        """
        Create and return a new Project instance, given the validated data.
        """
        return Project.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and return an existing Project instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance