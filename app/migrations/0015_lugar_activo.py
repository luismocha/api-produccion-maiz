# Generated by Django 3.2.8 on 2022-12-28 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_lugar'),
    ]

    operations = [
        migrations.AddField(
            model_name='lugar',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
