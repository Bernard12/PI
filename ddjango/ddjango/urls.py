from django.contrib import admin
from django.urls import path, re_path
from mtg.views import customer_profile, card_profile, cards_list, cards_list_by_category

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('customer/(?P<id>\d+)', customer_profile),
    re_path('card/(?P<id>\d+)', card_profile),
    re_path('cards', cards_list),
    re_path('cards/(?P<category>\w+)', cards_list_by_category),
]
