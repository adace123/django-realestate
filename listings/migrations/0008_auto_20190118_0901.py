# Generated by Django 2.1.2 on 2019-01-18 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20190118_0858'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='description',
            field=models.TextField(null=True),
        ),
    ]