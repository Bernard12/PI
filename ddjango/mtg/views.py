from django.shortcuts import render, render_to_response
from django.http import HttpResponse, JsonResponse

def customer_profile(req, id = None):
    return JsonResponse({ 'name': 'John Doe', 'purchased_cards': [] })

def card_profile(req, id = None):
    return JsonResponse({ 'Title': 'Simple name', 'author': 'John doe', 'image_url': 'https://example.com', 'description': { 'message': 'Wow', 'author': 'somebody' } })

def cards_list(req):
    return JsonResponse({ 'cards': [] })

def cards_list_by_category(req, category = None):
    return JsonResponse({ 'cards': [] })