# Generated by Django 4.1.2 on 2022-11-05 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myBlog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='add_post',
            new_name='Post',
        ),
    ]
