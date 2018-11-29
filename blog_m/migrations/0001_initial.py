# Generated by Django 2.0.8 on 2018-09-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Nombre')),
                ('description', models.CharField(max_length=250, verbose_name='Descipcion')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creacion')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Titulo')),
                ('tags', models.SlugField(help_text='Separa las etiquetas con ,', verbose_name='Etiquetas')),
                ('content', models.TextField(verbose_name='Contenido')),
                ('image', models.ImageField(upload_to='blogMedia', verbose_name='Imagen')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de publicacion')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Ultima actualizacion')),
                ('categories', models.ManyToManyField(to='blog_m.Category', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
                'ordering': ['-created'],
            },
        ),
    ]