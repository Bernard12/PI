from django import forms
from django.core.exceptions import ValidationError

from card_color.models import COLOR_CHOICES
from card_info.models import CardInfo

def _parse_color_string(cols):
    list_colors = cols.split(',')

    defined_colors = [col[0] for col in COLOR_CHOICES]

    for col in list_colors:
        if not col in defined_colors:
            raise ValidationError(f"Unkown color '{col}'")
    return list_colors

class CardCreateForm(forms.ModelForm):
    colors = forms.CharField(max_length=128)

    class Meta:
        model = CardInfo
        fields = ('title', 'author', 'expansion', 'type', 'lore_message', 'lore_author')

    def clean_colors(self):
        raw_colors = self.cleaned_data['colors']
        return _parse_color_string(raw_colors)

class CardProfileForm(forms.Form):
    id = forms.IntegerField()

class CardListColorForm(forms.Form):
    color = forms.ChoiceField(choices = COLOR_CHOICES)

class CardImageUploadForm(forms.Form):
    card_id = forms.IntegerField()
    card_image = forms.ImageField()

class CardSearchForm(forms.Form):
    title = forms.CharField()
