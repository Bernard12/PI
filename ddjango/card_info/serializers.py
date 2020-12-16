from rest_framework import serializers
from card_color.serializers import CardColorSerializer

class CardInfoSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=128)
    author = serializers.CharField(max_length=128)
    image_url = serializers.CharField(max_length=128)
    expansion = serializers.CharField(max_length=128)
    type = serializers.CharField(max_length=128)

    colors = CardColorSerializer(many=True)

    lore_message = serializers.CharField(max_length=128)
    lore_author = serializers.CharField(max_length=128)
