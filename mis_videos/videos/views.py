from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import tbl_videos
from .models import tbl_users
from .forms import UserForm, VideoForm
from django.db import connections


# Create your views here.

#Main index page.
def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())

#Shows a list of all users
def users(request):
    users = tbl_users.objects.all().values()

    return render(request,'users.html', {'users': users})


#Show details of each user in details.html
def details(request, user_id):
    user = tbl_users.objects.get(user_id=user_id)

    return render(request, 'details.html', {'user': user})


#Deliver what´s in Database for videos.html template
def videos(request):
    videos = tbl_videos.objects.all()

    return render(request, 'videos.html',  {'videos': videos})


#Renders create_user.html for creating a User
def create_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})

#Update the chosen (id) instance
def edit_user(request, user_id):
    edit_u = tbl_users.objects.get(user_id=user_id)
    form_eu = UserForm(instance=edit_u)

    if request.method == 'POST':
        edit_u = tbl_users.objects.get(user_id=user_id)
        form_eu = UserForm(request.POST, instance=edit_u)
        if form_eu.is_valid():
            form_eu.save()
            return redirect('users')

    return render(request, 'edit_user.html', {'form_eu': form_eu})


#Delete User from row wich id belongs to each Employee
def delete_user(request, user_id):
    user_del = tbl_users.objects.get(user_id=user_id)

    if request.method == 'POST':
        user_del.delete()
        return redirect('users')

    return render(request, 'delete_user.html', {'user_del': user_del})


#Add a Video from the method Post
def add_video(request):
    if request.method == 'POST':
        form_v = VideoForm(request.POST)
        if form_v.is_valid():
            form_v.save()
            return redirect('videos')
    else:
        form_v = VideoForm()
    return render(request, 'add_video.html', {'form_v': form_v})


def edit_video(request, id):

    edit_v = tbl_videos.objects.get(id=id)
    form_ve = VideoForm(instance=edit_v)

    if request.method == 'POST':
        form_ve = VideoForm(request.POST, instance=edit_v)
        if form_ve.is_valid():
            form_ve.save()
            return redirect('videos')


    return render(request, 'edit_video.html', {'form_ve': form_ve})


#Delete a video from the list of videos
def delete_video(request, id):
    video_del = tbl_videos.objects.get(id=id)

    if request.method == 'POST':
        video_del.delete()
        return redirect('videos')


    return render(request, 'delete_video.html', {'video_del': video_del})


#Shows the Videos from a specific Employee with payroll #
def video_detail(request, user_id):

    video_detail = tbl_videos.objects.filter(user_id=user_id)

    return render(request, 'video_detail.html', {'video_detail': video_detail})
