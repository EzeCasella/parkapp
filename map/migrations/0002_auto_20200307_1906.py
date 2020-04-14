# Generated by Django 3.0.3 on 2020-03-07 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parking',
            name='address',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='parking',
            name='carSlots',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='parking',
            name='notes',
            field=models.CharField(default='', max_length=400),
        ),
        migrations.AddField(
            model_name='parking',
            name='openingHours',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='parking',
            name='phoneNumber',
            field=models.IntegerField(default=0),
        ),
    ]
