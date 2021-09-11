# Generated by Django 3.2.7 on 2021-09-10 23:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0011_auto_20210910_1917'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
                'db_table': 'clients',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temp_name', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'db_table': 'projects',
            },
        ),
        migrations.CreateModel(
            name='ProjectClients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.client')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.project')),
            ],
            options={
                'verbose_name': 'Project Clients',
                'verbose_name_plural': 'Project Clients',
                'db_table': 'project_clients',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='clients',
            field=models.ManyToManyField(through='project.ProjectClients', to='project.Client'),
        ),
        migrations.AddField(
            model_name='client',
            name='projects',
            field=models.ManyToManyField(through='project.ProjectClients', to='project.Project'),
        ),
    ]
