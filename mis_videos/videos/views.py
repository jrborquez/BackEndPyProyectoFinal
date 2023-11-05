from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import tbl_videos
from .models import tbl_users
from django.db import connections


# Create your views here.


def main(request):
    template = loader.get_template("main.html")
    return HttpResponse(template.render())


def users(request):
    users = tbl_users.objects.all().values()

    return render(request,'users.html', {'users': users})


def details(request, user_id):
    user = tbl_users.objects.get(user_id=user_id)
    template = loader.get_template('details.html')
    context = {
        'user': user
    }

    return HttpResponse(template.render(context, request))

def videos(request):
    videos = tbl_videos.objects.all()

    return render(request, 'videos.html',  {'videos': videos})



