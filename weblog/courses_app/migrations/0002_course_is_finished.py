# Generated by Django 5.0.6 on 2024-06-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='is_finished',
            field=models.BooleanField(default=False),
        ),
    ]
