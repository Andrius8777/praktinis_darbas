from django import forms
from . import models
from .models import Mechanic


class ClientDataForm(forms.ModelForm):
    mechanic = forms.ModelChoiceField(queryset=Mechanic.objects.all(), required=False, empty_label='Pasirinkti', label="Darbus atliko")
    
    class Meta:
        model = models.ClientData
        fields = ['client_name', 'phone_number', 'issue_notes', 'number_plate', 'make', 'model', 'vin_number', 'year',
                  'engine_type', 'driven_axle', 'body_type', 'gearbox_type', 'engine_power_kw', 'engine_capacity',
                   'ordered_parts_description', 'ordered_parts_price', 'labor_cost', 'repair_notes', 'mechanic']
      
      
class MechanicForm(forms.ModelForm):
    class Meta:
        model = models.Mechanic
        fields = ('name', 'ph_number', 'skills', )


class ClientDataFilterForm(forms.Form):
    start_date = forms.DateField(label='Nuo', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    end_date = forms.DateField(label='Iki', required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    query = forms.CharField(label='', required=False, widget=forms.TextInput(attrs={'placeholder': 'Paieška'}))