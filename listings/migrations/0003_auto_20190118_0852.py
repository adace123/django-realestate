# Generated by Django 2.1.2 on 2019-01-18 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_auto_20190118_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
