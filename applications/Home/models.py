from django.db import models

# Create your models here.
from model_utils.models import TimeStampedModel

class Home(TimeStampedModel):
    
    title = models.CharField('Title', max_length=50)
    description = models.TextField()
    about_title = models.CharField('About Title', max_length=50)
    about_text = models.TextField()
    email = models.EmailField()
    phone = models.CharField('Contact Phone', max_length=20)

    class Meta:
        verbose_name = "Main Page"
        verbose_name_plural = "Main Page"
        db_table = "home"
    
    def __str__(self):
        return self.title

class Subscriber(TimeStampedModel):

    email = models.EmailField()

    class Meta:
        verbose_name = "Subscriber"
        verbose_name_plural = "Subscribers"
        db_table = "subscriber"

    def __str__(self):
        return self.email

class Contact(TimeStampedModel):

    full_name = models.CharField("Name", max_length=20)
    email = models.EmailField()
    message = models.TextField()

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"
        db_table = "contact"

    def __str__(self):
        return self.email