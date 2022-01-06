from django import forms

class ProductForm(forms.Form):
    nom = forms.CharField(label ='nom', max_length=100)
    qty = forms.IntegerField(label ='qty')
