from django import forms

class BookingForm(forms.Form):
    checkin = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    checkout = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    guests = forms.ChoiceField(choices=[(i, i) for i in range(1, 7)], widget=forms.Select(attrs={'class': 'form-control'}))
