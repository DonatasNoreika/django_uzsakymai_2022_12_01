from .models import MyOrder
from django import forms

class OrderCreateForm(forms.ModelForm):
    class Meta:
        model = MyOrder
        fields = ('user', 'status')
        widgets = {'user': forms.HiddenInput()}
