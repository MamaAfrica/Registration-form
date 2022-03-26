from django import forms
# from django.forms import ModelForm
from .models import Register
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

import datetime

GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
EVENT_CHOICES = [('Perform', 'Perform'), ('Dynatrace go', 'Dynatrace go'), ('Amplify', 'Amplify')]


# DATE_INPUT_FORMATS = []

class RegisterForm(forms.Form):
    email = forms.EmailField()
    birthday = forms.DateField(input_formats=["%d/%m/%Y","%Y-%m-%d"],error_messages={'ValueError': "Date Format must be DD/MM"})
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)
    phone = forms.CharField(max_length=30)
    gender = forms.ChoiceField(choices=GENDER_CHOICES)
    event = forms.ChoiceField(choices=EVENT_CHOICES)

    # class Meta:
    #     model = Register
    #     fields = ['first_name', 'last_name', 'birthday', 'email', 'phone', 'gender', 'event']

    def clean_email(self):
        cleaned_data = self.cleaned_data
        email = cleaned_data.get('email')
        try:
            validate_email(email)
        except ValidationError:
            print("bad email, details:", ValidationError)
        else:
            print("good email")
        return email

    # def clean_birthday(self):
    #     print(self.cleaned_data)
    #     birthday = self.cleaned_data.get('birthday')
    #     print(birthday)
    #     print("validating birthday")
    #     try:
    #         birthday = datetime.datetime.strptime(str(birthday), "%d/%m/%Y")
    #         print(birthday)
    #         print("validated birthday")
    #     except ValueError:
    #         print("validation failed")
    #     #     return birthday
    #         # raise ValueError("Date Format must be DD/MM/YYYY")
    #     return birthday
