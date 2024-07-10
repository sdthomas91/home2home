from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        widget=forms.TextInput(
            attrs={'placeholder': 'Enter Full Name', 'class': 'form-control'}
            ),
        required=True
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={'placeholder': 'Enter Email', 'class': 'form-control'}
            ),
        required=True
    )
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Type your message...', 'class': 'form-control'
                }
            ),
        required=True
    )
