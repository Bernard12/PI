from django.db import models

# Create your models here.
class CardColor(models.Model):
    WHITE = 'white'
    BLUE = 'blue'
    RED = 'red'
    GREEN = 'green'
    BLACK = 'black'
    COLOR_CHOICES = [
        (WHITE, WHITE),
        (BLUE, BLUE),
        (RED, RED),
        (GREEN, GREEN),
        (BLACK, BLACK),
    ]

    card_color = models.CharField(max_length=5, choices=COLOR_CHOICES)