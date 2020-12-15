from django.contrib import admin
from card_color.models import CardColor

# Register your models here.
class CardColorAdmin(admin.ModelAdmin):
    list_display = ('card_color', )

admin.site.register(CardColor, CardColorAdmin)
