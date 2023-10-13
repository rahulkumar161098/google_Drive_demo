from django.contrib import admin
from .models import Folder, Files, AddFolder

# Register your models here.
class FolderView(admin.ModelAdmin):
   list_display=['id', 'folder_name', 'folder_author']
admin.site.register(Folder, FolderView)

class FileView(admin.ModelAdmin):
   list_display=['id', 'file_author', 'file']
admin.site.register(Files, FileView)

class AddFolderView(admin.ModelAdmin):
   list_display=['id', 'file_author', ]
admin.site.register(AddFolder, AddFolderView)

