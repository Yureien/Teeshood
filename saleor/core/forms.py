from django import forms
from django.utils.translation import pgettext_lazy

from .models import CustomDesign, BulkOrder


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


class BulkOrderForm(forms.ModelForm):
    class Meta:
        model = BulkOrder
        exclude = []
        labels = {
            'name': pgettext_lazy(
                'Name', 'Name'),
            'email': pgettext_lazy(
                'E-Mail', 'E-Mail'),
            'phone_number': pgettext_lazy(
                'Phone Number', 'Phone Number'),
            'product_type': pgettext_lazy(
                'Type', 'Type'),
            'product_color': pgettext_lazy(
                'Color', 'Color'),
            'number_of_pieces': pgettext_lazy(
                'Number of Pieces', 'Number of Pieces'),
            'upload_design': pgettext_lazy(
                'Upload Design', 'Upload Design (zip file < 25 mb)'),
            'list_of_names': pgettext_lazy(
                'List Of Names', 'List Of Names (if required, excel sheet)'),
            'additional_description': pgettext_lazy(
                'Additional Description', 'Additional Description'),
            'teeshood_designs_product': pgettext_lazy(
                'Teeshood designs product', 'I would like TEESHOOD to design my product?'),
        }
