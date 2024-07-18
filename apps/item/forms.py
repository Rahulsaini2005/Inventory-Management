from django import forms

from apps.item.models import Item


class AddItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')