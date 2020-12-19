from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_view(req):
    username = req.user.username
    return render(req, 'home.html', { 'name': username })
