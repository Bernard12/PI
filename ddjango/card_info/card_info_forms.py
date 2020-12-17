from django import forms
from django.core.exceptions import ValidationError

from card_color.models import COLOR_CHOICES
from card_info.models import CardInfo

class CardCreateForm(forms.ModelForm):
    colors = forms.CharField(max_length=128)

    class Meta:
        model = CardInfo
        fields = ('title', 'author', 'expansion', 'type', 'lore_message', 'lore_author')

    def clean_colors(self):
        raw_colors = self.cleaned_data['colors']
        list_colors = raw_colors.split(',')

        defined_colors = [col[0] for col in COLOR_CHOICES]

        for col in list_colors:
            if not col in defined_colors:
                raise ValidationError(f"Unkown color '{col}'")
        return list_colors

class CardProfileForm(forms.Form):
    id = forms.IntegerField()

class CardListColorForm(forms.Form):
    color = forms.ChoiceField(choices = COLOR_CHOICES)
