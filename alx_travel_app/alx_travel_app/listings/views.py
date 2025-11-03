from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Property, Booking, Review


def property_list(request):
    """Display all available properties"""
    properties = Property.objects.filter(is_available=True)
    location = request.GET.get('location', '')
    property_type = request.GET.get('type', '')
    
    if location:
        properties = properties.filter(location__icontains=location)
    if property_type:
        properties = properties.filter(property_type=property_type)
    
    context = {
        'properties': properties,
        'location': location,
        'property_type': property_type,
    }
    return render(request, 'listings/property_list.html', context)


def property_detail(request, pk):
    """Display single property details"""
    property = get_object_or_404(Property, pk=pk)
    reviews = property.reviews.all()
    
    context = {
        'property': property,
        'reviews': reviews,
    }
    return render(request, 'listings/property_detail.html', context)


@login_required
def booking_create(request, property_id):
    """Create a new booking"""
    property = get_object_or_404(Property, pk=property_id)
    
    if request.method == 'POST':
        # Handle booking creation
        pass
    
    context = {
        'property': property,
    }
    return render(request, 'listings/booking_form.html', context)


@login_required
def my_bookings(request):
    """Display user's bookings"""
    bookings = Booking.objects.filter(user=request.user)
    
    context = {
        'bookings': bookings,
    }
    return render(request, 'listings/my_bookings.html', context)


@login_required
def review_create(request, property_id):
    """Create a review for a property"""
    property = get_object_or_404(Property, pk=property_id)
    
    if request.method == 'POST':
        # Handle review creation
        pass
    
    context = {
        'property': property,
    }
    return render(request, 'listings/review_form.html', context)
