from django.contrib import admin
from django.urls import path, re_path
from user_profile.views import user_profile
from card_info.views import card_profile, cards_list, cards_list_by_category

urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('user/(?P<id>\d+)', user_profile),
    re_path('card/(?P<id>\d+)', card_profile),
    re_path('cards', cards_list),
    re_path('cards/(?P<category>\w+)', cards_list_by_category),
]
