# Generated by Django 4.1.7 on 2023-07-25 02:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0013_remove_mensagem_data_hora_resposta'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='data_hora_resposta',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]