<<<<<<< HEAD
# Generated by Django 3.1.1 on 2020-09-04 11:35
=======
# Generated by Django 3.1.1 on 2020-09-05 05:53
>>>>>>> 93ec2910d097ff6e53e6d82d94a529fc169e862f

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
<<<<<<< HEAD
        ('ProjectApp', '0001_initial'),
=======
        ('ProjectApp', '__first__'),
>>>>>>> 93ec2910d097ff6e53e6d82d94a529fc169e862f
    ]

    operations = [
        migrations.CreateModel(
            name='Nodes',
            fields=[
                ('Code', models.CharField(default=0, max_length=255, primary_key=True, serialize=False, unique=True)),
                ('createdDate', models.DateTimeField(auto_now=True)),
                ('fileObj', models.FileField(upload_to='media')),
<<<<<<< HEAD
                ('ownerPCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectApp.projects')),
                ('previousCode', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NodeApp.nodes')),
=======
                ('ownerProjectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ProjectApp.projects')),
                ('previousID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='NodeApp.nodes')),
>>>>>>> 93ec2910d097ff6e53e6d82d94a529fc169e862f
                ('whoIsOwner', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
