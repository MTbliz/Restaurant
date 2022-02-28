from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    name = forms.CharField(
        label='Imię',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Imię",
                "style": "max-width:300px"
            }
        )
    )
    last_name = forms.CharField(
        label='Nazwisko',
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Nazwisko",
                "style": "max-width:300px"
            }
        )
    )
    email = forms.EmailField(
        label='Email',
        widget=forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Email",
                "style": "max-width:300px"
            }
        )
    )
    description = forms.CharField(
        label='Description',
        required=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "Opis rezerwacji",
                "id": "my-id-for-textarea",
                "rows": 8,
                "style": "max-width:600px"
            }
        )
    )

    class Meta:
        model = Reservation
        fields = [
            'name',
            'last_name',
            'email',
            'description'
        ]
