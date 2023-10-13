from django.shortcuts import redirect, render
from django.http.response import HttpResponse
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Folder, Files
# from .models import File, Folder, User

# Create your views here.

def home(request):
   if request.user.is_authenticated:
      folder= Folder.objects.filter(folder_author=request.user)
      context={
         'folder': folder
      }
      print(folder)
      return render(request, 'index.html', context)
   # return HttpResponse('hello')
   else:
      return redirect('login')



def upload_file(request, id):
   if request.method == 'POST':
      file= request.POST['file']
      try:
         create_folder= Files.objects.create(file=file, file_author=request.user, parent_folder=id )
         create_folder.save()
         return redirect('add_folder')
      except:
         messages.info(request, 'Something Went Wrong')
         return render (request, 'index.html')  


def create_folder(request):
   if request.method == 'POST':
      folder= request.POST['foldername']
      try:
         create_folder= Folder.objects.create(folder_name=folder, folder_author=request.user)
         create_folder.save()
         # home()
         return redirect('/home')
      except:
         messages.info(request, 'Something Went Wrong')
         return render (request, 'index.html')  

def add_folder(request, id):
   if request.method == 'POST':
      file= request.POST['file']
      try:
         create_folder= Files.objects.create(file=file, file_author=request.user, parent_folder=id )
         create_folder.save()
         return redirect('add_folder')
      except:
         messages.info(request, 'Something Went Wrong')
         return render (request, 'index.html') 
   return render( request, 'add_folder.html')


def user_login(request):
   if request.method== 'POST':
      u_name= request.POST['username']
      u_pass= request.POST['password']
      user= authenticate(request, username=u_name, password= u_pass)
      print(u_name, u_pass)
      if user is not None:
         login(request, user)
         return redirect('home')
      else:
         messages.error(request, 'Imvalid Email Id/Password')
         return render(request, 'login.html' )
   return render(request, 'login.html' )
   # return render(request, 'login.html')


class RegisterView(View):
   def get(self, request):
      return render(request, 'register.html')

   def post(self, request):
      fname= request.POST['fname']
      lname= request.POST['lname']
      uname= request.POST['email']
      password= request.POST['password']
      try:
         save_user= User.objects.create_user(first_name=fname, last_name=lname, username=uname, password= password)
         save_user.save()
         return redirect('login')
      except:
         return render(request, 'register.html')

   # return render(request, 'register.html')

def log_out(request):
   logout(request)
   return redirect('login')


# def all_parents(folder):
#   list = [folder]
#   parent = folder.parents
#   print(parent.count())
#   while parent.count() != 0:
#     temp = parent.all()[0]
#     list.insert(0, temp)
#     parent = temp.parents
#   return list

# class CreateFolder(View):
#   parser_classes = [FormParser, MultiPartParser]
#   authentication_classes = []