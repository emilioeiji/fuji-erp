# Generated by Django 4.1.7 on 2023-07-25 02:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0010_topico_data_hora_resposta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topico',
            name='data_hora_resposta',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]