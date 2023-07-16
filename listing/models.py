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
    listing_type = models.CharField(max_length=1000, unique=True)

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
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    date_of_upload = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title + " [ " + self.city.name+" ] "

    class Meta:
        ordering = ('-updated_date',)


class ListingImage(models.Model):
    listing = models.ForeignKey(
        Listing, on_delete=models.CASCADE, related_name='images')
    image = models.FileField()
    image_alt = models.CharField(max_length=500, default="image alt tag")

    def __str__(self):
        if self.images:
            return self.images.url+","+self.imagealt
