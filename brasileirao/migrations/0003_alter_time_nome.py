# Generated by Django 4.1 on 2022-08-24 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brasileirao', '0002_remove_time_participacoes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='nome',
            field=models.CharField(max_length=100),
        ),
    ]
