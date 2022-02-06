from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


# Create your models here.


class UserProfile(models.Model):
    """
    A user profile model for maintaining default
    delivery informations and order history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    defaul_tphone_number = models.CharField(max_length=20, null=True, blank=True)
    defaul_tcountry = CountryField(blank_label='Country *', null=True, blank=True)
    defaul_tpostcode = models.CharField(max_length=20, null=True, blank=True)
    defaul_ttown_or_city = models.CharField(max_length=40, null=True, blank=True)
    defaul_tstreet_address1 = models.CharField(max_length=80, null=True, blank=True)
    defaul_tstreet_address2 = models.CharField(max_length=80, null=True, blank=True)
    defaul_tcounty = models.CharField(max_length=80, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserProfile.object.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()