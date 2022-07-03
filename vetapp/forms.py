from django import forms
# from django.forms import modelformset_factory
from django.contrib.auth.forms import UserCreationForm
from users.models import User
# from django.contrib.auth.models import User
# from betterforms.multiform import MultiForm

from .models import Client, Pet, PetOwner, Drug, Visit, Card


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
        fields = ['first_name', 'last_name', 'username', 'email', 'clinic', 'password1', 'password2']
        # fields = ['username', 'password1', 'password2']


class ClientForm(forms.ModelForm):
    OWNER_CHOICES = (('YES', 'Yes'), ('NO', 'No'))
    is_owner = forms.CharField(widget=forms.RadioSelect(choices=OWNER_CHOICES), label='Is the owner of this animal?')
    firstname = forms.CharField(help_text=False, label='First Name')
    lastname = forms.CharField(help_text=False, label='Last Name')
    address = forms.CharField(help_text=False, label='Address')
    email = forms.EmailField(help_text=False, label='Email')
    class Meta:
        model = Client
        fields = ['is_owner', 'firstname', 'lastname', 'address', 'email']


class PetForm(forms.ModelForm):
    SPECIES_CHOICE = (('CAT','Cat'), ('DOG','Dog'), ('RABBIT','Rabbit'))
    SEX_CHOICE = (('MALE','Male'),('FEMALE','Female'))
    MICROCHIP_CHOICE = (('YES','Yes'), ('NO','No'))
    # card_no = models.CharField(max_length=10, editable=False, unique=True, default=create_card_no)
    name = forms.CharField(help_text=False, label='Name')
    species = forms.CharField(widget=forms.RadioSelect(choices=SPECIES_CHOICE), label='Species')
    breed = forms.CharField(help_text=False, label='Breed')
    color = forms.CharField(help_text=False, label='Color')
    sex = forms.CharField(widget=forms.RadioSelect(choices=SEX_CHOICE), label='Sex')
    weight = forms.IntegerField()
    birthday = forms.DateField(widget = forms.SelectDateWidget(), label='Date of Birth')
    microchip = forms.CharField(widget=forms.RadioSelect(choices=MICROCHIP_CHOICE), label='Microchip')
    microchip_code = forms.CharField(help_text=False, label='Microchip ID')
    class Meta:
        model = Pet
        fields = '__all__'


class VisitForm(forms.ModelForm):
    class Meta:
        model = Visit
        fields = '__all__'

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        fields = '__all__'