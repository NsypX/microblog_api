# Generated by Django 3.2.7 on 2021-09-05 20:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tite',
            new_name='title',
        ),
    ]