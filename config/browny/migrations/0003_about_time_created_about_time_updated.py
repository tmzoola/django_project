# Generated by Django 5.0.1 on 2024-01-27 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browny', '0002_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='time_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='time_updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
