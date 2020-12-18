from django import forms

class UserProfileByIdForm(forms.Form):
    id = forms.IntegerField()
