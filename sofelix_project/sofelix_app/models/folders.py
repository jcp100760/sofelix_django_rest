from django.db import models
from .users import Users

class Folders(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre de la carpeta")
    userID = models.ForeignKey(Users, on_delete=models.CASCADE, verbose_name="Usuario")

    def __str__(self):
        return self.name
    
class Meta:
    verbose_name = "Carpeta"
    verbose_name_plural = "Carpetas"