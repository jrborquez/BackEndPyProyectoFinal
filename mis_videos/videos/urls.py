from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.users, name='users'),
    path('users/details/<user_id>', views.details, name='details'),
    path('videos/', views.videos, name='videos')
]