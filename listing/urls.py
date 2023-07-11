from django.urls import path
from . import views

urlpatterns = [
    path('create-city/', views.create_city, name='create_citys'),
    path('update-city/', views.update_city, name='update_citys'),
    path('cities/', views.get_city, name='get_city'),
    path('city-detail/', views.city_detail, name='city_detail'),
    path('delete-city/', views.delete_city, name='delete_citys')
]
