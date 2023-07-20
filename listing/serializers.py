from rest_framework import serializers
from .models import Listing, City, ListingType, ListingImage


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CitySerializerSmall(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('id', 'slug', 'name')


class ListingTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingType
        fields = '__all__'


class ListingImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListingImage
        fields = ('id', 'image')


class ListingSerializerSmall(serializers.ModelSerializer):
    city = CitySerializer()
    type_of_listing = ListingTypeSerializer()
    images = ListingImageSerializer(many=True)

    class Meta:
        model = Listing
        fields = ('city', 'type_of_listing', 'images', 'price',
                  'created_at', 'title', 'project_address', 'price', 'slug', 'square_footage')


class ListingSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    type_of_listing = ListingTypeSerializer()
    authour = serializers.StringRelatedField()
    images = ListingImageSerializer(many=True)

    class Meta:
        model = Listing
        fields = '__all__'
