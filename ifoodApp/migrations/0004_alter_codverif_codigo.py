# Generated by Django 3.2.5 on 2024-04-09 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifoodApp', '0003_alter_codverif_codigo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codverif',
            name='codigo',
            field=models.CharField(default='314143', max_length=6),
        ),
    ]
