
from django import forms
from bmi.models import User




class BmiCalculator(forms.ModelForm):
    class Meta:
        model=User
        fields=['FullName','Gender','height','Weight','BMI_Calculate']
        widgets={
            'FullName':forms.TextInput(attrs={'class':'form-control'}),
            'Gender':forms.TextInput(attrs={'class':'form-control'}),
            'height':forms.TextInput(attrs={'class':'form-control'}),
            'Weight':forms.TextInput(attrs={'class':'form-control'}),
            'BMI_Calculate':forms.TextInput(attrs={'class':'form-control'}),
        }
