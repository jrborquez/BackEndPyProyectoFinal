from django.urls import path
from . import views

#My paths to the end-points we made in Views
urlpatterns = [
    path('', views.main, name='main'),
    path('users/', views.users, name='users'),
    path('users/details/<user_id>', views.details, name='details'),
    path('videos/', views.videos, name='videos'),
    path('videos/video_detail/<user_id>/', views.video_detail, name='video_detail'),
    path('create_user/', views.create_user, name='create_user'),
    path('edit_user/<user_id>/', views.edit_user, name='edit_user'),
    path('delete_user/<user_id>/', views.delete_user, name='delete_user'),
    path('add_video/', views.add_video, name='add_videos'),
    path('edit_video/<id>/', views.edit_video, name='edit_video'),
    path('delete_video/<id>/', views.delete_video, name='delete_video')
]