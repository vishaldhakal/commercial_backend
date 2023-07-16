from django.urls import path
from . import views

urlpatterns = [
    path('create-city/', views.create_city, name='create_citys'),
    path('update-city/', views.update_city, name='update_citys'),
    path('cities/', views.get_city, name='get_city'),
    path('city-detail/', views.city_detail, name='city_detail'),
    path('delete-city/', views.delete_city, name='delete_citys'),
    path('create-listingtype/', views.create_listingtype,
         name='create_listingtypes'),
    path('update-listingtype/', views.update_listingtype,
         name='update_listingtypes'),
    path('listingtypes/', views.get_listingtype, name='get_listingtype'),
    path('listingtype-detail/', views.listingtype_detail,
         name='listingtype_detail'),

    path('delete-listingtype/', views.delete_listingtype,
         name='delete_listingtypes'),
    path('listing-upload-initials/', views.listing_upload_initials,
         name='listing_upload_initials'),
    path('listings/', views.listing_list, name='listing-list'),
    path('create-listing/', views.create_listing, name='create-listing'),
    path('listing-detail/', views.listing_detail, name='listing-detail'),
    path('update-listing/', views.update_listing, name='update-listing'),
    path('publish-listing/', views.publish_listing, name='publish-listing'),
    path('delete-listing/', views.delete_listing, name='delete-listing'),

]
