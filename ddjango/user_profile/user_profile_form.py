from django import forms

class UserProfileForm(forms.Form):
    id = forms.IntegerField()
