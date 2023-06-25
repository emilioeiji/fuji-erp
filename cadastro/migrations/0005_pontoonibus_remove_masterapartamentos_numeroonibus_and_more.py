# Generated by Django 4.1.7 on 2023-06-24 01:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0004_alter_area_options_alter_grupofolga_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontoOnibus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroOnibus', models.IntegerField()),
                ('pontoOnibus', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['numeroOnibus'],
            },
        ),
        migrations.RemoveField(
            model_name='masterapartamentos',
            name='numeroOnibus',
        ),
        migrations.AddConstraint(
            model_name='pontoonibus',
            constraint=models.UniqueConstraint(fields=('numeroOnibus', 'pontoOnibus'), name='unique_ponto_onibus_combination'),
        ),
    ]