# Generated by Django 3.2 on 2021-04-06 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dog',
            name='breed',
            field=models.CharField(blank=True, max_length=32),
        ),
    ]
