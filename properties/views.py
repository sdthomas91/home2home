from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Property, Amenity

def all_properties(request):
    properties = Property.objects.all()

    city = request.GET.get('city')
    bedrooms = request.GET.get('bedrooms')
    bathrooms = request.GET.get('bathrooms')
    price = request.GET.get('price')
    pet_friendly = request.GET.get('pet_friendly')
    amenities = request.GET.getlist('amenities')

    if city:
        properties = properties.filter(city=city)
    if bedrooms:
        properties = properties.filter(number_of_bedrooms__gte=bedrooms)
    if bathrooms:
        properties = properties.filter(number_of_bathrooms__gte=bathrooms)
    if price:
        price_range = {
            "0-24.99": (0, 24.99),
            "25-39.99": (25, 39.99),
            "40-74.99": (40, 74.99),
            "75": (75, float('inf'))
        }
        min_price, max_price = price_range.get(price, (0, float('inf')))
        properties = properties.filter(price_per_night__gte=min_price, price_per_night__lte=max_price)
    if pet_friendly:
        properties = properties.filter(pets_allowed=True)
    if amenities:
        for amenity_id in amenities:
            properties = properties.filter(amenities__id=amenity_id)

    paginator = Paginator(properties, 12)  # 12 properties per page
    page_number = request.GET.get('page')
    properties_page = paginator.get_page(page_number)

    all_amenities = Amenity.objects.all()

    return render(request, 'properties/all_properties.html', {
        'properties': properties_page,
        'amenities': all_amenities,
        'selected_city': city,
        'selected_bedrooms': bedrooms,
        'selected_bathrooms': bathrooms,
        'selected_price': price,
        'selected_pet_friendly': pet_friendly,
        'selected_amenities': amenities,
    })

def property_detail(request, property_id):
    property = get_object_or_404(Property, id=property_id)
    return render(request, 'properties/property_detail.html', {'property': property})
