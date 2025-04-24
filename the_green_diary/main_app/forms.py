from django import forms
from .models import Watering 
from .models import Plant


class WateringForm(forms.ModelForm):
    class Meta:
        model = Watering 
        fields = ['water_amount', 'date' ]
        widgets = {'date': forms.DateInput(format=('%Y-%m-%d'),attrs={  'placeholder': 'Select a date', 'type': 'date'}),}

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = '__all__'
        widgets = {
            'date_added': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'Select a date',
                },
                format='%Y-%m-%d'
            ),
        }
