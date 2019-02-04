from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from realtors.models import Realtor
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.conf import settings
from django.core.exceptions import ValidationError
from utils import *
from constants import *

from pathlib import Path
import re

LISTING_TYPES = [('HOUSE', 'House'), ('APT', 'Apartment'), ('CONDO', 'Condominium')] 

# Create your models here.
class Listing(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, unique=True)
    realtor = models.ForeignKey(to=Realtor, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    street = models.CharField(null=False, max_length=100)
    city = models.CharField(null=False, max_length=50)
    state = models.CharField(null=False, max_length=2, choices=STATES)
    unit_number = models.CharField(null=True, max_length=4, blank=True)
    zipcode = models.IntegerField(null=False, validators=[MaxValueValidator(99999)])
    is_published = models.BooleanField(default=True)
    price = models.DecimalField(null=False, decimal_places=2, default=0, max_digits=11, validators=[MinValueValidator(1)])
    bedrooms = models.FloatField(default=1)
    bathrooms = models.FloatField(default=1)
    garage = models.IntegerField(default=1)
    sqft = models.FloatField(default=None)
    lot_size = models.FloatField(default=None)
    list_date = models.DateTimeField(auto_now=False, auto_now_add=True)
    listing_type = models.CharField(max_length=100, default=LISTING_TYPES[0], choices=LISTING_TYPES)
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    class Meta:
        unique_together = ("state", "city", "zipcode", "street", "unit_number")

    def __str__(self):
        return self.title
    
    @property
    def photos(self):
        return self.listingphoto_set.all()

    @property
    def main_photo(self):
        return self.photos.get(is_main=True)

    @property
    def additional_photos(self):
        return self.photos.filter(is_main=False)

    @property
    def photo_upload_path(self):
        fields = [self.state, self.city, self.zipcode, self.street]
        photo_path = [re.sub(r'[\s-]', '_', str(field).lower().replace('.', ''))\
                     for field in fields]
        if self.unit_number:
            photo_path[-1] += f"_{str(self.unit_number).lower()}"
        return Path('listing_imgs').joinpath(*photo_path)

    def save(self, *args, **kwargs):
        if not self.title:
            self.title = f"{self.street}"
            if self.unit_number:
                self.title += f" - Unit {self.unit_number}"
        prev = Listing.objects.get(pk=self.pk) if self.pk else None
        fields = ['state', 'zipcode', 'city', 'street']
        updated = any(getattr(self, field, None) != getattr(prev, field, None) for field in fields)
        if (prev and updated) or not self.pk:
            coords = get_address_coordinates(self, fields)
            if coords:
                self.longitude = coords['x']
                self.latitude = coords['y']
        if prev:
            prev_path, curr_path = prev.photo_upload_path, self.photo_upload_path
            if prev and prev_path != curr_path:
                move_photos(prev_path, curr_path, self.photos)
                remove_empty_photo_folders()
        super(Listing, self).save(*args, **kwargs)


def listing_upload_path(obj, filename):
    path = obj.listing.photo_upload_path
    base_name = f"photo_{str(obj.listing.listingphoto_set.count() + 1)}.jpeg"
    return obj.listing.photo_upload_path.joinpath(base_name)

class ListingPhoto(models.Model):
    listing = models.ForeignKey(to=Listing, on_delete=models.CASCADE)
    photo = models.ImageField(default=None, upload_to=listing_upload_path) 
    is_main = models.BooleanField(default=False)

    def __str__(self):
        return "Main Photo" if self.is_main else f"Additional Photo"

    @property
    def url(self):
        return self.photo.name
    

@receiver(post_delete, sender=ListingPhoto)
def remove_photo(sender, **kwargs):
    obj = kwargs['instance']
    photo_path = Path.cwd().joinpath('media', obj.url)
    photo_path.unlink()
    remove_empty_photo_folders()
    if photo_path.parent.exists():
        rename_photos_on_delete(photo_path.parent, obj.listing.photos)
