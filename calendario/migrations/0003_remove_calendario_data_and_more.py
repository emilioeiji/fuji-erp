# Generated by Django 4.1.7 on 2023-06-16 02:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_master_foto_delete_perfil'),
        ('calendario', '0002_alter_calendario_posto_de_trabalho'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendario',
            name='data',
        ),
        migrations.RemoveField(
            model_name='calendario',
            name='posto_de_trabalho',
        ),
        migrations.CreateModel(
            name='DiaCalendario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('calendario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calendario.calendario')),
                ('posto_de_trabalho', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.postotrabalho')),
            ],
        ),
    ]