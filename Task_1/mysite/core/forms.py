from django import forms
from .models import link
from django.core.validators import URLValidator

    
class LinkForm(forms.ModelForm):
    link = forms.CharField(max_length=2000, widget=forms.TextInput(attrs={"class":"form-control me-2","placeholder": "Input the link","aria-label":"Search","name":"link_holder"}))
    
    class Meta:
        model = link
        fields = ['link']
    
    def clean_link(self):
        domain_zone = ["ru","com","org","xyz","ua","рф"]
        Link = self.cleaned_data['link']
        url_validator = URLValidator(Link)
        try:
            url_validator(Link)
        except:
            raise forms.ValidationError("Invalid Link!")
        return(Link)