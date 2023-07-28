from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Entry(models.Model):
    """ Entry for saving data/information"""

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=225, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=255, default='Other')
    completed = models.BooleanField(default=False)
    image = models.ImageField(
        # upload_to='images/',
        # default='../media/images/default_post_keitpn',
    )

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return f"Entry:{self.id},Owner:{self.owner}, Entry:{self.id}"