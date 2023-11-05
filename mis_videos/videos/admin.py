from django.contrib import admin
from .models import tbl_users, tbl_videos

# Register your models here.
class tbl_user_admin(admin.ModelAdmin):
    list_display = ('user_id', 'user_name')

class tbl_videos_admin(admin.ModelAdmin):
    list_display = ('user_id', 'video_title', 'video_ext')


admin.site.register(tbl_users, tbl_user_admin)
admin.site.register(tbl_videos, tbl_videos_admin)

