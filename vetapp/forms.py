from datetime import datetime
from django import forms
from django.contrib.auth.forms import UserCreationForm
from bootstrap_datepicker_plus.widgets import DatePickerInput, DateTimePickerInput
from users.models import User
# from django.contrib.auth.models import User
from .models import Card, Client, Pet, Visit

class RegisterForm(UserCreationForm):

    first_name = forms.CharField(help_text=False, label='First Name', required=False)
    last_name = forms.CharField(help_text=False, label='Last Name', required=False)
    username = forms.CharField(help_text=False, label='Username')
    email = forms.EmailField(help_text=False, label='Email')
    # clinic = forms.ChoiceField()
    password1 = forms.CharField(widget=forms.PasswordInput(), help_text=False, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput(), help_text=False, label='Confirm password')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'clinic', 'password1', 'password2')
        # fields = ['username', 'password1', 'password2']


class CardForm(forms.ModelForm):
    card_no = forms.CharField(label='Card No.',
                              widget=forms.TextInput(attrs={'placeholder': 'Card No.: YYYY-00000', 'class':'form-control'}))
    date_time = forms.DateTimeField(label='Date of Registration', input_formats=['%Y-%m/%d %H:%M'],
                                widget=DateTimePickerInput(format='%Y-%m-%d %H:%M'))
    user_clinic = forms.CharField(label='Clinic',
                             widget=forms.TextInput(attrs={'readonly': 'readonly', 'class':'form-control'}))

    class Meta:
        model = Card
        fields = '__all__'



class ClientForm(forms.ModelForm):
    OWNER_CHOICES = (('YES', 'Yes'),
                     ('NO', 'No'))
    is_owner = forms.CharField(label='Is the owner of this animal?', widget=forms.RadioSelect(choices=OWNER_CHOICES))
    firstname = forms.CharField(label='First Name', help_text=False)
    lastname = forms.CharField(label='Last Name', help_text=False)
    address = forms.CharField(help_text=False, label='Address')
    email = forms.EmailField(label='Email', help_text=False)
    class Meta:
        model = Client
        fields = ('is_owner', 'firstname', 'lastname', 'address', 'email')


class PetForm(forms.ModelForm):
    SPECIES_CHOICE = (('CAT','Cat'),
                      ('DOG','Dog'),
                      ('RABBIT','Rabbit'))
    SEX_CHOICE = (('MALE','Male'),
                  ('FEMALE','Female'))
    MICROCHIP_CHOICE = (('YES','Yes'),
                        ('NO','No'))
    name = forms.CharField(label='Name', help_text=False)
    species = forms.CharField(label='Species', widget=forms.RadioSelect(choices=SPECIES_CHOICE))
    breed = forms.CharField(label='Breed', help_text=False)
    color = forms.CharField(help_text=False, label='Color')
    sex = forms.CharField(label='Sex', widget=forms.RadioSelect(choices=SEX_CHOICE))
    # weight = forms.IntegerField()
    birthday = forms.DateField(label='Date of Birth', input_formats=['%Y-%m/%d'],
                                widget=DatePickerInput(format='%Y-%m-%d'))
    microchip = forms.CharField(label='Microchip', widget=forms.RadioSelect(choices=MICROCHIP_CHOICE))
    microchip_code = forms.CharField(label='Microchip ID', help_text=False)
    class Meta:
        model = Pet
        fields = '__all__'


class VisitForm(forms.ModelForm):
    TREATMENT_CHOICE = (('MEDICAL', 'Medical'),
                         ('SURGICAL', 'Surgical'),
                         ('OTHER', 'Other'))
    DRUG_CHOICE = (('ANTIPARASITICS', 'Antiparasitics'),
                    ('ANTIFUNGALS', 'Antifungals'),
                    ('STEROIDS', 'Steroids'),
                    ('PAIN RELIEVERS', 'Pain Relievers'))
    ANESTESIA_CHOICE = (('YES', 'Yes'),
                        ('NO', 'No'))
    date = forms.DateTimeField(label='Visit Date and Time', input_formats=['%Y-%m/%d %H:%M'],
                                widget=DateTimePickerInput(format='%Y-%m-%d %H:%M'))
    notes = forms.CharField(label='Visit notes',
                            widget=forms.Textarea(attrs={'cols': 200, 'rows': 1, 'style': 'width: 100%'}))
    treatment = forms.CharField(label='Treatment',
                                widget=forms.CheckboxSelectMultiple(choices=TREATMENT_CHOICE))
    drug = forms.CharField(label='Drugs',
                                widget=forms.CheckboxSelectMultiple(choices=DRUG_CHOICE))
    anestesia = forms.CharField(label='Anestesia', widget=forms.RadioSelect(choices=ANESTESIA_CHOICE))
    class Meta:
        model = Visit
        fields = '__all__'

