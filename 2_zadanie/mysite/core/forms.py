from django import forms
from .models import link

    
class LinkForm(forms.ModelForm):
    link = forms.CharField(max_length=2000, widget=forms.TextInput(attrs={"class":"form-control me-2","placeholder": "Input the link","aria-label":"Search","name":"link_holder"}))
    class Meta:
        model = link
        fields = ['link']
    