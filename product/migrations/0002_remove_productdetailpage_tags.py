# Generated by Django 3.1.7 on 2021-04-25 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetailpage',
            name='tags',
        ),
    ]
