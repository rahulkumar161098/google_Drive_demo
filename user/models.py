from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Folder(models.Model):
   folder_name = models.CharField(max_length=255)
   folder_author = models.ForeignKey(User, on_delete=models.CASCADE,)

   def __str__(self):
      return self.folder_name

class Files(models.Model):
   file_author= models.ForeignKey(User, on_delete=models.CASCADE)
   file= models.FileField(upload_to='files')
   parent_folder=models.CharField(max_length=10)


class AddFolder(models.Model):
   file_author= models.ForeignKey(User, on_delete=models.CASCADE)
   parent_folder= models.ManyToManyField(to=Files)
   name= models.FileField(upload_to='files')