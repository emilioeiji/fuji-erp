# Generated by Django 4.1.7 on 2023-05-23 03:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uniforme', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uniforme',
            name='tamanho',
        ),
    ]