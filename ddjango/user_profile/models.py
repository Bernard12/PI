from django.db import models

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=128, null=False, blank=True)