from django.db import models

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

# Create your models here.
class CardColor(models.Model):
    card_color = models.CharField(max_length=5, choices=COLOR_CHOICES)


    def __str__(self):
        return f"{self.card_color}"
