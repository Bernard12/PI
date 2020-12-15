from django.contrib import admin
from card_info.models import CardInfo

# Register your models here.
class CardInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'expansion', 'type', 'get_colors')

    def get_colors(self, obj):
        return ' '.join([p.card_color for p in obj.colors.all()])

admin.site.register(CardInfo, CardInfoAdmin)
