# Generated by Django 3.2.8 on 2022-12-28 06:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_alter_intermediario_fk_lugar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Intermediario_Produccion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fk_intermediario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='app.intermediario')),
                ('fk_produccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='app.produccion')),
            ],
        ),
        migrations.AddField(
            model_name='intermediario',
            name='produccion',
            field=models.ManyToManyField(blank=True, through='app.Intermediario_Produccion', to='app.Produccion'),
        ),
    ]