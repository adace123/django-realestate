# Generated by Django 2.1.2 on 2019-01-21 21:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0030_auto_20190121_1919'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='listing',
            unique_together={('state', 'city', 'zipcode', 'street', 'unit_number')},
        ),
    ]
