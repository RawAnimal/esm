from rest_framework.viewsets import ModelViewSet

from .models import Client, Project, ProjectClients
from .serializers import (
    ClientSerializer,
    ProjectSerializer,
    ProjectClientsSerializer,
)


class ClientViewSet(ModelViewSet):
    """
    Endpoint for viewing and editing clients.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectViewSet(ModelViewSet):
    """
    Endpoint for viewing and editing projects.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectClientsViewSet(ModelViewSet):
    """
    Endpoint for viewing and editing clients associated with projects.
    """

    queryset = ProjectClients.objects.all()
    serializer_class = ProjectClientsSerializer
