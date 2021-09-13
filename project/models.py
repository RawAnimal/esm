from django.db import models
from contact.models import City

# from django.utils import timezone


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    projects = models.ManyToManyField("Project", through="ProjectClients")

    class Meta:
        db_table = "clients"
        verbose_name = "Client"
        verbose_name_plural = "Clients"

    def __str__(self) -> str:
        return self.first_name + " " + self.last_name


class Project(models.Model):
    temp_name = models.CharField(max_length=30)
    clients = models.ManyToManyField("Client", through="ProjectClients")
    project_city = models.ForeignKey(
        City,
        on_delete=models.PROTECT,
        related_name="project_city",
        verbose_name="City",
    )

    class Meta:
        db_table = "projects"
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __str__(self) -> str:
        return self.temp_name


class ProjectClients(models.Model):
    client = models.ForeignKey(
        "Client", on_delete=models.PROTECT, related_name="project_client_list"
    )
    project = models.ForeignKey(
        "Project", on_delete=models.PROTECT, related_name="client_project_list"
    )
    effective_date = models.DateField()

    class Meta:
        db_table = "project_clients"
        verbose_name = "Project Clients"
        verbose_name_plural = "Project Clients"
