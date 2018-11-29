# Generated by Django 2.0.8 on 2018-09-26 13:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog_m', '0003_category_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='c_tag',
            field=models.IntegerField(choices=[(1, 'Rojo'), (2, 'Azul'), (3, 'Verde'), (4, 'Amarillo')], default=1, verbose_name='Color de la etiqueta'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Autor'),
        ),
    ]