# Generated by Django 3.2.7 on 2021-09-10 23:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0010_alter_project_clients'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='clients',
        ),
        migrations.RemoveField(
            model_name='projectclients',
            name='client',
        ),
        migrations.RemoveField(
            model_name='projectclients',
            name='project',
        ),
        migrations.DeleteModel(
            name='Client',
        ),
        migrations.DeleteModel(
            name='Project',
        ),
        migrations.DeleteModel(
            name='ProjectClients',
        ),
    ]
