# Generated by Django 2.2.4 on 2019-09-21 17:16

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mine',
            new_name='Post',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='author_name',
        ),
    ]