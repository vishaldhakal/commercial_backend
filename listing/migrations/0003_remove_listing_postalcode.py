# Generated by Django 4.2 on 2023-07-15 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0002_alter_city_city_details_alter_city_slug_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='postalcode',
        ),
    ]
