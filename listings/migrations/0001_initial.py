# Generated by Django 2.1.2 on 2019-01-18 07:55

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999)])),
                ('is_published', models.BooleanField(default=True)),
                ('price', models.FloatField()),
                ('bedrooms', models.FloatField()),
                ('bathrooms', models.FloatField()),
                ('garage', models.IntegerField(default=1)),
                ('sqft', models.FloatField()),
                ('lot_size', models.FloatField()),
                ('list_date', models.DateTimeField()),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='realtors.Realtor')),
            ],
        ),
        migrations.CreateModel(
            name='ListingPhoto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(default=None, upload_to='')),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.Listing')),
            ],
        ),
    ]
