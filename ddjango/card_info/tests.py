from django.test import TestCase, Client
from factory import Faker, Factory, Sequence, SubFactory, post_generation
from factory.fuzzy import FuzzyChoice

import card_info
from card_info.models import CardInfo
from card_color.models import CardColor, COLOR_CHOICES
from card_info.serializers import CardInfoSerializer

from unittest.mock import patch
import json

# Views to test

# card_profile
# cards_list
# cards_list_by_color

# CardCreateView post
# CardImageUploadView: post


COLORS = [x[0] for x in COLOR_CHOICES]
class CardColorFactory(Factory):
    class Meta:
        model = CardColor

    card_color = FuzzyChoice(COLORS)

class CardProfileFactory(Factory):
    class Meta:
        model = CardInfo

    title = Faker('name')
    author = Faker('name')
    expansion = Faker('company')
    type = Faker('name')

    lore_message = Faker('name')
    lore_author = Faker('name')

    # colors = SubFactory(CardColorFactory)

    @post_generation
    def colors(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            # A list of groups were passed in, use them
            for color in extracted:
                self.colors.add(color)


class CardProfileTest(TestCase):
    def setUp(self):
        self.client = Client()

        colors = CardColorFactory.build_batch(2)
        [col.save() for col in colors]

        self.card = CardProfileFactory.create()
        self.card.save()
        self.card.colors.set(colors)

    def test_should_return_error_if_form_error(self):
        response = self.client.get('/api/v1/card')
        self.assertEquals(response.status_code, 400)

    def test_should_return_404_if_not_found(self):
        response = self.client.get('/api/v1/card?id=10000')
        self.assertEquals(response.status_code, 404)

    def test_should_return_200_if_found(self):
        response = self.client.get(f'/api/v1/card?id={self.card.id}')
        self.assertEquals(response.status_code, 200)

    def test_should_return_same_object_from_setup(self):
        response = self.client.get(f'/api/v1/card?id={self.card.id}')
        self.assertEquals(response.status_code, 200)
        res_json = json.loads(response.content)['card']

        self.assertEqual(self.card.title, res_json['title'])
        self.assertEqual(self.card.author, res_json['author'])
        self.assertEqual(self.card.expansion, res_json['expansion'])
        self.assertEqual(self.card.type, res_json['type'])

class CardListTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.card1 = CardProfileFactory.create()
        self.card1.save()

        self.card2 = CardProfileFactory.create()
        self.card2.save()


        self.colors = CardColorFactory.build_batch(2)
        [col.save() for col in self.colors]

        self.card1.colors.add(self.colors[0])
        self.card2.colors.add(self.colors[1])

    def test_should_return_all_cards(self):
        response = self.client.get('/api/v1/cards')
        self.assertEquals(response.status_code, 200)
        res_json = json.loads(response.content)['cards']

        self.assertEquals(res_json[0]['title'], self.card1.title)
        self.assertEquals(res_json[1]['title'], self.card2.title)

    @patch('card_info.views.get_all_cards', autospec=True)
    def test_should_return_404_if_error(self, get_all_cards_mock):
        get_all_cards_mock.side_effect = CardInfo.DoesNotExist('mocked excpetion')
        response = self.client.get('/api/v1/cards')

        self.assertTrue(get_all_cards_mock.called)
        self.assertEquals(response.status_code, 404)

    def test_should_400_if_form_is_invalid(self):
        response = self.client.get('/api/v1/cards/color')
        self.assertEquals(response.status_code, 400)

    def test_should_return_card_list_by_color(self):
        response = self.client.get(f'/api/v1/cards/color?color={self.colors[0].card_color}')
        res_json = json.loads(response.content)['cards']

        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(res_json), 1)
        self.assertEquals(res_json[0]['title'], self.card1.title)

    @patch('card_info.views.get_cards_by_color', autospec=True)
    def test_should_return_404_on_error(self, get_cards_by_color_mock):
        get_cards_by_color_mock.side_effect = CardInfo.DoesNotExist('mocked excpetion')

        missing_color = None
        used_colors = [i.card_color for i in self.colors]
        for i in COLORS:
            if not i in used_colors:
                missing_color = i

        self.assertTrue(missing_color != None)
        response = self.client.get(f'/api/v1/cards/color?color={missing_color}')
        self.assertEquals(response.status_code, 404)        
