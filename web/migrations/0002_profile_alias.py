# Generated by Django 5.0 on 2023-12-20 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='alias',
            field=models.CharField(default='', max_length=50),
        ),
    ]
