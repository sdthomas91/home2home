# bookings/tests.py
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from properties.models import Property
from bookings.models import Booking
from django.test import Client
from django.contrib.messages import get_messages

class BookingViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.property = Property.objects.create(
            host=self.user,
            title="Test Property",
            description="A test property.",
            address="123 Main St",
            city="Anytown",
            state="Anystate",
            country="Anycountry",
            postal_code="12345",
            latitude=45.0,
            longitude=-75.0,
            price_per_night=100.00,
            max_guests=4,
            number_of_bedrooms=2,
            number_of_bathrooms=1,
            availability=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            featured=True
        )
        self.client.login(username='testuser', password='password')

    def test_book_property_view_no_active_booking(self):
        response = self.client.get(reverse('book_property', args=[self.property.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'properties/property_detail.html')

        post_data = {
            'checkin': '2023-01-01',
            'checkout': '2023-01-05',
            'guests': 2
        }
        response = self.client.post(reverse('book_property', args=[self.property.id]), post_data)
        self.assertEqual(response.status_code, 302)  # Redirect to basket
        self.assertTrue(Booking.objects.filter(user=self.user, property=self.property).exists())
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'Your dates are available! Please proceed to checkout')

    def test_book_property_view_with_active_booking(self):
        Booking.objects.create(
            user=self.user,
            property=self.property,
            checkin=timezone.now(),
            checkout=timezone.now() + timezone.timedelta(days=1),
            guests=2,
            status='Pending'
        )
        response = self.client.get(reverse('book_property', args=[self.property.id]))
        self.assertEqual(response.status_code, 302)  # Redirect to basket
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(str(messages[0]), 'You already have an active booking in your basket. Please complete the checkout first.')

    def test_basket(self):
        Booking.objects.create(
            user=self.user,
            property=self.property,
            checkin=timezone.now(),
            checkout=timezone.now() + timezone.timedelta(days=1),
            guests=2,
            status='Pending'
        )
        response = self.client.get(reverse('basket'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookings/basket.html')
        self.assertContains(response, 'Test Property')
