from django.db import models
from django.core.validators import RegexValidator
from pathlib import Path

def realtor_img_path(obj, filename):
    split_name = '-'.join([val.lower() for val in obj.name.split()])
    return Path("realtor_imgs", f"{split_name}.jpeg")

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Realtor Name')
    email = models.EmailField()
    description = models.TextField(blank=True, null=True)
    hire_date = models.DateField()
    phone = models.CharField(max_length=20, validators=[RegexValidator(r'\(?([0-9]{3})\)?([ .-]?)([0-9]{3})\2([0-9]{4})')])
    is_mvp = models.BooleanField()
    photo = models.ImageField(default=None, upload_to=realtor_img_path)        

    def __str__(self):
        return self.name