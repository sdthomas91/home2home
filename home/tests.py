# home/tests.py
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from properties.models import Property
from reviews.models import Review
from users.models import User

class HomeViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='hostuser', password='password')

        self.property1 = Property.objects.create(
            host=self.user,
            title="Featured Property 1",
            description="A beautiful featured property.",
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
        self.property2 = Property.objects.create(
            host=self.user,
            title="Featured Property 2",
            description="Another beautiful featured property.",
            address="456 Main St",
            city="Anytown",
            state="Anystate",
            country="Anycountry",
            postal_code="12345",
            latitude=45.0,
            longitude=-75.0,
            price_per_night=150.00,
            max_guests=5,
            number_of_bedrooms=3,
            number_of_bathrooms=2,
            availability=True,
            created_at=timezone.now(),
            updated_at=timezone.now(),
            featured=True
        )
        self.review = Review.objects.create(
            guest=self.user,
            property=self.property1,
            host=self.user,
            rating=5,
            comment="Great place!",
            created_at=timezone.now(),
            updated_at=timezone.now()
        )

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
        self.assertContains(response, 'Featured Property 1')
        self.assertContains(response, 'Featured Property 2')
        self.assertContains(response, 'Great place!')
