# properties/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from properties.models import Property, Amenity

class AllPropertiesViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create amenities
        self.amenity1 = Amenity.objects.create(name="WiFi", font_awesome_class="fa-wifi", order=1)
        self.amenity2 = Amenity.objects.create(name="Pool", font_awesome_class="fa-pool", order=2)

        # Create properties
        self.property1 = Property.objects.create(
            host=self.user,
            title="Property 1",
            description="A nice property",
            address="123 Main St",
            city="CityA",
            state="StateA",
            country="CountryA",
            postal_code="12345",
            latitude=45.0,
            longitude=-75.0,
            price_per_night=30.00,
            max_guests=4,
            number_of_bedrooms=2,
            number_of_bathrooms=1,
            availability=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            featured=True
        )
        self.property1.amenities.add(self.amenity1)

        self.property2 = Property.objects.create(
            host=self.user,
            title="Property 2",
            description="Another nice property",
            address="456 Main St",
            city="CityB",
            state="StateB",
            country="CountryB",
            postal_code="67890",
            latitude=46.0,
            longitude=-76.0,
            price_per_night=100.00,
            max_guests=6,
            number_of_bedrooms=3,
            number_of_bathrooms=2,
            availability=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            featured=True
        )
        self.property2.amenities.add(self.amenity2)

    def test_all_properties_view(self):
        response = self.client.get(reverse('all_properties'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'properties/all_properties.html')
        self.assertContains(response, 'Property 1')
        self.assertContains(response, 'Property 2')

    def test_all_properties_view_with_filters(self):
        response = self.client.get(reverse('all_properties'), {
            'city': 'CityA',
            'bedrooms': 2,
            'bathrooms': 1,
            'price': '25-39.99',
            'amenities': [self.amenity1.id]
        })
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'properties/all_properties.html')
        self.assertContains(response, 'Property 1')
        self.assertNotContains(response, 'Property 2')

    def test_all_properties_view_with_pagination(self):
        response = self.client.get(reverse('all_properties'), {'page': 1})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'properties/all_properties.html')
        self.assertContains(response, 'Property 1')
        self.assertContains(response, 'Property 2')
