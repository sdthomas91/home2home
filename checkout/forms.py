from django import forms

class CheckoutForm(forms.Form):
    card_number = forms.CharField(max_length=16, widget=forms.TextInput(attrs={'placeholder': 'Card Number'}))
    expiry_date = forms.CharField(max_length=5, widget=forms.TextInput(attrs={'placeholder': 'MM/YY'}))
    cvv = forms.CharField(max_length=3, widget=forms.TextInput(attrs={'placeholder': 'CVV'}))
