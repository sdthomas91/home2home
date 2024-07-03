from django import forms
from .models import Order, OrderLineItem

class CheckoutForm(forms.Form):
    # Checkout address fields
    street_address1 = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Street Address 1'}))
    street_address2 = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'Street Address 2'}))
    town_or_city = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Town or City'}))
    county = forms.CharField(max_length=255, required=False, widget=forms.TextInput(attrs={'placeholder': 'County'}))
    country = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Country'}))
    postcode = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'placeholder': 'Postcode'}))

    # Checkout payment fields
    card_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'placeholder': 'Card Number'}))
    expiry_date = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'MM/YY'}))
    cvv = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'placeholder': 'CVV'}))
    save_payment_details = forms.BooleanField(required=False)
