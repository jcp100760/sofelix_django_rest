from django.db import models
from .series import Series
from .folders import Folders

class Series_Folders(models.Model):
    serieID = models.ForeignKey(Series, on_delete=models.CASCADE, verbose_name="Serie") 
    folderID = models.ForeignKey(Folders, on_delete=models.CASCADE, verbose_name="Carpeta")

    def __str__(self):
        return self.serieID.name + " - " + self.folderID.name
    
class Meta:
    verbose_name = "Serie_Carpeta"
    verbose_name_plural = "Series_Carpetas"