# Generated by Django 2.1.2 on 2019-01-19 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0019_auto_20190119_0345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='apartment_number',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]