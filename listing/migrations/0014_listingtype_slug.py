# Generated by Django 4.2 on 2023-07-21 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0013_listing_acerage'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingtype',
            name='slug',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
