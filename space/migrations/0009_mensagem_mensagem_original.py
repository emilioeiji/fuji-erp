# Generated by Django 4.1.7 on 2023-07-24 04:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0008_remove_mensagem_lida'),
    ]

    operations = [
        migrations.AddField(
            model_name='mensagem',
            name='mensagem_original',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='respostas', to='space.mensagem'),
        ),
    ]