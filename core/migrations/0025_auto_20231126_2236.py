# Generated by Django 3.1.2 on 2023-11-27 01:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0024_auto_20231126_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='taller',
            name='inscripcion',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.inscripcion'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='inscripcion',
            name='cupos',
            field=models.IntegerField(),
        ),
        migrations.CreateModel(
            name='Perfil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('talleres_inscritos', models.ManyToManyField(related_name='usuarios_inscritos', to='core.Taller')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
