# Generated by Django 3.2.8 on 2022-12-10 23:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20221207_1841'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parroquia',
            name='fk_canton',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cantoneslist', to='app.canton'),
        ),
    ]
