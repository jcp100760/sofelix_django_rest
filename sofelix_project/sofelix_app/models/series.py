from django.db import models
from .users import Users

class Series(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    chapter = models.IntegerField(max_length=10, verbose_name="Capítulo")
    season = models.IntegerField(max_length=10, verbose_name="Temporada")
    image = models.URLField(null=True, blank=True, verbose_name="Imagen")
    link = models.URLField(null=True, blank=True, verbose_name="Link")
    userID = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Usuario")

    def __str__(self):
        return self.name
    
class Meta:
    verbose_name = "Serie"
    verbose_name_plural = "Series"