# Generated by Django 2.1.2 on 2019-01-19 04:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0023_listingphoto_is_main'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='address',
            new_name='street',
        ),
    ]
