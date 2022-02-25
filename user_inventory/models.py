from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserInventory(models.Model):
    """
    A user inventory model for maintaining user
    unique item inventory and order history
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    username = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_inventory(sender, instance, created, **kwargs):
    """
    Create or update the user inventory
    """
    if created:
        UserInventory.objects.create(user=instance)
    # Existing users: just save the profile
    instance.userprofile.save()
