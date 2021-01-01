# Generated by Django 3.1 on 2020-11-08 17:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0004_auto_20201031_2009'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=100)),
                ('estate', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('rent', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('garage', models.IntegerField(default=0)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('is_published', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
        migrations.DeleteModel(
            name='RentalImage',
        ),
        migrations.DeleteModel(
            name='rentals',
        ),
    ]