# Generated by Django 5.0.1 on 2024-01-27 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('browny', '0003_about_time_created_about_time_updated'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('time_created', models.DateTimeField(auto_now_add=True, null=True)),
                ('time_updated', models.DateTimeField(auto_now=True, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
