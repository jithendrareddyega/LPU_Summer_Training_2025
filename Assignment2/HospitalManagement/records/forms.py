from django import forms
from .models import Patient

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'age', 'contact', 'diagnosis', 'admission_date']  # Correct fields from your model
