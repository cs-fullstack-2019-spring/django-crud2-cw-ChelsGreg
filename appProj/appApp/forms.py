from django import forms
from .models import Application

# FORM TO SYNC MODEL
class AppForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = '__all__'