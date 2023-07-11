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
         name='delete_listingtypes')
]
