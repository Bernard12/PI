from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(["GET", "POST"])
def card_profile(req, id = None):
    return JsonResponse({
        'Title': 'Simple name',
        'author': 'John doe',
        'image_url': 'https://example.com',
        'description': { 'message': 'Wow', 'author': 'somebody' },
        'color': ['red', 'blue'],
        'expansion': 'zandikar',
        'type': 'human soldier'
    })

@require_http_methods(["GET", "POST"])
def cards_list(req):
    return JsonResponse({ 'cards': [] })

@require_http_methods(["GET", "POST"])
def cards_list_by_color(req, category = None):
    return JsonResponse({ 'cards': [] })
