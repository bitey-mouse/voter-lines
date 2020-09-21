# Generated by Django 3.0.9 on 2020-09-20 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0004_auto_20200919_1912'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='polling_location',
        ),
        migrations.AddField(
            model_name='user',
            name='polling_location',
            field=models.ManyToManyField(to='rest_api.PollingLocation'),
        ),
    ]
