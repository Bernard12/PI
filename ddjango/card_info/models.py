from django.db import models
from card_color.models import CardColor

# Create your models here.
class CardInfo(models.Model):
    title = models.CharField(max_length=128, null=False)
    author = models.CharField(max_length=128, null=False)
    expansion = models.CharField(max_length=128, null=False)
    type = models.CharField(max_length=128, null=False)
    colors = models.ManyToManyField(CardColor)

    card_image = models.ImageField(null=True, blank=True, upload_to='card_images')

    lore_message = models.CharField(max_length=128, null=True)
    lore_author = models.CharField(max_length=128, null=True)
