# Generated by Django 2.1.2 on 2019-01-20 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0026_remove_listing_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='listingphoto',
            name='index',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]