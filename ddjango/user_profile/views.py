from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods

from user_profile.user_profile_form import UserProfileForm
from user_profile.models import UserProfile 
from user_profile.api import get_user


# Create your views here.
@require_http_methods(["GET"])
def user_profile(req):

    form = UserProfileForm(req.GET)

    if not form.is_valid():
        return JsonResponse({ 'error': form.errors })
    
    try:
        user = get_user(form.cleaned_data['id'])
        return JsonResponse({ 'name': user.name, 'purchased_cards': [] })
    except UserProfile.DoesNotExist:
        return JsonResponse({ 'status': 'Not found' }, status=404)
