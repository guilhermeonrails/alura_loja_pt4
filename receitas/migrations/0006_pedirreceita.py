# Generated by Django 2.2.6 on 2020-01-14 13:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receitas', '0005_auto_20191203_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='PedirReceita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=200)),
                ('categoria', models.CharField(max_length=100)),
                ('date_receita', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('pedido_atendido', models.BooleanField(default=False)),
            ],
        ),
    ]
