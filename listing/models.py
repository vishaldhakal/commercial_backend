from django.db import models
from ckeditor.fields import RichTextField
from account.models import UserProfile


class City(models.Model):
    slug = models.SlugField(max_length=1000, unique=True)
    name = models.CharField(max_length=500)
    city_details = RichTextField(blank=True)

    def __str__(self):
        return self.name


class ListingType(models.Model):
    slug = models.CharField(max_length=1000, blank=True)
    thumbnail_image = models.FileField(blank=True, null=True)
    listing_type = models.CharField(max_length=1000, unique=True)
    short_description = models.TextField(blank=True)
    details = RichTextField(blank=True)

    def __str__(self):
        return self.listing_type


class Listing(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, unique=True)
    type_of_listing = models.ForeignKey(
        ListingType, on_delete=models.CASCADE, related_name='type_of_listing')
    authour = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='authour_by')
    is_published = models.BooleanField(default=False)
    slug = models.CharField(max_length=1000, unique=True)
    price = models.FloatField()
    description = RichTextField(blank=True)
    project_address = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    square_footage = models.FloatField(default=0)
    acerage = models.FloatField(default=0)
    additional_data = models.JSONField(default=dict)

    def __str__(self):
        return self.title + " [ " + self.city.name+" ] "

    class Meta:
        ordering = ('-updated_at',)


class ListingImage(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='images')
    image = models.FileField()

    def __str__(self):
        if self.image:
            return self.image.url
