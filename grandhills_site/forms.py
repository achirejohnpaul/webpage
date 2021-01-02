from django import forms
from . models import Partnership


class PartnerWithForm(forms.ModelForm):
    class Meta:
        model = Partnership
        fields = ('partner_name', 'address', 'phone_contact', 'email_add')

        labels = {
            'partner_name': 'Partner Name/Company Name',
            'address': 'Address',
            'phone_contact': 'Phone Contact',
            'email_add': 'Email',
        }

        widgets = {
            'partner_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'phone_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'email_add': forms.TextInput(attrs={'class': 'form-control'}),

        }


class ContactForm(forms.Form):
    name = forms.CharField(required=False, max_length=500)
    email = forms.EmailField(required=True, )
    comment = forms.CharField(required=True, widget=forms.Textarea)





