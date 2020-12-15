from django.contrib import admin
from card_color.models import CardColor

# Register your models here.
class CardColorAdmin(admin.ModelAdmin):
    pass

admin.site.register(CardColor, CardColorAdmin)