from django.db import models
from user_profile.models import UserProfile
from card_info.models import CardInfo

# Create your models here.
class PurchasedCard(models.Model):
    owner_id = models.ForeignKey(UserProfile, on_delete=models.DO_NOTHING)
    card_id = models.ForeignKey(CardInfo, on_delete=models.DO_NOTHING) 