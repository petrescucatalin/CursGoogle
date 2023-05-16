from django import forms
from .models import Company
from .models import Location

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'website']

class LocationForm(forms.ModelForm):
     class Meta:
         model = Location
         fields = ['name']  # Include whatever fields you have in your Location model
