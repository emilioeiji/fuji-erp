# Generated by Django 4.1.7 on 2023-06-09 06:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('uniforme', '0014_alter_itemsolicitacao_solicitacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemsolicitacao',
            name='solicitacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='itens', to='uniforme.solicitacao'),
        ),
    ]
