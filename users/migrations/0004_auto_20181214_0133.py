# Generated by Django 2.1.3 on 2018-12-13 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20181214_0021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='check',
            field=models.CharField(max_length=20),
        ),
    ]
