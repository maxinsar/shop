from django import forms

PRODUCT_QTY = [(i, str(i)) for i in range(1,21)]

class AddProductToCartForm(forms.Form):
    qty = forms.TypedChoiceField(choices = PRODUCT_QTY,
     coerce = int)
    update = forms.BooleanField(required = False,
     initial = False,
     widget = forms.HiddenInput)
