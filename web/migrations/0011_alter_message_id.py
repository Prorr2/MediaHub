# Generated by Django 5.0 on 2023-12-22 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]