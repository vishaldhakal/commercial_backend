# Generated by Django 4.2 on 2023-07-18 04:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0008_remove_listingimage_image_alt'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='longitude',
        ),
    ]