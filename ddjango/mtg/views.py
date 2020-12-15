from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET", "POST"])
def customer_profile(req, id = None):
    return JsonResponse({ 'name': 'John Doe', 'purchased_cards': [] })

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
def cards_list_by_category(req, category = None):
    return JsonResponse({ 'cards': [] })