from django.contrib import admin
from .models import Folder

# Register your models here.
class FolderView(admin.ModelAdmin):
   list_display=['id', 'name']
admin.site.register(Folder, FolderView)
