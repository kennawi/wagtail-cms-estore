# Generated by Django 3.1.7 on 2021-05-02 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='homepage',
            old_name='banner_image',
            new_name='parallax_image',
        ),
    ]
