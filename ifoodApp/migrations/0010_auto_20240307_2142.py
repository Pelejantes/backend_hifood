# Generated by Django 3.2.5 on 2024-03-08 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0009_auto_20240307_2132'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimento',
            name='codVerif',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='codVerif',
            field=models.CharField(blank=True, max_length=6, null=True),
        ),
    ]