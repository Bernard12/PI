from django.contrib import admin
from django.urls import path
from user_profile.views import user_profile
from card_info.views import card_profile, cards_list, cards_list_by_color, CardCreateView, CardImageUploadView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', user_profile),
    path('api/v1/card', card_profile),
    path('api/v1/card/create', CardCreateView.as_view()),
    path('api/v1/card/upload/image', CardImageUploadView.as_view()),
    path('api/v1/cards', cards_list),
    path('api/v1/cards/color', cards_list_by_color),
]
