from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Property, Amenity, PropertyImage
from .forms import PropertyCreateForm, PropertyImageForm

def all_properties(request):
    """
    View to display all properties with filters
    """
    properties = Property.objects.all()

    city = request.GET.get('city')
    bedrooms = request.GET.get('bedrooms')
    bathrooms = request.GET.get('bathrooms')
    price = request.GET.get('price')
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
        'selected_amenities': amenities,
    })

def property_detail(request, property_id):
    """
    View to display selected property details
    """
    property = get_object_or_404(Property, id=property_id)
    return render(
        request,
        'properties/property_detail.html',
        {'property': property}
        )

@login_required
def add_property(request):
    if not request.user.profile.user_type == 'Host':
        messages.error(request, 'You must be a host to add a property.')
        return redirect('home')

    if request.method == 'POST':
        form = PropertyCreateForm(request.POST)
        if form.is_valid():
            property_instance = form.save(commit=False)
            property_instance.host = request.user
            property_instance.save()
            
            for file in request.FILES.getlist('images'):
                PropertyImage.objects.create(property=property_instance, image=file)
            
            messages.success(request, 'Property added successfully!')
            return redirect('property_detail', property_id=property_instance.id)
    else:
        form = PropertyCreateForm()
        image_form = PropertyImageForm()

    return render(request, 'properties/add_property.html', {'form': form, 'image_form': image_form})
