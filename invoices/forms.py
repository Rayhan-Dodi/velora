from django import forms
from django.forms import inlineformset_factory
from .models import Invoice, InvoiceItem

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['client', 'date', 'due_date']

InvoiceItemFormSet = inlineformset_factory(
    Invoice,
    InvoiceItem,
    fields=['description', 'quantity', 'unit_price'],
    extra=1,
    can_delete=True
)
