# Generated by Django 3.2.5 on 2024-03-08 00:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0006_auto_20240307_2056'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='ativo',
            new_name='statusAtivo',
        ),
    ]