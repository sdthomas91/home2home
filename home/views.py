from django.shortcuts import render
from properties.models import Property

def home(request):
    featured_properties = Property.objects.filter(featured=True)[:4]
    return render(request, 'home/index.html', {'featured_properties': featured_properties})