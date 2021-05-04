from django.db import models
from django.forms import ModelForm

class link(models.Model):
    link = models.CharField(max_length=2000)
    
    def __str__(self):
        return self.link

class LinkForm(ModelForm):
    class Meta:
        model = link
        fields = ['link']
    