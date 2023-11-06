from django import forms
from .models import tbl_users, tbl_videos

class UserForm(forms.ModelForm):
    class Meta:
        model = tbl_users
        fields = ["user_id", "user_name"]


class VideoForm(forms.ModelForm):
    class Meta:
        model = tbl_videos
        fields = ["user_id", "video_title", "video_name", "video_ext"]