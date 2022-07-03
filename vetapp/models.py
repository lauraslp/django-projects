from django.db import models
# from django.conf import settings
from users.models import User
# from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator


class Client(models.Model):
    OWNER_CHOICES = (('YES', 'Yes'), ('NO', 'No'))
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    address = models.CharField( max_length=150)
    email = models.EmailField()
    is_owner = models.CharField(choices=OWNER_CHOICES, max_length=3)

    def __str__(self):
        return f'Client:{self.firstname}-{self.firstname}'

class Pet(models.Model):
    SPECIES_CHOICE = (('CAT','Cat'), ('DOG','Dog'), ('RABBIT','Rabbit'))
    SEX_CHOICE = (('MALE','Male'),('FEMALE','Female'))
    MICROCHIP_CHOICE = (('YES','Yes'), ('NO','No'))
    # card_no = models.CharField(max_length=10, editable=False, unique=True, default=create_card_no)
    name = models.CharField(max_length=50)
    species = models.CharField(choices=SPECIES_CHOICE,max_length=20)
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    sex = models.CharField(choices=SEX_CHOICE,max_length=6)
    weight = models.PositiveIntegerField(validators=[MaxValueValidator(99)])
    birthday = models.DateField(blank=True)
    microchip = models.CharField(choices=MICROCHIP_CHOICE,max_length=3)
    microchip_code = models.CharField(max_length=15, blank=True, unique=True)

    def __str__(self):
        return f'Pet:{self.species}-{self.name}'


class PetOwner(models.Model):
    pet_id = models.ForeignKey(Pet, on_delete=models.CASCADE)
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)

class Drug(models.Model):
    pass

class Visit(models.Model):
    TREATMENT_CHOICE = (('MEDICA', 'Medical'), ('SURGICAL', 'Surgical'), ('OTHER', 'Other'))
    ANESTESIA_CHOICES = (('YES','Yes'), ('NO','No'))
    DRUGS_CHOICES = (('ANTIPARASITIS', 'Antiparasitis'), ('ANTIFUNGALS', 'Antifungal'), ('STEROIDS', 'Steroids'), ('PAIN RELIEVES', 'Pain Relieves'))
    date = models.DateField(verbose_name="Visit date", blank=True)
    owner_id = models.ForeignKey(PetOwner, on_delete=models.PROTECT)
    notes = models.CharField(verbose_name="Visit notes", max_length=300)
    treatment = models.CharField(choices=TREATMENT_CHOICE, max_length=10)
    drug_id = models.CharField(choices=DRUGS_CHOICES, max_length=100)
    anestesia = models.CharField(choices=ANESTESIA_CHOICES, max_length=3)
    vet_id = models.ForeignKey(User, on_delete=models.PROTECT)


class Card(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    visit = models.ForeignKey(Visit, on_delete=models.CASCADE)
    # user_details = models.ForeignKey(User, on_delete=models.CASCADE )





