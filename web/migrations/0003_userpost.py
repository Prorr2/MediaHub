# Generated by Django 5.0 on 2023-12-20 21:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_profile_alias'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('media', models.FileField(upload_to='posts')),
                ('description', models.CharField(max_length=1000)),
                ('profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.profile')),
            ],
        ),
    ]