# Generated by Django 3.1.2 on 2023-11-24 22:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_taller'),
    ]

    operations = [
        migrations.AddField(
            model_name='taller',
            name='sala',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.sala'),
            preserve_default=False,
        ),
    ]