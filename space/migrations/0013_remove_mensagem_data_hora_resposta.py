# Generated by Django 4.1.7 on 2023-07-25 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0012_remove_topico_data_hora_resposta_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mensagem',
            name='data_hora_resposta',
        ),
    ]