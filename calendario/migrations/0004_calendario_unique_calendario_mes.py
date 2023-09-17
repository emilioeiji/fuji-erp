# Generated by Django 4.2.4 on 2023-09-17 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calendario', '0003_alter_calendario_options'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='calendario',
            constraint=models.UniqueConstraint(fields=('area', 'mes', 'ano'), name='unique_calendario_mes'),
        ),
    ]