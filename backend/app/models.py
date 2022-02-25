from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class PhoneValidator(RegexValidator):
    regex = r'^\+?1?\d{9,15}$'
    message = "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."

class Organization(models.Model):
    name = models.CharField(max_length=50)
    notes = models.TextField(max_length=200)
class Source(models.Model):
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, null=True, related_name="sources") 
    email = models.EmailField()
    notes = models.TextField(max_length=200)
    # maybe do regex for phone?
    phone = models.CharField(validators=[PhoneValidator], max_length=17, blank=True)