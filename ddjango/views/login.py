from django.shortcuts import render

def login_view(req):
    return render(req, 'login.html', {})
