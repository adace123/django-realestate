from django.db import models
from listings.models import Listing
from realtors.models import Realtor

# Create your models here.
class Contact(models.Model):
    name = models.CharField(null=False, max_length=100)
    email = models.EmailField(null=False)
    listing = models.ForeignKey(to=Listing, on_delete=models.CASCADE)
    realtor = models.ForeignKey(to=Realtor, on_delete=models.CASCADE)
    message = models.TextField(null=False)
    contact_date = models.DateTimeField(auto_now=True)
    responded = models.BooleanField(default=False)
