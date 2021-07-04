# Generated by Django 3.2.4 on 2021-07-01 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='App',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=200)),
                ('link', models.URLField()),
                ('about', models.CharField(max_length=500)),
                ('picture', models.ImageField(upload_to='images')),
                ('github', models.URLField()),
            ],
            options={
                'verbose_name': 'App',
                'verbose_name_plural': 'App',
            },
        ),
    ]