# Generated by Django 3.2.7 on 2021-09-09 18:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('added_timestamp', models.DateTimeField(auto_now_add=True)),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('alt_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Alt. Name')),
                ('esm_file_number', models.CharField(blank=True, max_length=10, null=True, verbose_name='ESM File #')),
                ('project_address1', models.CharField(max_length=100, verbose_name='Address')),
                ('project_address2', models.CharField(blank=True, max_length=100, null=True, verbose_name='')),
                ('assignment', models.CharField(choices=[('Emergency', 'Emergency'), ('Labour Dispute', 'Labour Dispute'), ('Loss Prevention', 'Loss Prevention'), ('Static', 'Static'), ('Special Project', 'Special Project')], default='Emergency', max_length=25, verbose_name='Assignment')),
                ('assignment_type', models.CharField(choices=[('Access Control', 'Access Control'), ('Evacuation Support', 'Evacuation Support'), ('Executive Protection', 'Executive Protection'), ('Fire - Fire Watch', 'Fire - Fire Watch'), ('Flood - Flood Watch', 'Flood - Flood Watch'), ('Health Screening', 'Emergency'), ('Patient - Watch', 'Patient Watch'), ('Theft Control', 'Theft Control')], default='Fire - Fire Watch', max_length=25, verbose_name='Assignment Type')),
                ('with_vehicle', models.BooleanField(default=False, verbose_name='With Vehicle?')),
                ('weekly_hours_estimate', models.PositiveSmallIntegerField(verbose_name='Weekly Hours Estimate')),
                ('project_details', models.TextField(blank=True, null=True, verbose_name='Details')),
                ('principle_first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Principle First Name')),
                ('principle_last_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Principle Last Name')),
                ('principle_address1', models.CharField(blank=True, max_length=100, null=True, verbose_name='Principle Address 1')),
                ('principle_address2', models.CharField(blank=True, max_length=100, null=True, verbose_name='Principle Address 2')),
            ],
        ),
    ]
