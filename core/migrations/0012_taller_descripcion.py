# Generated by Django 3.1.2 on 2023-11-24 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_taller_sala'),
    ]

    operations = [
        migrations.AddField(
            model_name='taller',
            name='descripcion',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
