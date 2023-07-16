# Generated by Django 4.2 on 2023-07-15 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0004_remove_listing_status_listing_is_published'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=500, unique=True),
        ),
        migrations.AlterField(
            model_name='listingtype',
            name='listing_type',
            field=models.CharField(max_length=1000, unique=True),
        ),
    ]