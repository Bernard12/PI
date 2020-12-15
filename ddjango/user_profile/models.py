from django.db import models
from card_info.models import CardInfo

# Create your models here.
class UserProfile(models.Model):
    name = models.CharField(max_length=128, null=False, blank=True)
    purchased_cards = models.ManyToManyField(CardInfo)