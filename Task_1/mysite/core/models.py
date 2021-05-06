from django.db import models
from django.forms import ModelForm

class link(models.Model):
    link = models.CharField(max_length=2000)
    # date = models.DateField(null=True, blank=False)

    def __str__(self):
        return self.link
    
    # class Meta:
    #     ordering = ['-date']

class LinkForm(ModelForm):
    class Meta:
        model = link
        fields = ['link']
    