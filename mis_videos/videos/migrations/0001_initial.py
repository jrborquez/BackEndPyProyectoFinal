# Generated by Django 4.2.6 on 2023-11-02 21:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_users',
            fields=[
                ('user_id', models.CharField(max_length=5, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='tbl_videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=50)),
                ('video_name', models.CharField(max_length=50)),
                ('video_ext', models.CharField(max_length=4)),
                ('user_id', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='videos.tbl_users')),
            ],
        ),
    ]
