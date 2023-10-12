from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Folder(models.Model):
   name = models.CharField(max_length=255)
   parent_folder = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE)
   author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
  
  # parents = models.OneToOneField('self', related_name="folders", on_delete=models.CASCADE)

   # def all_parents(self):
   #    return self.parents

   # def __str__(self):
   #    return self.name
   # def get_folders(self):
   #    return "\n".join([p.folders for p in self.folders.all()])