# Generated by Django 2.1.2 on 2019-01-18 07:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('contact_date', models.DateTimeField()),
                ('listing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='listings.Listing')),
            ],
        ),
    ]