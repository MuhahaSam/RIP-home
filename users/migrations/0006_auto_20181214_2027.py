# Generated by Django 2.1.3 on 2018-12-14 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20181214_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='channel_name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
