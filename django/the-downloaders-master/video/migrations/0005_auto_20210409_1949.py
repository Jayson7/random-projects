# Generated by Django 3.1.7 on 2021-04-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0004_video_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='Image',
            field=models.FileField(upload_to='images/video'),
        ),
    ]
