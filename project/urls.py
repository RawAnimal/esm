from django.urls import path, include
from rest_framework.routers import DefaultRouter, APIRootView
from .views import ProjectViewSet, ClientViewSet, ProjectClientsViewSet


class Root(APIRootView):
    """
    ESM API Root
    """

    pass


class ApiRootRouter(DefaultRouter):
    APIRootView = Root


# Create a router and register our viewsets with it.
router = ApiRootRouter()
router.register(r"projects", ProjectViewSet)
router.register(r"clients", ClientViewSet)
router.register(r"client_projects", ProjectClientsViewSet)


urlpatterns = [
    path("", include(router.urls)),
]
