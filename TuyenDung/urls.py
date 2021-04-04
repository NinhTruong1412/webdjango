
from django.urls import path
from TuyenDung.views import index, ProfileView, about,ungvien_create_view


urlpatterns = [
    path('ungvien/create/', ungvien_create_view, name='ungvien_create'),
]
