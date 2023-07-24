from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.
class Profile(models.Model):
    """ Profile for users creating account"""

    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=225, blank=True)

    class Meta:
    ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.owner}'s profile"

def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)

# Each time a user is created, call the create profile function
post_save.connect(create_profile, sender=User)

