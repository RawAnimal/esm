# Generated by Django 3.2.7 on 2021-09-10 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_auto_20210909_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectClients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_date', models.DateTimeField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.client')),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='project.project')),
            ],
            options={
                'verbose_name': 'Project Client',
                'verbose_name_plural': 'Project Clients',
                'db_table': 'project_clients',
            },
        ),
        migrations.AddField(
            model_name='project',
            name='clients',
            field=models.ManyToManyField(through='project.ProjectClients', to='project.Client'),
        ),
    ]
