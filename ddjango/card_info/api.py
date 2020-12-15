from card_info.models import CardInfo

def get_card(id = 0):
    return CardInfo.objects.get(id=id)

def get_all_cards():
    return CardInfo.objects.all()

def get_cards_by_color(color=''):
    return CardInfo.objects.filter(colors__card_color__exact=color)
