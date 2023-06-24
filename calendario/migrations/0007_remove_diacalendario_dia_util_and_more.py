# Generated by Django 4.1.7 on 2023-06-21 01:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_master_foto_delete_perfil'),
        ('calendario', '0006_remove_calendario_funcionario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diacalendario',
            name='dia_util',
        ),
        migrations.RemoveField(
            model_name='diacalendario',
            name='funcionario',
        ),
        migrations.RemoveField(
            model_name='diacalendario',
            name='posto_de_trabalho',
        ),
        migrations.CreateModel(
            name='Alocacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendario.calendario')),
                ('dia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendario.diacalendario')),
                ('funcionario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.master')),
                ('posto_trabalho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.postotrabalho')),
            ],
        ),
    ]