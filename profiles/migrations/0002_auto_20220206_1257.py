# Generated by Django 3.2 on 2022-02-06 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaul_tcountry',
            new_name='default_country',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaul_tcounty',
            new_name='default_county',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaul_tphone_number',
            new_name='default_phone_number',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaul_tpostcode',
            new_name='default_postcode',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaul_tstreet_address1',
            new_name='default_street_address1',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaul_tstreet_address2',
            new_name='default_street_address2',
        ),
        migrations.RenameField(
            model_name='userprofile',
            old_name='defaul_ttown_or_city',
            new_name='default_town_or_city',
        ),
    ]
