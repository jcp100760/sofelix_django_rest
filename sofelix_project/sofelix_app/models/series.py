from django.db import models

class Series(models.Model):
    name = models.CharField(max_length=100)
    chapter = models.IntegerField(10)
    season = models.IntegerField(10)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    userID = models.IntegerField(10)
    folderID = models.IntegerField(10)

    def __str__(self):
        return self.name