from django import forms
from django.core.validators import MaxLengthValidator
from django.forms import NumberInput, TextInput


class ContactForm(forms.Form):
        parent_name = forms.CharField(max_length=50, label='Parent Name ')
        child_name = forms.CharField(max_length=50, label="Toddler's Name ")
        child_dob = forms.DateField(label="Toddler's Date of birth", widget=NumberInput(attrs={'type': 'date'}))
        contact_number = forms.IntegerField(label='Phone Number ', widget=forms.NumberInput(attrs={'placeholder': 'XXXXXXXXXX'}))
        email_address = forms.EmailField(label="Email Address ")
        filled_details = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Please tell us your concern in maximum 100 words', 'style': "position=relative; top=0"}))