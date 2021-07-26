from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    """User model"""

    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('NB', 'Non-Binary'),
    )


    username = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    first_names = models.CharField(max_length=30, blank=True)
    last_names = models.CharField(max_length=30, blank=True)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email', ]

    objects = UserManager()

    class Meta:

        verbose_name = 'User'
        verbose_name_plural = 'Users'
        db_table = 'user'
        unique_together = ['username', 'email']

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_fullname(self):
        return self.first_names + " " + self.last_names
