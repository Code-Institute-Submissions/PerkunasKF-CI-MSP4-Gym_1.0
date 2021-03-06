# Generated by Django 3.2 on 2022-02-06 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_countries.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('defaul_tphone_number', models.CharField(blank=True, max_length=20, null=True)),
                ('defaul_tcountry', django_countries.fields.CountryField(blank=True, max_length=2, null=True)),
                ('defaul_tpostcode', models.CharField(blank=True, max_length=20, null=True)),
                ('defaul_ttown_or_city', models.CharField(blank=True, max_length=40, null=True)),
                ('defaul_tstreet_address1', models.CharField(blank=True, max_length=80, null=True)),
                ('defaul_tstreet_address2', models.CharField(blank=True, max_length=80, null=True)),
                ('defaul_tcounty', models.CharField(blank=True, max_length=80, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE,to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
