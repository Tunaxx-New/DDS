from django import forms

from records.models import Record, SubCategory


class RecordForm(forms.ModelForm):
    class Meta:
        model = Record
        fields = ['purpose', 'type', 'category', 'subcategory', 'sum', 'note']


class SubCategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ['name']
