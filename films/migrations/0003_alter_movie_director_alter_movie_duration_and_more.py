# Generated by Django 5.0.7 on 2024-07-31 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0002_movie_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(max_length=100, verbose_name='Режиссёр'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.DurationField(verbose_name='Продолжительность'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Название'),
        ),
    ]
