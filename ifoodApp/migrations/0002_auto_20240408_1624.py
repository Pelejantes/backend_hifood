# Generated by Django 3.2.5 on 2024-04-08 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codverif',
            name='codigo',
            field=models.CharField(default='400374', max_length=6),
        ),
        migrations.AlterField(
            model_name='codverif',
            name='data_hora_expiracao',
            field=models.DateTimeField(null=True),
        ),
    ]
