from django.contrib import admin
from django.urls import path
from user import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.user_login, name="login"),
    path('register', views.RegisterView.as_view(), name="register"), 
    path('home/', views.home, name="home"),
    path('create_folder', views.create_folder, name="create_folder"),
    path('upload_file', views.upload_file, name="upload_file"),
    path('add_folder/<id>', views.add_folder, name="add_folder"),
    path('log_out', views.log_out, name="log_out"),
    # path('bid_form')
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
