from rest_framework import serializers

from .models import Client, Project, ProjectClients


class ProjectClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectClients
        fields = "__all__"


class ProjectSerializer(serializers.ModelSerializer):
    clients = serializers.StringRelatedField(many=True)
    project_city = serializers.StringRelatedField()

    class Meta:
        model = Project
        fields = ["temp_name", "clients", "project_city"]


class ClientSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    projects = serializers.StringRelatedField(many=True)

    class Meta:
        model = Client
        fields = ["full_name", "first_name", "last_name", "projects"]

    def get_full_name(self, object):
        return f"{object.first_name} {object.last_name}"
