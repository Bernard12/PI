from rest_framework import serializers
from card_color.models import COLOR_CHOICES

class CardColorSerializer(serializers.Serializer):
    card_color = serializers.ChoiceField(COLOR_CHOICES)
