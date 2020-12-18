from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from user_profile.models import UserProfile 
from user_profile.api import get_user_by_name

from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
@require_http_methods(["GET"])
def user_profile(req):
    try:
        username = req.user.username
        user = get_user_by_name(username)
        return JsonResponse({ 'name': user.name, 'purchased_cards': [] })
    except UserProfile.DoesNotExist:
        return JsonResponse({ 'status': 'Not found' }, status=404)
