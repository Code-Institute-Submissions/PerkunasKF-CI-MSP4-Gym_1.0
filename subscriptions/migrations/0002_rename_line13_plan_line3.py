# Generated by Django 3.2 on 2022-02-12 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='line13',
            new_name='line3',
        ),
    ]
