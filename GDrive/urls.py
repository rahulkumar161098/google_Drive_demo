from django.contrib import admin
from django.urls import path
from user import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.user_login, name="login"),
    path('register', views.RegisterView.as_view(), name="register"), 
    path('home', views.home, name="home"),
    path('log_out', views.log_out, name="log_out"),
    # path('bid_form')
]
