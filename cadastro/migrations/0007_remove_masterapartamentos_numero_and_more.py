# Generated by Django 4.1.7 on 2023-06-25 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0006_alter_masterapartamentos_pontoonibus'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='masterapartamentos',
            name='numero',
        ),
        migrations.AddField(
            model_name='masterapartamentos',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]