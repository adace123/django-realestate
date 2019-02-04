# Generated by Django 2.1.2 on 2019-02-01 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0008_auto_20190128_0349'),
        ('contacts', '0004_contact_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='realtor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='realtors.Realtor'),
            preserve_default=False,
        ),
    ]
