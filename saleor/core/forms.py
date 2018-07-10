from django import forms
from django.utils.translation import pgettext_lazy

from .models import CustomDesign


class CustomDesignForm(forms.ModelForm):
    class Meta:
        model = CustomDesign
        exclude = ['user']
        labels = {
            'name': pgettext_lazy(
                'Name of design', 'Name'),
            'image': pgettext_lazy(
                'Design image', 'Image'),
        }
