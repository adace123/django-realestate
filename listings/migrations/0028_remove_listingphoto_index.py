# Generated by Django 2.1.2 on 2019-01-20 11:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0027_listingphoto_index'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listingphoto',
            name='index',
        ),
    ]
