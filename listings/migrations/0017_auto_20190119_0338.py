# Generated by Django 2.1.2 on 2019-01-19 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0016_auto_20190119_0327'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='apt_number',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='listing_type',
            field=models.CharField(blank=True, choices=[('HOUSE', 'House'), ('APT', 'Apartment'), ('CONDO', 'Condominium')], default=('HOUSE', 'House'), max_length=100),
        ),
    ]