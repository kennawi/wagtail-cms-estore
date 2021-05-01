# Generated by Django 3.1.7 on 2021-04-25 07:42

from django.db import migrations
import modelcluster.contrib.taggit


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('product', '0002_remove_productdetailpage_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdetailpage',
            name='tag',
            field=modelcluster.contrib.taggit.ClusterTaggableManager(blank=True, help_text='A comma-separated list of tags.', through='product.ProductTag', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]