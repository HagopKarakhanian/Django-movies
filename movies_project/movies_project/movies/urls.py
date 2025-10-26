from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_movie, name='add_movie'),
    path('display/', views.display_movie, name='display_movie'),
    path('edit/', views.edit_movie, name='edit_movie'),
    path('delete/', views.delete_movie, name='delete_movie'),
]