# Generated by Django 4.2.6 on 2023-11-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_videos',
            name='id',
            field=models.IntegerField(max_length=6, primary_key=True, serialize=False),
        ),
    ]
