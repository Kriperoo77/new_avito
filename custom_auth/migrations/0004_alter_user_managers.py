# Generated by Django 3.2.16 on 2023-05-13 06:11

import custom_auth.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('custom_auth', '0003_auto_20230429_1612'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', custom_auth.models.CustomUserManager()),
            ],
        ),
    ]