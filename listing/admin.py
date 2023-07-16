from django.contrib import admin
from .models import City, ListingType, Listing, ListingImage


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


@admin.register(ListingType)
class ListingTypeAdmin(admin.ModelAdmin):
    list_display = ('listing_type',)
    search_fields = ('listing_type',)


class ListingImageInline(admin.TabularInline):
    model = ListingImage
    extra = 1


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'type_of_listing',
                    'authour', 'is_published')
    list_filter = ('is_published', 'city', 'type_of_listing')
    search_fields = ('title', 'city__name', 'authour__username')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ListingImageInline]


@admin.register(ListingImage)
class ListingImageAdmin(admin.ModelAdmin):
    list_display = ('listing', 'image_alt')
    list_filter = ('listing',)


# Register your models here.
