# Generated by Django 5.0.3 on 2024-04-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_presente', '0004_alter_inconsistenciaciclo_cpf'),
    ]

    operations = [
        migrations.CreateModel(
            name='CodigoMensagem',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False, unique=True)),
                ('mensagem', models.TextField()),
            ],
        ),
    ]