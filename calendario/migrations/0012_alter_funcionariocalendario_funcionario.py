# Generated by Django 4.1.7 on 2023-06-28 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0008_remove_masterapartamentos_id_and_more'),
        ('calendario', '0011_funcionariocalendario_unique_calendario_funcionario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='funcionariocalendario',
            name='funcionario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.master', unique=True),
        ),
    ]