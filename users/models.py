from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    CLINIC_CHOICES = (('FAST GIRAFFE', 'Fast Giraffe'), ('CARE VET', 'Care Vet'), ('DRPAWPAW', 'DrPawPaw'), ('DR.VET', 'Dr.Vet'))
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(null=True, max_length=50, blank=True)
    username = models.CharField(max_length=50, unique=True)
    photo = models.ImageField(upload_to='profile_pics', default='default.png', blank=True)
    email = models.EmailField(verbose_name='email address', max_length=100, unique=True)
    clinic = models.CharField(choices=CLINIC_CHOICES, max_length=100)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'clinic']




