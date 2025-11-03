from django.urls import path
from . import views

app_name = 'listings'

urlpatterns = [
    path('', views.property_list, name='property_list'),
    path('property/<int:pk>/', views.property_detail, name='property_detail'),
    path('property/<int:property_id>/book/', views.booking_create, name='booking_create'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('property/<int:property_id>/review/', views.review_create, name='review_create'),
]


