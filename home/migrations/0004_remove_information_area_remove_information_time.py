# Generated by Django 4.1.5 on 2023-01-29 12:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_information'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='information',
            name='area',
        ),
        migrations.RemoveField(
            model_name='information',
            name='time',
        ),
    ]