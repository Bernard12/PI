from django.contrib import admin
from card_info.models import CardInfo

# Register your models here.
class CardInfoAdmin(admin.ModelAdmin):
    pass

admin.site.register(CardInfo, CardInfoAdmin)