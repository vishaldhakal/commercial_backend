import json
from .serializers import ListingSerializer, ListingSerializerSmall
from .models import Listing
from rest_framework.decorators import api_view, permission_classes
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import (
    api_view,
    permission_classes,
)
from rest_framework import status
from .models import City, ListingType, ListingImage
from .serializers import CitySerializer, ListingTypeSerializer, CitySerializerSmall, ListingImageSerializer
from django.shortcuts import get_object_or_404
from account.models import UserProfile
from account.serializers import UserProfileSerializer, UserProfileDetailSerializer


@api_view(['POST'])
def create_city(request):
    city_name = request.POST['name']
    slug = request.POST['slug']
    city_details = request.POST['city_details']

    # Check if a city with the provided slug already exists
    existing_city = City.objects.filter(slug=slug).first()

    if existing_city:
        return Response({'error': 'A city with this slug already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    # Create a new city instance
    city = City(
        name=city_name,
        city_details=city_details,
        slug=slug
    )
    city.save()

    return Response({'success': 'Successfully created City'})


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


@api_view(['POST'])
def update_city(request):
    idd = request.POST["id"]
    city = get_object_or_404(City, id=idd)
    name = request.POST['name']
    city_details = request.POST['city_details']
    new_slug = request.POST['slug']

    # Check if the new slug is already used by another city
    if new_slug != city.slug and City.objects.filter(slug=new_slug).exists():
        return Response({'error': 'A city with this slug already exists.'}, status=status.HTTP_400_BAD_REQUEST)

    city.name = name
    city.slug = new_slug
    city.city_details = city_details
    city.save()
    return Response({'success': "Successfully updated City"})


@api_view(['DELETE'])
def delete_city(request):
    # Retrieve the article to be deleted
    slug = request.GET.get("slug")
    city = get_object_or_404(City, slug=slug)

    # Delete the article
    city.delete()

    return Response({'success': "Sucessfully Deleted City"})


@api_view(['POST'])
def create_listingtype(request):
    listing_type = request.POST.get('listing_type')
    slug = request.POST.get('slug')
    details = request.POST.get('details')
    short_description = request.POST.get('short_description')
    thumbnail_image = request.FILES.get('thumbnail_image')

    if not listing_type:
        return Response({'error': 'Listing type is required.'}, status=status.HTTP_400_BAD_REQUEST)

    listingtype = ListingType(slug=slug,
                              listing_type=listing_type, details=details, short_description=short_description, thumbnail_image=thumbnail_image)
    listingtype.save()

    return Response({'success': "Successfully created Listing Type"})


@api_view(['GET'])
def get_listingtype(request):
    listt = ListingType.objects.all()
    serializers = ListingTypeSerializer(listt, many=True)
    return Response({"listing_types": serializers.data})


@api_view(['GET'])
def listingtype_detail(request):
    slug = request.GET.get("slug")
    listingg = get_object_or_404(ListingType, slug=slug)
    serializers = ListingTypeSerializer(listingg)
    return Response({"listing_type": serializers.data})


@api_view(['POST'])
def update_listingtype(request):
    idd = request.POST.get("id")
    slug = request.POST.get("slug")
    listingtype = get_object_or_404(ListingType, id=idd)
    listing_type = request.POST.get('listing_type')
    details = request.POST.get('details')
    short_description = request.POST.get('short_description')
    thumbnail_image = request.FILES.get('thumbnail_image')

    if not listing_type:
        return Response({'error': 'Listing type is required.'}, status=status.HTTP_400_BAD_REQUEST)

    listingtype.listing_type = listing_type
    listingtype.details = details
    listingtype.slug = slug
    listingtype.thumbnail_image = thumbnail_image
    listingtype.short_description = short_description
    listingtype.save()
    return Response({'success': "Successfully updated Listing Type"})


@api_view(['DELETE'])
def delete_listingtype(request):
    slug = request.GET.get("slug")
    listingtype = get_object_or_404(ListingType, slug=slug)

    # Delete the listing type
    listingtype.delete()

    return Response({'success': "Successfully deleted Listing Type"})


@api_view(['GET'])
def listing_list(request):
    listings = Listing.objects.all()
    serializer = ListingSerializerSmall(listings, many=True)
    return Response({"listings": serializer.data})


@api_view(['GET'])
def listing_list_city(request, city):
    cityyyy = City.objects.get(slug=city)
    listings = Listing.objects.filter(city=cityyyy)
    serializer = ListingSerializerSmall(listings, many=True)
    return Response({"listings": serializer.data})


@api_view(['GET'])
def listing_list_type(request, slug):
    type_of_listingg = ListingType.objects.get(slug=slug)
    listings = Listing.objects.filter(type_of_listing=type_of_listingg)
    serializer = ListingSerializerSmall(listings, many=True)
    return Response({"listings": serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_listing(request):
    additional_dataa = request.POST.get("additional_data")
    additional_data = json.loads(additional_dataa) if additional_dataa else {}
    city_name = request.POST.get('city_name')
    listing_type = request.POST.get('listing_type')
    title = request.POST.get('title')
    square_footage = request.POST.get('square_footage', 0)
    acerage = request.POST.get('acerage', 0)
    author_id = request.user.id
    slug = request.POST.get('slug')
    price = request.POST.get('price')
    description = request.POST.get('description')
    project_address = request.POST.get('project_address')
    is_published = request.POST.get('is_published', "False") == "True"

    latest_object = Listing.objects.latest('id')
    latest_id = latest_object.id
    slug2 = slug+latest_id

    # Retrieve the city instance
    city = get_object_or_404(City, name=city_name)

    # Retrieve the author instance
    author = get_object_or_404(UserProfile, id=author_id)

    # Retrieve the listing type instance
    type_of_listings = ListingType.objects.get(
        listing_type=listing_type)

    # Create a new listing instance
    listing = Listing(
        city=city,
        title=title,
        acerage=acerage,
        square_footage=square_footage,
        type_of_listing=type_of_listings,
        authour=author,
        slug=slug2,
        is_published=is_published,
        price=price,
        description=description,
        project_address=project_address,
        additional_data=additional_data,
    )
    listing.save()

    files = request.FILES.getlist('image')
    for file in files:
        img = ListingImage.objects.create(image=file, listing=listing)
        img.save()

    return Response({'success': "Successfully created Listing"})


@api_view(['GET'])
def listing_upload_initials(request):
    listing_types = ListingType.objects.all()
    cities = City.objects.all()
    listing_type_ser = ListingTypeSerializer(listing_types, many=True)
    cities_ser = CitySerializerSmall(cities, many=True)
    return Response({"listing_types": listing_type_ser.data, "cities": cities_ser.data})


@api_view(['GET'])
def get_listing(request):
    listings = Listing.objects.all()
    serializer = ListingSerializerSmall(listings, many=True)
    return Response({"listings": serializer.data})


@api_view(['GET'])
def listing_detail(request):
    slug = request.GET.get("slug")
    listing = get_object_or_404(Listing, slug=slug)
    serializer = ListingSerializer(listing)
    return Response({"listing": serializer.data})


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def update_listing(request):
    additional_dataa = request.POST.get("additional_data")
    additional_data = json.loads(additional_dataa) if additional_dataa else {}

    p_slug = request.POST.get("p_slug")
    slug = request.POST.get("slug")
    listing = get_object_or_404(Listing, slug=p_slug)
    title = request.POST.get('title')
    listing_type = request.POST.get('listing_type')
    square_footage = request.POST.get('square_footage', 0)
    acerage = request.POST.get('acerage', 0)
    price = request.POST.get('price')
    description = request.POST.get('description')
    project_address = request.POST.get('project_address')
    is_published = request.POST.get('is_published', "False") == "True"

    slug2 = slug+listing.id

    # Retrieve the listing type instance
    type_of_listing = ListingType.objects.get_or_create(
        listing_type=listing_type)

    listing.title = title
    listing.acerage = acerage
    listing.slug = slug2
    listing.listing_type = type_of_listing
    listing.is_published = is_published
    listing.price = price
    listing.description = description
    listing.square_footage = square_footage
    listing.project_address = project_address
    listing.additional_data = additional_data

    listing.save()
    files = request.FILES.getlist('image')
    for file in files:
        img = ListingImage.objects.create(image=file, listing=listing)
        img.save()

    return Response({'success': "Successfully updated Listing"})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def publish_listing(request):
    slug = request.GET.get("slug")
    listing = get_object_or_404(Listing, slug=slug)

    # Delete the listing
    listing.is_published = True
    listing.save()

    return Response({'success': "Successfully published Listing"})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_listing(request):
    slug = request.GET.get("slug")
    listing = get_object_or_404(Listing, slug=slug)

    # Delete the listing
    listing.delete()

    return Response({'success': "Successfully deleted Listing"})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_image(request):
    id = request.GET.get("id")
    listingimg = get_object_or_404(ListingImage, id=id)

    # Delete the listing
    listingimg.delete()

    return Response({'success': "Successfully deleted image"})
