# Generated by Django 3.1.2 on 2023-11-27 01:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0022_auto_20231126_2233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inscripcion',
            name='taller',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.taller'),
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
