from rest_framework import serializers
from .models import Listing, City, ListingType, ListingImage


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class ListingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingType
        fields = '__all__'


class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ('image', 'image_alt')


class ListingSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    type_of_listing = ListingTypeSerializer()
    authour = serializers.StringRelatedField()
    images = ListingImageSerializer(many=True)

    class Meta:
        model = Listing
        fields = (
            'id',
            'city',
            'title',
            'type_of_listing',
            'authour',
            'status',
            'slug',
            'price',
            'description',
            'project_address',
            'postalcode',
            'latitute',
            'longitude',
            'date_of_upload',
            'updated_date',
            'images',
        )
