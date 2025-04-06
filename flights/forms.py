from django import forms
from .models import Airline, City, Flight


class AirlineForm(forms.ModelForm):
    class Meta:
        model = Airline
        fields = ['name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }


class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = ['name', 'code']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'code': forms.TextInput(attrs={'class': 'form-control'}),
        }


class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['airline', 'origin', 'destination', 'departure', 'arrival', 'price', 'flight_id']
        widgets = {
            'airline': forms.Select(attrs={'class': 'form-control'}),
            'origin': forms.Select(attrs={'class': 'form-control'}),
            'destination': forms.Select(attrs={'class': 'form-control'}),
            'departure': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'arrival': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'flight_id': forms.TextInput(attrs={'class': 'form-control'}),
        }
