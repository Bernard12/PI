from mimesis import Person, Generic, Text, Business, Choice
from elasticsearch import Elasticsearch 

# title -> str
# author -> name 
# expansion -> str
# type -> str
# colors -> str[]  
#
# lore_message -> str
# lore_author -> name

def generate_card_info(n=2):
    res = []

    en_text = Text('en')
    en_person = Person('en')
    en_business = Business('en')

    color_choice = Choice()

    for i in range(n):
        card = {
            'title': en_text.title(),
            'author': en_person.full_name(),
            'expansion': en_text.word(),
            'type': en_text.word(),

            'colors': color_choice(items=['white', 'black', 'red', 'green', 'blue'], unique=True, length=2),

            'lore_message': en_text.quote(),
            'lore_author': en_person.full_name()


        }
        res.append(card)

    return res

def insert_data_to_elastic(data=[]):
    es = Elasticsearch()
    for i in data:
        es.index(index='card_info', body=i)

data = generate_card_info(n=50)
insert_data_to_elastic(data)
