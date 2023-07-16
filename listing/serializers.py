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
        fields = ('image', 'image_alt')


class ListingSerializer(serializers.ModelSerializer):
    city = CitySerializer()
    type_of_listing = ListingTypeSerializer()
    authour = serializers.StringRelatedField()
    images = ListingImageSerializer(many=True)

    class Meta:
        model = Listing
        fields = '__all__'
