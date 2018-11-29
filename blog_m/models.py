from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Category(models.Model):
    COLOR = (
        ('dark', 'Negro'),
        ('danger', 'Rojo'),
        ('primary', 'Azul'),
        ('success', 'Verde'),
        ('warning', 'Amarillo')
    )

    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=250, verbose_name="Descipcion")
    c_tag = models.CharField(choices=COLOR, max_length=10, verbose_name="Color de la etiqueta")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima actualizacion")

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['-created']

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    tags = models.SlugField(help_text="Separa las etiquetas con ,", verbose_name="Etiquetas")
    author = models.ForeignKey(User, verbose_name="Autor", on_delete=models.PROTECT, null=True)
    content = models.TextField(verbose_name="Contenido")
    categories = models.ManyToManyField(Category, verbose_name="Categorias")
    image = models.ImageField(verbose_name="Imagen", upload_to="blogMedia")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima actualizacion")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"
        ordering = ['-created']

    def __str__(self):
        return self.title
