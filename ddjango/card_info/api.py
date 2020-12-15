from card_info.models import CardInfo
from card_color.models import CardColor

def get_card(id = 0):
    return CardInfo.objects.get(id=id)

def get_all_cards():
    return CardInfo.objects.all()

def get_cards_by_color(color=''):
    return CardInfo.objects.filter(colors__card_color__exact=color)

def create_card(title='', author='', image_url='', expansion='', card_type='', color=[], lore_message=None, lore_author=None):
    card_colors = CardColor.objects.filter(card_color__in=color)
    card = CardInfo.objects.create(
        title=title,
        author=author,
        image_url=image_url,
        expansion=expansion,
        type=card_type,
        lore_message=lore_message,
        lore_author=lore_author,
    )
    for col in card_colors:
        print(col)
        card.colors.add(col)
