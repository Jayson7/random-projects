# Generated by Django 3.1.7 on 2021-04-03 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='pdf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=200)),
                ('Author', models.CharField(max_length=200)),
                ('File', models.FileField(upload_to='media/pdf')),
                ('Date_uplaoded', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]