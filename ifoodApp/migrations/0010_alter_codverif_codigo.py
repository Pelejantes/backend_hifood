# Generated by Django 3.2.5 on 2024-04-09 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0009_alter_codverif_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codverif',
            name='codigo',
            field=models.CharField(max_length=6, null=True),
        ),
    ]
