# Generated by Django 4.2 on 2023-09-06 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listing', '0016_alter_listing_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='listing_pdf',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
