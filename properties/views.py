from django.shortcuts import render
from .models import Property

def all_properties(request):
    properties = Property.objects.all()

    city = request.GET.get('city')
    if city:
        properties = properties.filter(city=city)

    return render(request, 'properties/all_properties.html', {'properties': properties})
