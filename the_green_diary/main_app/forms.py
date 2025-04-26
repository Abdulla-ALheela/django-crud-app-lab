from django import forms
from .models import Watering 
from .models import Plant


class WateringForm(forms.ModelForm):
    class Meta:
        model = Watering 
        fields = ['water_amount', 'date' ]
        widgets = {
            'date': forms.DateInput(
                attrs={
                    'type': 'date',  # 🔥 this triggers the date picker
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                }
            )
        }

class PlantForm(forms.ModelForm):
    class Meta:
        model = Plant
        fields = ['name' , 'species', 'date_added', 'description', 'image']
        widgets = {
            'date_added': forms.DateInput(
                attrs={
                    'type': 'date',
                    'placeholder': 'Select a date',
                    'class': 'col-form-label col-form-label-sm mt-4 form-floating mb-3'
                },
                format='%Y-%m-%d'
            ),
        }

