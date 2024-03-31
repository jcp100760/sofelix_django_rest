from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    password = models.CharField(max_length=100, verbose_name="Password")

    def __str__(self):
        return self.name
    
class Meta:
    verbose_name = "Usuario"
    verbose_name_plural = "Usuarios"