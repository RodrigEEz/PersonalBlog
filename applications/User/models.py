from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non-Binary'),
    )


    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    first_names = models.CharField(max_length=30)
    last_names = models.CharField(max_length=30)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)

    USERNAME_FIELD = 'username'

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_fullname(self):
        return self.first_names + " " + self.last_names
