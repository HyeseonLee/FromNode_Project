# Generated by Django 3.1.1 on 2020-10-27 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ProjectApp', '0001_initial'),
        ('NodeApp', '0003_auto_20201027_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodes',
            name='ownerPCode',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectApp.projects'),
        ),
    ]
