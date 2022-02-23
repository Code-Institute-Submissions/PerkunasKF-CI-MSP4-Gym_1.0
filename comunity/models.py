from django.db import models

from profiles.models import UserProfile

# Create your models here.


class ComunityMessages(models.Model):
    """ Model for user messages """

    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='messages')
    username = models.CharField(max_length=50, null=False, blank=False)
    title = models.CharField(max_length=50, null=True, blank=True)
    message_content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    like = models.BooleanField(default=False, null=False, blank=True)

    def __str__(self):
        return self.title