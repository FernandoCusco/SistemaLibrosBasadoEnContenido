# Generated by Django 2.2.2 on 2019-07-01 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='autor',
            options={'ordering': ['nombre'], 'verbose_name': 'Autor', 'verbose_name_plural': 'Autores'},
        ),
        migrations.AlterField(
            model_name='autor',
            name='apellidos',
            field=models.CharField(max_length=255, verbose_name='Apellidos'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='descripcion',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Descripcion'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nacionalidad',
            field=models.CharField(max_length=50, verbose_name='Nacionalidad'),
        ),
        migrations.AlterField(
            model_name='autor',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='Nombres'),
        ),
    ]