# Generated by Django 4.1.5 on 2023-01-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_category_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=500)),
                ('area', models.CharField(max_length=500)),
                ('phone', models.CharField(max_length=100)),
                ('time', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=500)),
            ],
        ),
    ]