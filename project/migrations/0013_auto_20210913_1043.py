# Generated by Django 3.2.7 on 2021-09-13 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
        ('project', '0012_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_city',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='project_city', to='contact.city', verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='projectclients',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='project_client_list', to='project.client'),
        ),
        migrations.AlterField(
            model_name='projectclients',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='client_project_list', to='project.project'),
        ),
    ]
