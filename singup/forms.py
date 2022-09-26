from django import forms
from .models import Member




class MemberRegistration(forms.ModelForm):
    class Meta:
        model=Member
        fields=['firstname','lastname','Email','password']
        widgets={
            'firstname':forms.TextInput(attrs={'class':'form-control'}),
            'lastname':forms.TextInput(attrs={'class':'form-control'}),
            'Email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }
