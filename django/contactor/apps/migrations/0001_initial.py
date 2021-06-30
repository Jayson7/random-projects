# Generated by Django 3.2.4 on 2021-06-26 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('picuture', models.ImageField(upload_to='Images')),
                ('number', models.PositiveBigIntegerField()),
            ],
            options={
                'verbose_name_plural': 'Contact',
            },
        ),
    ]
