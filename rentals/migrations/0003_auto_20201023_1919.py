# Generated by Django 3.1 on 2020-10-23 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rentals', '0002_auto_20201022_1750'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentals',
            name='agent',
        ),
        migrations.AddField(
            model_name='rentals',
            name='main_image',
            field=models.ImageField(default='https://photos.google.com/photo/AF1QipOK45w-YPGkrI5Y-Njk8IP6eXFwisNgGkBlfJzR', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='rentals',
            name='size',
            field=models.CharField(max_length=30),
        ),
    ]
