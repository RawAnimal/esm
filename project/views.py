from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets

from .models import Client, Project, ProjectClients
from .serializers import (
    ClientSerializer,
    ProjectSerializer,
    ProjectClientsSerializer,
)


class ClientViewSet(viewsets.ModelViewSet):
    """
    Endpoint for viewing and editing clients.
    """

    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    """
    Endpoint for viewing and editing projects.
    """

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectClientsViewSet(viewsets.ModelViewSet):
    """
    Endpoint for viewing and editing clients associated with projects.
    """

    queryset = ProjectClients.objects.all()
    serializer_class = ProjectClientsSerializer
