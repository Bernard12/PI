from django.conf.urls import url, include
from django.contrib import admin
from django.urls import path
from user_profile.views import user_profile
from card_info.views import card_profile, cards_list, cards_list_by_color, CardCreateView, CardImageUploadView

from django.contrib.auth import views as auth_views
from views.login import login_view
from views.home import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user', user_profile),

    path('home/', home_view),

    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('social_auth/', include('social_django.urls', namespace='social')),

    path('api/v1/card', card_profile),
    path('api/v1/card/create', CardCreateView.as_view()),
    path('api/v1/card/upload/image', CardImageUploadView.as_view()),
    path('api/v1/cards', cards_list),
    path('api/v1/cards/color', cards_list_by_color),
]
