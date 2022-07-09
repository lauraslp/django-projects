from django.db import models
# from django.conf import settings
from users.models import User
# from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from datetime import datetime
from computed_property import ComputedTextField


class Card(models.Model):
    card_no = models.CharField(max_length=10)
    date_time = models.DateTimeField(auto_now=True)
    user_clinic = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.card_no

class Client(models.Model):
    OWNER_CHOICES = (('YES', 'Yes'),
                     ('NO', 'No'))
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=100)
    address = models.CharField( max_length=150)
    email = models.EmailField(blank=True)
    is_owner = models.CharField(max_length=3, choices = OWNER_CHOICES)

    def __str__(self):
        return f'{self.firstname} {self.firstname}'


class Pet(models.Model):
    SPECIES_CHOICE = (('CAT','Cat'),
                      ('DOG','Dog'),
                      ('RABBIT','Rabbit'))
    SEX_CHOICE = (('MALE','Male'),
                  ('FEMALE','Female'))
    MICROCHIP_CHOICE = (('YES','Yes'),
                        ('NO','No'))
    name = models.CharField(max_length=50)
    species = models.CharField(max_length=20, choices=SPECIES_CHOICE)
    breed = models.CharField(max_length=50)
    color = models.CharField(max_length=20)
    sex = models.CharField(max_length=6, choices=SEX_CHOICE)
    birthday = models.DateField(blank=True)
    microchip = models.CharField(max_length=3, choices=MICROCHIP_CHOICE)
    microchip_code = models.CharField(max_length=15, blank=True, unique=True, null=True)
    owner = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.species}:{self.name}'

class Visit(models.Model):
    TREATMENT_CHOICE = (('MEDICAL', 'Medical'),
                         ('SURGICAL', 'Surgical'),
                         ('OTHER', 'Other'))
    DRUG_CHOICE = (('ANTIPARASITICS', 'Antiparasitics'),
                    ('ANTIFUNGALS', 'Antifungals'),
                    ('STEROIDS', 'Steroids'),
                    ('PAIN RELIEVERS', 'Pain Relievers'))
    ANESTESIA_CHOICE = (('YES', 'Yes'),
                        ('NO', 'No'))
    date = models.DateTimeField()
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    weight = models.PositiveIntegerField(validators=[MaxValueValidator(99)], null=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, blank=True, null=True)
    notes = models.CharField(max_length=300)
    treatment = models.CharField(max_length=10, choices=TREATMENT_CHOICE)
    drug = models.CharField(max_length=100, choices=DRUG_CHOICE)
    anestesia = models.CharField(max_length=3, choices=ANESTESIA_CHOICE)
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    vet = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.card}:{self.id}'

    @property
    def get_age(self):
        return 10

    # pet_age_year = property(get_age)

    # def save(self, *args, **kwargs):
    #     self.age_year = property(self.get_age)
    #     super(Visit, self).save(*args, **kwargs)


