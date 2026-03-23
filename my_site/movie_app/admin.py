from modeltranslation.admin import TabbedTranslationAdmin
from django.contrib import admin
from .models import (Country, City, Service, Hotel, HotelImage,
                     Room, RoomImage, Booking, Review, UserProfile)


class CityInline(admin.TabularInline):
    model = City
    extra = 1


class HotelImageInline(admin.TabularInline):
    model = HotelImage
    extra = 1


class RoomImageInline(admin.TabularInline):
    model = RoomImage
    extra = 1


class RoomInline(admin.TabularInline):
    model = Room
    extra = 1


@admin.register(Country)
class CountryAdmin(TabbedTranslationAdmin):
    inlines = [CityInline]
    list_display = ['country_name']


@admin.register(City)
class CityAdmin(TabbedTranslationAdmin):
    list_display = ['city_name', 'country']


@admin.register(Service)
class ServiceAdmin(TabbedTranslationAdmin):
    list_display = ['service_name']


@admin.register(Hotel)
class HotelAdmin(TabbedTranslationAdmin):
    inlines = [HotelImageInline, RoomInline]
    list_display = ['hotel_name', 'sity', 'hotel_stars', 'owner']
    list_filter = ['hotel_stars', 'sity']


@admin.register(Room)
class RoomAdmin(TabbedTranslationAdmin):
    inlines = [RoomImageInline]
    list_display = ['hotel', 'hotel_number', 'room_type', 'room_status', 'price']
    list_filter = ['room_type', 'room_status']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'room', 'user', 'check_in', 'check_out']
    list_filter = ['check_in', 'check_out']


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['hotel', 'user', 'ratting', 'created_date']
    list_filter = ['ratting']


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name', 'last_name', 'role', 'phone_number']
    list_filter = ['role']