# Generated by Django 2.1.2 on 2019-01-19 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0013_auto_20190119_0232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='realtor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='realtors.Realtor'),
        ),
    ]