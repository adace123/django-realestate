# Generated by Django 2.1.2 on 2019-01-21 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0004_realtor_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realtor',
            name='photo',
            field=models.ImageField(default=None, upload_to='realtor_imgs'),
        ),
    ]
