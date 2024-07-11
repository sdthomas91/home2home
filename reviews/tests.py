# reviews/tests.py
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from properties.models import Property
from reviews.models import Review
from reviews.forms import ReviewForm
from bookings.models import Booking

class WriteReviewViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.property = Property.objects.create(
            host=self.user,
            title="Test Property",
            description="A nice property",
            address="123 Main St",
            city="CityA",
            state="StateA",
            country="CountryA",
            postal_code="12345",
            latitude=45.0,
            longitude=-75.0,
            price_per_night=50.00,
            max_guests=4,
            number_of_bedrooms=2,
            number_of_bathrooms=1,
            availability=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            featured=True
        )
        self.booking = Booking.objects.create(
            user=self.user,
            property=self.property,
            checkin=timezone.now().date(),
            checkout=(timezone.now() + timezone.timedelta(days=1)).date(),
            guests=2,
            status='Confirmed'
        )
        self.client.login(username='testuser', password='password')

    def test_write_review_view_get(self):
        response = self.client.get(reverse('write_review', args=[self.property.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'reviews/write_review.html')
        self.assertIsInstance(response.context['form'], ReviewForm)
        self.assertEqual(response.context['property'], self.property)

    def test_write_review_view_post_success(self):
        post_data = {
            'rating': 5,
            'comment': 'Great place!'
        }
        response = self.client.post(reverse('write_review', args=[self.property.id]), post_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful review submission
        self.assertTrue(Review.objects.filter(guest=self.user, property=self.property).exists())
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'Your review has been submitted.')

    def test_write_review_view_post_no_stay(self):
        other_user = User.objects.create_user(username='otheruser', password='password')
        self.client.login(username='otheruser', password='password')
        post_data = {
            'rating': 5,
            'comment': 'Great place!'
        }
        response = self.client.post(reverse('write_review', args=[self.property.id]), post_data)
        self.assertEqual(response.status_code, 302)  # Redirect to property_detail
        self.assertFalse(Review.objects.filter(guest=other_user, property=self.property).exists())
        messages = list(response.wsgi_request._messages)
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "You haven't stayed here yet, book now!")
