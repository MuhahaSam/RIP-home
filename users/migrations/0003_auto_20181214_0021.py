# Generated by Django 2.1.3 on 2018-12-13 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20181207_0024'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='check',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='channel_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
