# Generated by Django 3.2.7 on 2021-09-10 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20210910_1320'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='principle_address1',
        ),
        migrations.RemoveField(
            model_name='project',
            name='principle_address2',
        ),
        migrations.RemoveField(
            model_name='project',
            name='principle_first_name',
        ),
        migrations.RemoveField(
            model_name='project',
            name='principle_last_name',
        ),
    ]
