from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from django.views.decorators.http import require_http_methods

from card_info.card_info_forms import CardListColorForm, CardProfileForm, CardCreateForm, CardImageUploadForm
from card_info.models import CardInfo
from card_info.api import get_cards_by_color, get_all_cards, get_card, create_card, upload_card_image
from card_info.serializers import CardInfoSerializer

from rest_framework.views import APIView

# Create your views here.
@require_http_methods(["GET"])
def card_profile(req):
    form = CardProfileForm(req.GET)

    if not form.is_valid():
        return JsonResponse({ 'error': form.errors }, status=400)

    try:
        card = get_card(form.cleaned_data['id'])
        serialized_card = CardInfoSerializer(card)
        return JsonResponse({ 'card': serialized_card.data })
    except CardInfo.DoesNotExist:
        return JsonResponse({ 'error': 'Not found' }, status=404)

@require_http_methods(["GET"])
def cards_list(req):
    try:
        cards = get_all_cards()
        serialized_cards = [CardInfoSerializer(single_card).data for single_card in cards ]
        return JsonResponse({ 'cards': serialized_cards })
    except CardInfo.DoesNotExist:
        return JsonResponse({ 'cards': [] }, status=404)

@require_http_methods(["GET"])
def cards_list_by_color(req):
    form = CardListColorForm(req.GET)

    if not form.is_valid():
        return JsonResponse({ 'errors': form.errors }, status=400)

    try:
        cards = get_cards_by_color(form.cleaned_data['color'])
        serialized_cards = [CardInfoSerializer(single_card).data for single_card in cards ]
        return JsonResponse({ 'cards': serialized_cards })
    except CardInfo.DoesNotExist:
        return JsonResponse({ 'cards': [] }, status=404)


class CardCreateView(APIView):
    def post(self, req):
        form = CardCreateForm(req.POST)
        
        if not form.is_valid():
            return JsonResponse({ 'errors': form.errors }, status_code=400)

        # create_card(title='', author='', card_image=None, expansion='', card_type='', colors=[], lore_message=None, lore_author=None) -> id:
        title = form.cleaned_data['title']
        author = form.cleaned_data['author']
        expansion = form.cleaned_data['expansion']
        card_type = form.cleaned_data['type']
        colors = form.cleaned_data['colors']

        lore_message = form.cleaned_data['lore_message']
        lore_author = form.cleaned_data['lore_author']

        card_id = create_card(title, author, None, expansion, card_type, colors, lore_message, lore_author)
        return JsonResponse({ 'status' : 'Card created', 'id': card_id })


class CardImageUploadView(APIView):
    def post(self, req):
        form = CardImageUploadForm(req.POST, req.FILES or None)

        if not form.is_valid():
            return JsonResponse({ 'errors': form.errors })

        card_id = form.cleaned_data['card_id']
        card_image = form.cleaned_data['card_image']

        try:
            upload_card_image(card_id, card_image)
            return JsonResponse({ 'status' : 'image uploaded successfuly' })
        except err:
            print(err)
            return JsonResponse({ 'error' : 'failed to upload image' })



