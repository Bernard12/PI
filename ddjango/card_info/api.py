from card_info.models import CardInfo
from card_color.models import CardColor

def get_card(id = 0):
    return CardInfo.objects.get(id=id)

def get_all_cards():
    return CardInfo.objects.all()

def get_cards_by_color(color=''):
    return CardInfo.objects.filter(colors__card_color__exact=color)

def create_card(title='', author='', card_image=None, expansion='', card_type='', colors=[], lore_message=None, lore_author=None):
    card_colors = CardColor.objects.filter(card_color__in=colors)
    card = CardInfo.objects.create(
        title=title,
        author=author,
        card_image=card_image,
        expansion=expansion,
        type=card_type,
        lore_message=lore_message,
        lore_author=lore_author,
    )
    for col in card_colors:
        print(col)
        card.colors.add(col)
    return card.id
