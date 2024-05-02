# Generated by Django 3.2.5 on 2024-05-01 21:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0005_auto_20240430_2121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formapag',
            name='nomeFormaPag',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='itempedido',
            name='qtdItens',
            field=models.SmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='dataPedido',
            field=models.DateField(default=datetime.datetime(2024, 5, 1, 18, 31, 46, 258362)),
        ),
    ]