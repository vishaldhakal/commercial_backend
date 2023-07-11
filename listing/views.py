from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from .models import City
from .serializers import CitySerializer
from django.shortcuts import get_object_or_404


@api_view(['POST'])
def create_city(request):
    city_name = request.POST['name']
    slug = request.POST['slug']
    city_details = request.POST['city_details']
    # Create a new tag instance
    city = City(
        name=city_name,
        city_details=city_details,
        slug=slug
    )
    city.save()

    return Response({'success': "Successfully created City"})


@api_view(['GET'])
def get_city(request):
    tag = City.objects.all()
    serializers = CitySerializer(tag, many=True)
    return Response({"cities": serializers.data})


@api_view(['GET'])
def city_detail(request):
    slug = request.GET.get("slug")
    tag = City.objects.get(slug=slug)
    serializers = CitySerializer(tag)
    return Response({"city": serializers.data})


@api_view(['PUT'])
def update_city(request):
    slug = request.GET.get("slug")
    city = get_object_or_404(City, slug=slug)
    name = request.POST['name']
    city_details = request.POST['city_details']
    slug = request.POST.get('slug', city.slug)

    city.name = name
    city.slug = slug
    city.city_details = city_details

    city.save()
    return Response({'success': "Successfully updated City"})


def delete_city(request):
    # Retrieve the article to be deleted
    city_id = request.GET.get("id")
    tag = get_object_or_404(City, id=city_id)

    # Delete the article
    tag.delete()

    return Response({'success': "Sucessfully Deleted City"})
