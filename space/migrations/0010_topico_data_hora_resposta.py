# Generated by Django 4.1.7 on 2023-07-25 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0009_mensagem_mensagem_original'),
    ]

    operations = [
        migrations.AddField(
            model_name='topico',
            name='data_hora_resposta',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
