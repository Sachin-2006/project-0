# Generated by Django 4.2 on 2023-04-18 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='profile_pics/default_profile_pic.jpg', null=True, upload_to=''),
        ),
    ]
