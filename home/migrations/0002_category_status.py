# Generated by Django 4.1.5 on 2023-01-15 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='status',
            field=models.CharField(blank=True, choices=[('active', 'active'), ('', 'default')], max_length=500),
        ),
    ]
