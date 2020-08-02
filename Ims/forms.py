from django import forms
from .models import Laptop,Mobile,Desktop

class Desktopform(forms.ModelForm):
    class Meta:
        model=Desktop
        fields=('type','price','status','issue')

class Mobileform(forms.ModelForm):
    class Meta:
        model=Mobile
        fields=('type','price','status','issue')

class Laptopform(forms.ModelForm):
    class Meta:
        model=Laptop
        fields=('type','price','status','issue')