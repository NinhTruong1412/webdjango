"""web_tuyendung URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TuyenDung.views import index, ProfileView, about,ungvien_create_view,ungvien_list_view,dynamic_lookup_view,tuyendung_create_view
from django.contrib.auth import views as auth_views
from register import views as  v
urlpatterns = [
    path('home/', index, name='index'),
    path('register/',v.register, name='register'),
    path('login/',v.login, name='login'),
	path('', index, name='index'),
    path("login/", auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),
    path('admin/', admin.site.urls),
    path('about/', about, name='about'),
    path('ungvien/create/', ungvien_create_view, name='ungvien_create'),
    path('ungvien/', ungvien_list_view, name='ungvien_list'),
    path('ungvien/<int:mauv>/', dynamic_lookup_view, name='ungvien_detail'),
    path('tuyendung/create/', tuyendung_create_view, name='tuyendung_create'),

]
