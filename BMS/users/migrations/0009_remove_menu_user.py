# Generated by Django 5.0 on 2024-02-26 06:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_delete_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='user',
        ),
    ]
