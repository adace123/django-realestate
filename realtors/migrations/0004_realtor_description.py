# Generated by Django 2.1.2 on 2019-01-21 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0003_auto_20190119_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
