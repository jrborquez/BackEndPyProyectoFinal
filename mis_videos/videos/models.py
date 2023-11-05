from django.db import models

# Create your models here.


class tbl_users(models.Model):
    user_id = models.CharField(max_length=5, primary_key=True)
    user_name = models.CharField(max_length=50, null=False)

    def __str__(self):
        return f'{self.user_id} {self.user_name}'

class tbl_videos(models.Model):
    user_id = models.ForeignKey(tbl_users, on_delete=models.CASCADE, default=None)
    video_title = models.CharField(max_length=50)
    video_name = models.CharField(max_length=50)
    video_ext = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.user_id} {self.video_title}'
