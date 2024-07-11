from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib.messages import get_messages
from properties.models import Property
from bookings.models import Booking
from checkout.models import Order
from users.models import Profile

class CheckoutSuccessViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='password')
        self.profile, created = Profile.objects.get_or_create(user=self.user, defaults={'user_type': 'Host'})
        
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
        
        self.booking = Booking.objects.create(
            user=self.user,
            property=self.property,
            checkin=timezone.now(),
            checkout=timezone.now() + timezone.timedelta(days=1),
            guests=2,
            status='Confirmed'
        )
        
        self.order = Order.objects.create(
            booking=self.booking,
            user_profile=self.profile,
            first_name='Test',
            last_name='User',
            email='testuser@example.com',
            phone_number='1234567890',
            country='Test Country',
            postcode='12345',
            town_or_city='Test City',
            street_address1='123 Test St',
            street_address2='',
            county='Test County',
            total_price=100.00,
            payment_status='Pending',
            stripe_pid='test_stripe_pid'
        )
        self.client.login(username='testuser', password='password')

    def test_checkout_success_view(self):
        session = self.client.session
        session['save_info'] = True
        session.save()

        response = self.client.get(reverse('checkout_success', args=[self.order.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout_success.html')

        order = Order.objects.get(id=self.order.id)
        profile = Profile.objects.get(user=self.user)

        # Check if the order is assigned to the user's profile
        self.assertEqual(order.user_profile, profile)

        # Check if the profile's default payment information is updated
        self.assertEqual(profile.default_payment_method, order.phone_number)
        self.assertEqual(profile.country, order.country)
        self.assertEqual(profile.postal_code, order.postcode)
        self.assertEqual(profile.city, order.town_or_city)
        self.assertEqual(profile.address_1, order.street_address1)
        self.assertEqual(profile.address_2, order.street_address2)
        self.assertEqual(profile.state, order.county)

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), f'Order successfully processed! Your order number is {self.order.order_number}. A confirmation email will be sent to {self.order.email}.')
