# Generated by Django 3.1.1 on 2020-12-26 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0004_auto_20201224_1705'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='owner',
            field=models.CharField(default='Admin', max_length=200),
        ),
    ]
