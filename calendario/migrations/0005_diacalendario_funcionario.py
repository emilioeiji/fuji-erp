# Generated by Django 4.1.7 on 2023-06-16 03:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_master_foto_delete_perfil'),
        ('calendario', '0004_calendario_ano_calendario_bloqueado_calendario_mes_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='diacalendario',
            name='funcionario',
            field=models.ForeignKey(default=8, on_delete=django.db.models.deletion.CASCADE, to='cadastro.master'),
            preserve_default=False,
        ),
    ]