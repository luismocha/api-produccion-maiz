# Generated by Django 4.1.6 on 2023-02-08 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_galeria'),
    ]

    operations = [
        migrations.AlterField(
            model_name='galeria',
            name='imagen',
            field=models.ImageField(upload_to='imagenes/'),
        ),
    ]
