from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['date','regno','name', 'age', 'gender', 'phone','doctor', 'address']
