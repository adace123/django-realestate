# Generated by Django 2.1.2 on 2019-01-18 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0004_auto_20190118_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]
