from django.contrib import admin
from .models import Series
from .models import Users
from .models import Folders
from .models import Series_Folders

# Register your models here.

admin.site.register(Series)
admin.site.register(Users)
admin.site.register(Folders)
admin.site.register(Series_Folders)