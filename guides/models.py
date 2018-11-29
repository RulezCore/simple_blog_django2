from django.db import models


# Create your models here.

class Guide(models.Model):
    title = models.CharField(max_length=300, verbose_name="Titulo")
    image = models.ImageField(verbose_name="Miniatura", help_text="Se recomienda un tamaño de 500x500", upload_to="guidesImage")
    content = models.TextField(verbose_name="Contenido de la guia")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de publicacion")
    updated = models.DateTimeField(auto_now=True, verbose_name="Ultima actualizacion")

    class Meta:
        verbose_name = "Guia"
        verbose_name_plural = "Guias"

    def __str__(self):
        return self.title
